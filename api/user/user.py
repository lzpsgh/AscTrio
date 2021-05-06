# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common
from util.logger import logger
from util.mysql_operate import db

sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 官网注册
    def register(self, datajson):
        self.req_method = 'POST'
        self.req_url = '/user/register'
        # self.req_body = {
        #     "phone": "18899112667",
        #     "code": "123456",
        #     "userGrade": '小学四年级',
        # }
        self.req_body = datajson
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth.set_cookie('web', core_jsessionid)
        logger.info(core_jsessionid)
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
        asserter.result_check(result)
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
        asserter.result_check(result)
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
        asserter.result_check(result)
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
        asserter.result_check(result)
        return result

    # 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）对国内国外支持更好也支持国家码
    def send_sms2(self, phone):
        self.req_method = 'GET'
        self.req_url = '/ccbb/sendSMS2'
        self.req_body = {
            "phone": phone,
            'countryCode': '86',
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 判断手机号是否存在（落地页和）
    def phone_exist(self, phone):
        # application/x-www-form-urlencoded
        self.req_method = 'POST'
        self.req_url = '/goodsOrder/phoneExist'
        self.req_body = {
            "phone": phone,
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body
        )
        asserter.result_check(result)
        assert result.sdata['isLeads'] is False
        assert result.sdata['isUser'] is False
        return result

    # 修改用户所属cc
    def modify_users_owner(self, phone):
        sql_query_userid = "select id from activityuser where phone = "
        # phone = '13333333333'
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
        asserter.result_check(result)
        return result


user = User(common.env('BASE_URL_CORE'))

if __name__ == '__main__':

    mphone = '18888655443'
    # user.send_sms2(mphone)
    # user.phone_exist(mphone)

    # data = {
    #     'phone': "18877771650",
    #     'code': "123456",
    #     'userGrade': '小学三年级',
    # }
    # user.register(data)
