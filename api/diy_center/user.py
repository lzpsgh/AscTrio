# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from util import asserter
from util import common
from util import auth


class GZUser(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GZUser, self).__init__(api_root_url, **kwargs)

    # 发送短信
    def send_sms(self, param1):
        self.req_method = 'GET'
        self.req_url = '/gzuser/sms/sendSMS'
        self.req_body = {
            "phone": param1
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 注册
    def register(self, param1):
        self.req_method = 'POST'
        self.req_url = '/gzuser/user/register'
        self.req_body = {
            "phone": param1,
            "userPassword": "262728293031",
            "code": '123456'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryJ8fdxxspLpykHU8t'
        }
        # self.req_cookies = {
        #     'JSESSIONID': auth.set_cookie('web'),
        # }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 登录
    def login(self, param1):
        self.req_method = 'GET'
        self.req_url = '/gzuser/user/login'
        self.req_body = {
            "phone": param1,
            'userPassword': '262728293031'   # common.calc_pwd(param1)
        }
        # result = self.x_request()
        result = self.request(
                method=self.req_method, url=self.req_url,
                params=self.req_body
            )
        token = result.rsp.cookies['token']
        auth.set_cookie('gz', token)
        asserter.result_check(result)
        return result


gzuser = GZUser(common.env('BASE_URL_GZ'))

if __name__ == '__main__':

    phone = '18844550004'
    res3 = gzuser.login(phone)
    assert res3.status is True

    # assert res3.rsp.status_code == 200
