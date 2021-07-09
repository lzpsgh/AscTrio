# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common
from util.mysql_operate import db

sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 新建预约试听课leads,官网
    def booking_demo(self, phone):
        self.req_method = 'POST'
        self.req_url = '/course/bookingDemo'
        self.req_body = {
            "isOnlyLeads": False,
            'phone': phone,
            'countryCode': 86,
            'smsCode': '123456',
            'childGrade': '五年级',
            'childName': 'name' + phone[-4:],
            'channel': 'official'
        }
        # self.req_body = datajson
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body
        )
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
            'countryCode': '86'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 微服务发送短信
    def gz_send_sms(self, param1):
        self.req_method = 'GET'
        self.req_url = '/gzuser/sms/sendSMS'
        self.req_body = {
            "phone": param1
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 落地页注册登录
    def login_and_register(self, phone):
        self.req_method = 'GET'
        self.req_url = '/user/loginAndRegister'
        self.req_body = {
            "phone": phone,
            "code": '123456',  # '262728293031'
            't': common.get_timestamp()
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        # result = self.x_request()
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            params=self.req_body
        )
        asserter.result_check(result)
        return result

    # 官网注册,要先获取验证码,用户密码默认后4位
    def register(self, param):
        self.req_method = 'POST'
        self.req_url = '/user/register'

        self.req_body = {
            'phone': param,
            'userPassword': '262728293031',
            'code': '123456',
            'regChannel': 'official',
            'channelKey': 'web',
            'platform': 'web',
            'origin': 'pc',
            'position': '001',
            'isOrg': 'false'
        }

        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        # core_jsessionid = result.rsp.cookies["JSESSIONID"]  # todo有时候不返回jsessionid
        # auth.set_cookie('web', core_jsessionid)
        # logger.info(core_jsessionid)
        return result

    # 微服务注册
    def gz_register(self, param1):
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

    # 官网登录
    def login(self, phone):
        self.req_method = 'GET'
        self.req_url = '/user/login'
        self.req_body = {
            "phone": phone,
            "userPassword": common.calc_pwd(phone),
            't': common.get_timestamp(),
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        auth.set_cookie('web', result.rsp.cookies["JSESSIONID"])
        return result

    # 官网退出登录
    def logout(self):
        self.req_method = 'GET'
        self.req_url = '/user/logout'
        self.req_body = {
            "t": common.get_timestamp()
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        auth.set_cookie('web', result.rsp.cookies["JSESSIONID"])
        return result

    # 官网登录
    def phone_login(self, phone):
        self.req_method = 'GET'
        self.req_url = '/user/phoneLogin'
        self.req_body = {
            "phone": phone,
            "code": 123456
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        auth.set_cookie('web', result.rsp.cookies["JSESSIONID"])
        return result

    # 微服务登录
    def gz_login(self, param1):
        self.req_method = 'GET'
        self.req_url = '/gzuser/user/login'
        self.req_body = {
            "phone": param1,
            'userPassword': '262728293031'  # common.calc_pwd(param1)
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

    # 重制用户密码
    # @pytest.mark.usefixtures("delete_register_user")
    def reset_pwd(self, user_id):
        self.req_method = 'POST'
        self.req_url = '/user/resetPWD'
        self.req_body = {
            'userId': user_id
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body, cookies=self.req_cookies
        )
        asserter.result_check(result)
        return result

    # 获取当前用户信息，用于获取官网web的cookie
    def get_current_user(self):
        self.req_method = 'GET'
        self.req_url = '/user/getCurrentUser'
        result = self.x_request()
        # asserter.result_check(result)
        if result.rsp.status_code == 200:
            # print(result.rsp.text)
            jsession_id = result.rsp.cookies['JSESSIONID']
            print(jsession_id)
            auth.set_cookie('crm', jsession_id)
        return result


user = User(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    phone = '15618698971'
    userid = '110311'

    # user.phone_exist(phone)
    user.reset_pwd(userid)

    # res1 = user.send_sms2(phone)
    # assert res1.rsp.status_code == 200
    # res2 = user.register(phone)
    # assert res2.rsp.status_code == 200

    # user.modify_users_owner()
    # account.crm_login_with_mm()
    # user.modify_users_owner(phone)

    # mphone = '18659107886'
    # user.send_sms2(mphone)
    # user.login(mphone)

    # user.send_sms2(mphone)
    # user.phone_exist(phone)

    # user.register(data)