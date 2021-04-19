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
    def login(self, **kwargs):
        return self.request("GET", f'/user/login', **kwargs)

    # 落地页注册登录
    def login_and_register(self, **kwargs):
        return self.request("GET", f'/user/loginAndRegister', **kwargs)


user = User(api_root_url)
