import json
from configparser import ConfigParser

import yaml

from util import common


# 由于[安全问题](https://security.openstack.org/guidelines/dg_avoid-dangerous-input-parsing-libraries.html)
# 建议使用yaml.safe_load()而不是yaml.load()以防止代码注入。

class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData:

    def __init__(self):
        pass

    def save_cookie_yml(self, yml_data):
        file_path = common.env('COOKIE_YML')
        # logger.debug(f"打开文件: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            tmp_data = yaml.safe_dump(yml_data, f, default_flow_style=False)  # 写入文件，不是用flow流格式
        # logger.debug(f"写入数据: {tmp_data} ")
        return tmp_data

    def load_yml(self, file_path):
        # logger.debug(f"加载文件 {file_path}")
        with open(file_path, encoding='utf-8') as f:
            tmp_data = yaml.safe_load(f)
        # logger.debug(f"读取yml {tmp_data}")
        return tmp_data

    def load_ymlist(self, file_path):
        # logger.debug(f'加载文件 {file_path}')
        with open(file_path, encoding='utf-8') as f:
            tmp_data = yaml.safe_load(f)
        # logger.debug(f'读取yml列表 {tmp_data}')
        return tmp_data

    def load_json(self, file_path):
        # logger.debug("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            tmp_data = json.load(f)
        # logger.debug(f"读取json ==>> {tmp_data} ")
        return tmp_data

    def load_ini(self, file_path):
        # logger.debug("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读取ini ==>>  {} ".format(data))
        return data

    # def process(**params):  # pass in variable numbers of args
    #     for key, value in params.items():
    #         print('%s: %s' % (key, value))
    # conf = data_tool.load_yml(path)
    # process(**conf)  # pass in your keyword args


datazoo = ReadFileData()

if __name__ == '__main__':
    pass
