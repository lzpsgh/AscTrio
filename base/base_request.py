import json as complexjson

import requests

from base.base_result import BaseResult
from util.log_kit import logger


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

    def request_log(self, url, data=None, json=None, params=None,
                    headers=None, cookies=None, files=None, **kwargs):
        # Python3中需要设置 ensure_ascii=False，避免json在做dumps操作时将中文转换成unicode字符
        logger.info(f"请求URL     ==>> {url}")
        if headers is not None:
            logger.debug(f"请求header  ==>> {headers}")
        if cookies is not None:
            logger.info(f"请求cookies ==>> {cookies}")
        if params is not None:
            logger.info(f"请求params  ==>> {params}")
        if data is not None:
            logger.info(f"请求data    ==>> {data}")
        if json is not None:
            logger.info(f"请求json    ==>> {json}")
        if files is not None:
            logger.info(f"请求files   ==>> {files}")

    def request(self, method, url, data=None, json=None, **kwargs):
        m_method = method.strip().upper()
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        # todo 为什么从kwargs取出的cookies的值会变成params，而在调qequests.get时又会被还原回去。但并没影响实际功能
        cookies = dict(**kwargs).get("cookies")
        inner_rsp = {}
        self.request_log(url, data, json, params, headers, files, cookies)

        if m_method == "GET":
            # inner_rsp = self.session.get(url, timeout=5, **kwargs) # 多用户场景下不能开启session会话功能
            inner_rsp = requests.get(url, timeout=5, **kwargs)

        if m_method == "POST":
            inner_rsp = requests.post(url, data, json, timeout=5, **kwargs)

        if m_method == "DELETE":
            inner_rsp = self.session.delete(url, **kwargs)

        if m_method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            inner_rsp = self.session.put(url, data, **kwargs)

        if m_method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            inner_rsp = self.session.patch(url, data, **kwargs)

        base_result = BaseResult()

        if inner_rsp is None:
            logger.warning(f"sorry,requests库响应对象为空")
            base_result.rsp = {}
        else:
            # if inner_rsp.cookies
            #     logger.debug("响应头cookie/JSESSIONID ==>> " + inner_rsp.cookies.get("JSESSIONID"))
            if 'text' in inner_rsp:
                logger.debug(f"响应data    ==>> {inner_rsp.text}")
            logger.debug(f"响应hash    ==>> {str(id(inner_rsp))}")
            # logger.debug(f"\n\n#################################################\n")
            base_result.rsp = inner_rsp
        return base_result

    # 【适用对象】用params参数的get请求 / 用json参数的post请求(对应的请求头是 application/json)
    # 【不适用对象】
    # 用 data 参数的 post 请求（建议改用原始的 request 方法 ，对应的请求头是 application/x-www-form-urlencoded）
    # 其他 put, patch 请求（建议改用原始的 request 方法）
    # todo 用try-except捕获异常
    # todo 用partial优化
    def x_request(self):
        m_method = self.req_method
        method = m_method.strip().upper()
        if method == 'GET':
            return self.request(
                method='GET', url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
                params=self.req_body
            )
        elif method == 'POST':
            # 如果调用失败，出现形如' Required String parameter xxx is not present' 或 '参数缺失 '等报错
            # 可能考虑是服务端限制了content-type为'application/x-www-form-urlencoded'
            # 此时在外部调用request函数时，将json改为data即可
            return self.request(
                method='POST', url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
                json=self.req_body
            )
        else:
            logger.error('该方法不支持其他请求方式')
            exit()

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
