#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 上午10:13

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit


class GroupBuy(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GroupBuy, self).__init__(api_root_url, **kwargs)

    def add_activity(self):
        self.req_method = 'POST'
        self.req_url = '/group_buy/add_activity'
        self.req_body = {
            'name': 'Asctrio新的拼团名称退费',
            'title': 'Asctrio新的拼团标题退费',
            'startTime': '2021-06-02 07:08:00',
            'endTime': '2021-06-29 16:48:00',
            'userCoupon': False,
            'channelCode': 'testtesttest',
            'goodsId': 668,
            'price': 1,
            'buyChanceNumber': 1,
            'activityType': 'GROUPPURCHASING',
            'seatNumber': 3,
            # 'validTime': 172799000  # 47h 59m 59s
            'validTime': 300000  # 20h-72000000-1200min  600000-10min
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_kit.result_check(result)
        return result


group_buy = GroupBuy(common_kit.env('BASE_URL_CORE'))

if __name__ == '__main__':
    group_buy.add_activity()
