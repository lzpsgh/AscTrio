# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


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

    # 官网退出登录
    def crm_logout(self):
        self.req_method = 'POST'
        self.req_url = '/user-center/api/v1.0/accountSign/out'
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        auth_util.set_token('zgj', 'token', result.sdata)
        return result

account = Account(common_util.env('DOMAIN_USER'))

if __name__ == '__main__':
    account.crm_login()
    # account2.crm_login()
