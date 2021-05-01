# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common
from util.logger import logger

api_root_url = envar.BASE_URL_CORE


class Account(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Account, self).__init__(root_url, **kwargs)

    def crm_login_with_mm(self):
        req_data = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
            "captcha": '1'
        }
        req_headers = {
            "Cache-Control": "no-cache",
        }
        req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request("GET",
                              "/account/login",
                              params=req_data,
                              headers=req_headers,
                              cookies=req_cookies)
        common.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth.set_cookie('crm', core_jsessionid)
        logger.info(core_jsessionid)
        return result


account = Account(api_root_url)

if __name__ == '__main__':
    account.crm_login_with_mm()
