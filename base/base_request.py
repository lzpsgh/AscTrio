import json as complexjson

import requests

from base.base_result import BaseResult
from util.logger import logger


class BaseRequest:
    req_method = ''
    req_url = ''
    req_body = {}
    req_headers = {}
    req_cookies = {}

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()
        self.req_headers = {
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",  # 在HTTP1.1规范中默认开启
        }

    def __str__(self):
        return f'BaseRequest object (api_root_url: {self.api_root_url})'

    __repr__ = __str__

    def request_log(self, url, data=None, json=None, params=None, headers=None, cookies=None, files=None,
                    **kwargs):
        # Python3中需要设置 ensure_ascii=False，避免json在做dumps操作时将中文转换成unicode字符
        logger.debug(f"请求URL     ==>> {url}")
        if headers is not None:
            logger.debug(f"请求header  ==>> {headers}")
        if cookies is not None:
            logger.debug(f"请求cookies ==>> {cookies}")
        if params is not None:
            logger.debug(f"请求params  ==>> {params}")
        if data is not None:
            logger.debug(f"请求data  ==>> {data}")
        if json is not None:
            logger.debug(f"请求json  ==>> {json}")
        # if files is not None:
        #     logger.info("请求体 files 参数 ==>> {}".format(files))

    def x_request(self):
        return self.request(method=self.req_method,
                            url=self.req_url,
                            params=self.req_body,
                            headers=self.req_headers,
                            cookies=self.req_cookies)

    def request(self, method, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        # todo 为什么从kwargs取出的cookies的值会变成params，而在调qequests.get时又会被还原回去。但并没影响实际功能
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, data, json, params, headers, files, cookies)

        if method == "GET":
            inner_rsp = self.session.get(url, timeout=5, **kwargs)

        if method == "POST":
            inner_rsp = requests.post(url, data, json, timeout=5, **kwargs)

        if method == "DELETE":
            inner_rsp = self.session.delete(url, **kwargs)

        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            inner_rsp = self.session.put(url, data, **kwargs)

        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            inner_rsp = self.session.patch(url, data, **kwargs)

        if inner_rsp is None:
            exit(f"sorry,requests库响应对象为空")
        # if inner_rsp.cookies
        #     logger.debug("响应头cookie/JSESSIONID ==>> " + inner_rsp.cookies.get("JSESSIONID"))
        logger.debug(f"响应data    ==>> {inner_rsp.text}")
        logger.debug(f"响应hash    ==>> {abs(inner_rsp.__hash__())}")
        logger.debug(
            f"\n\n###########################################################################################\n")
        base_result = BaseResult()
        base_result.rsp = inner_rsp

        return base_result

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request("POST", url, data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request("PUT", url, data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request("PATCH", url, data, **kwargs)
