# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class Other(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Other, self).__init__(api_root_url, **kwargs)

    # 给9.9元流量课用户 重新推送[新带新]链接
    def send_paysucmsg_fast(self, **kwargs):
        return self.request("GET", f"/wxmsg/sendPaySucMsgFast", **kwargs)

    def add_sprite(self, **kwargs):
        return self.request("POST", "/mate/addSprite", **kwargs)

    def add_stage(self, **kwargs):
        return self.request("POST", "/mate/addStage", **kwargs)

other = Other(api_root_url)
