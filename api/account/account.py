# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from util import auth
from util import common
from util.logger import logger


class Account(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Account, self).__init__(root_url, **kwargs)

    def crm_login_with_mm(self):
        self.req_method = 'GET'
        self.req_url = '/account/login'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
            "captcha": '1'
        }
        result = self.x_request()
        common.result_check(result)

        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth.set_cookie('crm', core_jsessionid)
        logger.info(core_jsessionid)
        return result


account = Account(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    account.crm_login_with_mm()
