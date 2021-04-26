import json as complexjson

import requests

from util.logger import logger


class BaseRequest:

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def request_log(self, method, url, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        # Python3中需要设置 ensure_ascii=False，避免json在做dumps操作时将中文转换成unicode字符
        logger.info("请求URL ==>> {}".format(url))
        if headers is not None:
            logger.info("请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        if cookies is not None:
            logger.debug("请求头 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
        if params is not None:
            logger.info("请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        if data is not None:
            logger.info("请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        if json is not None:
            logger.info("请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        if files is not None:
            logger.info("请求体 files 参数 ==>> {}".format(files))

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

    def request(self, method, url, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")

        self.request_log(method, url, data, json, params, headers, files, cookies)

        if method == "GET":
            # todo 为了临时解决crm和官网的cookie冲突问题，先禁用session
            # inner_rsp = requests.get(url, timeout=7, **kwargs)
            inner_rsp = self.session.get(url, timeout=7, **kwargs)

        if method == "POST":
            inner_rsp = requests.post(url, data, json, timeout=7, **kwargs)

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

        # logger.info(f"响应头cookie ==>> " + inner_rsp.cookies.get("JSESSIONID"))
        logger.info(f"响应体text   ==>> " + inner_rsp.text)
        logger.info("响应体ID   ==>> " + str(inner_rsp.__hash__()))
        logger.info("\n\n###########################################################################################\n")
        return inner_rsp
