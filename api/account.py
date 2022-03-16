# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.log_util import logger


class Account(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Account, self).__init__(root_url, **kwargs)

    def crm_login(self):
        self.req_method = 'get'
        self.req_url = '/core/account/login'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "589678262728104112",  # 对应的明文是'Qwe123!@#'   589678262728104112
            "captcha": 'qwe123EWQ#@!'  # '262728293031'
        }
        result = self.x_request()
        assert_util.result_check(result)

        # 保存jsessionid，在core项目中用到
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth_util.set_cookie('crm', core_jsessionid)

        # 保存api_account_token，在蓝桥杯项目中用到
        api_account_token = result.rsp.cookies["api_account_token"]
        auth_util.set_gz_token('crm', api_account_token)
        logger.info(api_account_token)

        return result

    def crm_login_with(self, account_name):
        self.req_method = 'get'
        self.req_url = '/core/account/login'
        self.req_body = {
            "accountName": account_name,
            "accountPassword": "589678262728104112",
            "captcha": 'qwe123EWQ#@!'
        }
        result = self.x_request()
        assert_util.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        api_account_token = result.rsp.cookies["api_account_token"]
        # auth_util.set_cookie('crm', core_jsessionid)
        auth_util.set_token('crm', 'jsessionid', core_jsessionid)
        auth_util.set_token('crm', 'api_account_token', api_account_token)

        logger.debug(core_jsessionid)
        return result


account = Account(common_util.env('DOMAIN_CORE'))
# account2 = Account(common_util.env("DOMAIN_MOCK") + '/' + common_util.env("YAPI_PROJ_CORE"))

if __name__ == '__main__':
    account.crm_login()
    # account2.crm_login()
