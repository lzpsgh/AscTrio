# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common
from util.logger import logger


class Sample(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Sample, self).__init__(root_url, **kwargs)

    def req_get(self):
        """
        get请求
        :param username: 用户名
        :param sex: 性别
        :return: 自定义的关键字返回结果 result
        """
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request("GET", "/account/login",
                              params=self.req_body,
                              headers=self.req_headers,
                              cookies=self.req_cookies)
        common.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth.set_cookie('crm', core_jsessionid)
        logger.info(core_jsessionid)
        return result

    def req_post(self):
        """
        post请求
        :param username: 用户名
        :param sex: 性别
        :return: 自定义的关键字返回结果 result
        """
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request("POST", "/account/submit",
                              data=self.req_body,
                              headers=self.req_headers,
                              cookies=self.req_cookies)
        common.result_check(result)
        return result


sample = Sample(envar.BASE_URL_CORE)

if __name__ == '__main__':
    sample.req_post()
