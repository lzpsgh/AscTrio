# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from config import envar
from core.base_request import BaseRequest

api_root_url = envar.BASE_URL_CORE


class Sample(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Sample, self).__init__(api_root_url, **kwargs)

    # get请求
    def req_get(self, **kwargs):
        return self.request("GET", f"/leadsApi/getTokennnn", **kwargs)

    # get请求 带参数
    def req_get_with_param(self, param1, **kwargs):
        return self.request("GET", f"/leadsApi/getTokenWith/{param1}", **kwargs)

    # post请求
    def req_post(self, **kwargs):
        return self.request("POST", f"/leadsApi/mypost", **kwargs)


sample = Sample(api_root_url)
