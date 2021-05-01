# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common
from util.logger import logger


class Account(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Account, self).__init__(root_url, **kwargs)

    def crm_login_with_mm(self):
        self.req_data = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
            "captcha": '1'
        }
        # self.req_cookies = {
        #     'JSESSIONID': auth.get_cookie('crm'),
        # }
        result = self.request("GET",
                              "/account/login",
                              params=self.req_data,
                              headers=self.req_headers,
                              cookies=self.req_cookies)
        common.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth.set_cookie('crm', core_jsessionid)
        logger.info(core_jsessionid)
        return result


account = Account(envar.BASE_URL_CORE)

if __name__ == '__main__':
    account.crm_login_with_mm()
