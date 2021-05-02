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
        self.req_method = 'GET'
        self.req_url = '/account/login'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        logger.info('响应体: ' + result.sdata)

        return result

    def req_post(self):
        self.req_method = 'POST'
        self.req_url = '/account/submit'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        logger.info('响应体: ' + result.sdata)
        return result


sample = Sample(envar.BASE_URL_CORE)

if __name__ == '__main__':
    sample.req_post()
