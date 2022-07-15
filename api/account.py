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
        self.req_method = 'post'
        self.req_url = '/user-center/api/v1.0/accountSign/in'
        self.req_body = {
            "userName": 'chenzhihao@aulton.com',
            "password": 'b217d9031a2e2f03475706094c17f71a',
        }
        result = self.x_request()
        assert_util.result_check(result)
        auth_util.set_token('zgj', 'token', result.sdata)
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


account = Account(common_util.env('DOMAIN_USER'))

if __name__ == '__main__':
    account.crm_login()
    # account2.crm_login()
