# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 官网注册
    def register(self, **kwargs):
        return self.request("POST", '/user/register', **kwargs)

    # 官网登录
    def login(self, **kwargs):
        return self.request("GET", '/user/login', **kwargs)

    # 落地页注册登录
    def login_and_register(self, **kwargs):
        return self.request("GET", '/user/loginAndRegister', **kwargs)

    # 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）
    def send_sms(self, **kwargs):
        return self.request("GET", '/ccbb/sendSMS', **kwargs)


user = User(api_root_url)
