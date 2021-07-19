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

    def add_activity(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/group_buy/add_activity'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_kit.result_check(result)
        return result


group_buy = GroupBuy(common_kit.env('BASE_URL'))

if __name__ == '__main__':
    group_buy.add_activity()
