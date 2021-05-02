# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common


class Other(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Other, self).__init__(api_root_url, **kwargs)

    # 给9.9元流量课用户 重新推送[新带新]链接
    def send_paysucmsg_fast(self, phone):
        self.req_method = 'GET'
        self.req_url = '/wxmsg/sendPaySucMsgFast'
        self.req_body = {
            "phone": phone
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result

    def add_sprite(self):
        self.req_method = 'POST'
        self.req_url = '/mate/addSprite'
        self.req_body = {
            'isCommon': False,
            'price': 8,
            'spriteName': '环保比赛-孩子9',
            'dataURL': 'https://res.miaocode.com/6ff0d74b-29e6-424f-8870-a08a6f58b995.png'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        common.result_check(result)
        return result

    def add_stage(self):
        self.req_method = 'POST'
        self.req_url = '/mate/addStage'
        self.req_body = {
            'isCommon': False,
            'comment': 'asdf',
            'price': 0,
            'stageName': '环保比赛-新几44',
            'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        common.result_check(result)
        return result


other = Other(envar.BASE_URL_CORE)

if __name__ == '__main__':
    # other.send_paysucmsg_fast("18899758128")
    other.add_sprite()
