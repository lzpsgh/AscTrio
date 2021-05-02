# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common
from util.mysql_operate import db

sql_query_userid = "select id from activityuser where phone = "
sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 官网注册
    def register(self):
        self.req_method = 'POST'
        self.req_url = '/user/register'
        self.req_body = {
            "phone": "18899112667",
            "code": "123456",
            "userGrade": '小学四年级',
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        return result

    # 官网登录
    def login(self, phone, user_password, t):
        self.req_method = 'GET'
        self.req_url = '/account/login'
        self.req_body = {
            "phone": phone,
            "userPassword": user_password,
            't': common.get_timestamp(),
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        return result

    # 官网登录
    def phone_login(self, phone):
        self.req_method = 'GET'
        self.req_url = '/user/phoneLogin'
        self.req_body = {
            "phone": phone,
            "code": 123456,
            't': common.get_timestamp(),
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        return result

    # 落地页注册登录
    def login_and_register(self, phone, user_password, t):
        self.req_method = 'GET'
        self.req_url = '/user/loginAndRegister'
        self.req_body = {
            "phone": phone,
            "userPassword": user_password,
            't': common.get_timestamp()
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        return result

    # 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）
    def send_sms(self):
        self.req_method = 'GET'
        self.req_url = '/ccbb/sendSMS'
        self.req_body = {
            "phone": "18899112648"
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        return result

    # 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）对国内国外支持更好也支持国家码
    def send_sms2(self):
        self.req_method = 'GET'
        self.req_url = '/ccbb/sendSMS2'
        self.req_body = {
            "phone": "18899112648",
            't': common.get_timestamp(),
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        return result

    # 修改用户所属cc
    def modify_users_owner(self):
        phone = '13333333333'
        self.req_method = 'GET'
        self.req_url = '/user/modifyUsersOwner'
        self.req_body = {
            'salerIds': '889',  # cc倪旭(新)  ccxu.ni01@miaocode.com
            'userIds': db.select_db(sql_query_userid + phone)
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()

        return result


user = User(envar.BASE_URL_CORE)

if __name__ == '__main__':
    user.phone_login()
