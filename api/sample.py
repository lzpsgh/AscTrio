# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class Sample(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Sample, self).__init__(api_root_url, **kwargs)

    # get请求
    def req_get(self, **kwargs):
        return self.request("GET", "/leadsApi/getTokennnn", **kwargs)

    # post请求
    def req_post(self, **kwargs):
        return self.request("POST", "/leadsApi/mypost", **kwargs)


sample = Sample(api_root_url)
