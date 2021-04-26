# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_GZ


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # 发送短信
    def send_sms(self, **kwargs):
        return self.request("GET", "/gzuser/sms/sendSMS", **kwargs)

    # 注册
    def register(self, **kwargs):
        return self.request("POST", "/gzuser/user/register", **kwargs)

    # 登录
    def login(self, **kwargs):
        return self.request("GET", "/gzuser/user/login", **kwargs)


user = User(api_root_url)
