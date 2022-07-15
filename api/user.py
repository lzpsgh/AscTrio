# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 官网登录-密码登录
    def login(self):
        self.req_method = 'POST'
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
    def logout(self):
        self.req_method = 'POST'
        self.req_url = '/user-center/api/v1.0/accountSign/out'
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        auth_util.set_cookie('web', result.rsp.cookies["JSESSIONID"])
        return result


user = User(common_util.env('DOMAIN_USER'))

if __name__ == '__main__':
    phone = '9758137'
    user.login()
