# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class Account(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Account, self).__init__(api_root_url, **kwargs)

    # get请求
    def login(self, **kwargs):
        return self.request("GET", f"/account/login", **kwargs)


account = Account(api_root_url)
