#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 下午6:12

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class DBF(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(DBF, self).__init__(api_root_url, **kwargs)

    # 端午节活动
    def dbf_accept_zong_zi(self, invite_code):
        self.req_method = 'POST'
        self.req_url = '/dragonBoatFestival/acceptZongzi'
        self.req_body = {
            "inviteCode": invite_code
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 端午节活动
    def dbf_leader_board(self):
        self.req_method = 'GET'
        self.req_url = '/dragonBoatFestival/leaderboard'
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 修改活动时间
    def dbf_set_time(self, start_time, end_time):
        self.req_method = 'POST'
        self.req_url = '/dragonBoatFestival/setTime'
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        self.req_body = {
            "startTime": start_time,
            "endTime": end_time
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result


dbf = DBF(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    # dbf.dbf_set_time('1624204800000', '1625065200000')  # 21-30 未开始
    dbf.dbf_set_time('1622476800000', '1625065200000')  # 1-30  进行中
    # dbf.dbf_set_time('1622476800000', '1622646000000')  # 1-2   已结束
