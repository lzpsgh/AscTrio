#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 14:02

import argparse
import errno
import json
import os
import re
import sys
from datetime import datetime
from os import path

import requests

# TODO
# HOST = 'localhost:8080'
HOST = '10.100.2.36:11002'

# TODO
# BASE_PATH = '/'
BASE_PATH = '/station'


def check_python_version():
    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 2):
        print('Must use Python 3.2+. Current version:', sys.version)
        sys.exit(1)


def parse_cmdline_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', '-u',
                        help='Swagger API docs URL. Format: "http://<host>[:<port>][/<basePath>]/v2/api-docs" (default: http://localhost:8080/v2/api-docs)')
    parser.add_argument('--host', '-H',
                        help='Domain name or IP. (default: "localhost:8080")')
    parser.add_argument('--basePath', '-b',
                        help='URL prefix for all API paths, relative to the host root. It must start with a leading slash "/". (default: "/" )')
    parser.add_argument('--outputDir', '-o', help='Output directory path. (default: current working directory)')
    parser.add_argument('--compare', '-c',
                        help='Compare to another (old) Swagger JSON file and export newly added APIs and models.')
    parser.add_argument('--api', '-a',
                        help='Export specified API(s). Comma-separated (partial) API path(s), case sensitive. eg. "register,login"')
    parser.add_argument('--model', '-m',
                        help='Export specified model(s). Comma-separated (partial) model name(s), case sensitive. eg. "User,Files"')

    return parser.parse_args()


def get_swagger_json(url):
    try:
        r = requests.get(url)
    except:
        raise Exception('[ERROR] Invalid URL or service is not running. URL: {}'.format(url))

    if r.status_code == 200:
        try:
            response = r.json()
            if response.get('swagger'):
                return response
            else:
                raise Exception('[ERROR] Not a Swagger JSON file:\n' + str(response))
        except:
            raise
    else:
        raise Exception('[ERROR] Cannot get JSON. Status code: {}, content: {}'.format(r.status_code, r.text))


def make_dir(dir_path):
    if not path.exists(dir_path):
        try:
            os.mkdir(dir_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def export_whole_json(swagger_json, output_path):
    make_dir(output_path)

    with open(path.join(output_path, 'all.json'), 'w', encoding='utf-8') as f:
        json.dump(swagger_json, f, ensure_ascii=False)


def export_apis(swagger_json, output_path):
    make_dir(output_path)

    api_dir = path.join(output_path, 'api')
    make_dir(api_dir)

    tags = swagger_json['tags']
    for tag in tags:
        tag_name = tag['name']
        tag_dir = path.join(api_dir, tag_name)
        make_dir(tag_dir)

        apis = swagger_json['paths']
        for api in apis:
            if tag_name in json.dumps(apis[api], ensure_ascii=False):
                api_file = path.join(tag_dir, api.replace('/', '--') + '.json')
                with open(path.join(tag_dir, api_file), 'w', encoding='utf-8') as f:
                    json.dump(apis[api], f, ensure_ascii=False)


def export_models(swagger_json, output_path):
    make_dir(output_path)

    model_dir = path.join(output_path, 'model')
    make_dir(model_dir)

    models = swagger_json['definitions']
    for model in models:
        with open(path.join(model_dir, model + '.json'), 'w', encoding='utf-8') as f:
            json.dump(models[model], f, ensure_ascii=False)


def search_refs(string):
    return re.findall('"\$ref": "#/definitions/(.+?)"', string)


def write_selected_elements_to_file(selections, elements, file_obj):
    refs = []
    elements_to_write = []

    for selection in set(selections):
        for element in elements:
            if selection in element:
                content = json.dumps(elements[element], ensure_ascii=False)
                elements_to_write.append('\t\t"{}": {},\n'.format(element, content))

                refs.extend(search_refs(content))

    for element in set(elements_to_write):
        file_obj.write(element)

    return list(set(refs))


def write_all_ref_models_to_file(ref_list, model_list, file_obj):
    ref_list = list(set(ref_list))
    models_to_write = []

    while len(ref_list):
        for ref in set(ref_list):
            if ref in model_list:
                content = json.dumps(model_list[ref], ensure_ascii=False)
                models_to_write.append('\t\t"{}": {},\n'.format(ref, content))

                ref_list.extend(search_refs(content))
                if ref in ref_list:
                    ref_list.remove(ref)

    for model in set(models_to_write):
        file_obj.write(model)


def export_selected_docs(swagger_json, output_file, api_list=None, model_list=None):
    if not api_list:
        api_list = []
    if not model_list:
        model_list = []

    apis = swagger_json['paths']
    models = swagger_json['definitions']
    refs = []

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('{\n\t"swagger": "2.0",\n')
        f.write('\t"info": {},\n'.format(json.dumps(swagger_json['info'], ensure_ascii=False)))
        f.write('\t"host": "{}",\n'.format(HOST))
        f.write('\t"basePath": "{}",\n'.format(BASE_PATH))
        f.write('\t"tags": {},\n'.format(json.dumps(swagger_json['tags'], ensure_ascii=False)))

        f.write('\t"paths": {\n')
        refs.extend(write_selected_elements_to_file(api_list, apis, f))
        f.write('\t\t"":{}\n')  # Use empty element to avoid trailing comma issue
        f.write('\t},\n')

        f.write('\t"definitions": {\n')
        refs.extend(write_selected_elements_to_file(model_list, models, f))
        write_all_ref_models_to_file(refs, models, f)
        f.write('\t\t"":{}\n')  # Use empty element to avoid trailing comma issue
        f.write('\t}\n')
        f.write('}')


def export_diff_docs(old_file_path, output_path):
    if path.exists(old_file_path) and path.isfile(old_file_path):
        with open(old_file_path, encoding='utf-8') as f:
            old_swagger_json = json.load(f)

        new_apis = set(j['paths'].keys())
        old_apis = set(old_swagger_json['paths'].keys())

        added = new_apis - old_apis
        missing = old_apis - new_apis
        print('\nAdded APIs:\n{}'.format(added))
        print('Missing APIs:\n{}'.format(missing))

        if len(added):
            output_added = path.join(output_path, 'diff-added.json')
            export_selected_docs(j, output_added, added)
            print('\nAdded APIs are saved to:\n{}'.format(output_added))
        else:
            print('[INFO] No new APIs found.')

        if len(missing):
            output_missing = path.join(output_path, 'diff-missing.json')
            export_selected_docs(old_swagger_json, output_missing, missing)
            print('\nMissing APIs are saved to:\n{}'.format(output_missing))
    else:
        print('[ERROR] No such file: {}'.format(old_file_path))


if __name__ == '__main__':
    check_python_version()

    args = parse_cmdline_args()

    if args.url:
        match = re.search('https?://(.+?)(?:/v2/api-docs.*?)', args.url)
        if match:
            HOST = match.groups()[0]
            if '/' in HOST:
                match2 = re.search('(.+?)(/.*)', HOST)
                if match2:
                    HOST = match2.groups()[0]
                    BASE_PATH = match2.groups()[1]

    # overwrite "host" and "basePath" in Swagger JSON
    if args.host:
        HOST = args.host
    if args.basePath:
        BASE_PATH = args.basePath

    swagger_url = args.url or 'http://{}{}/v2/api-docs'.format(HOST, BASE_PATH)

    output_dir = path.abspath(path.expanduser(args.outputDir)) if args.outputDir else path.join(
        os.getcwd(), 'swagger_json_docs-{}'.format(datetime.now().strftime('%Y%m%d-%H%M%S')))

    j = get_swagger_json(swagger_url)

    export_whole_json(j, output_dir)
    export_apis(j, output_dir)
    export_models(j, output_dir)
    print('Saved to:\n{}'.format(output_dir))

    if args.compare:
        old_file = args.compare
        export_diff_docs(old_file, output_dir)

    if args.api or args.model:
        selected_apis = args.api.strip().split(',') if args.api else []
        selected_models = args.model.strip().split(',') if args.model else []
        output_file = path.join(output_dir, 'selected.json')

        export_selected_docs(j, output_file, selected_apis, selected_models)
        print('\nSelected APIs and models are saved to:\n{}'.format(output_file))
