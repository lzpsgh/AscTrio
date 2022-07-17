#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 17:47
from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class StationApply(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(StationApply, self).__init__(root_url, **kwargs)

    # 新建建站申请
    def add_station_apply(self, kwargs):
        self.req_method = 'POST'
        self.req_url = '/station/api/v1.0/locationConstruction/addLocationConstruction'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 撤回建站申请
    def withdraw_station_apply(self, xid):
        self.req_method = 'POST'
        self.req_url = '/station/api/v1.0/locationConstruction/withdraw'
        self.req_body = {
            "id": xid
        }
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


station_apply = StationApply(common_util.env('DOMAIN_ASSET'))

if __name__ == '__main__':
    pass
    # kwargs = data_pool.supply('channel.yml', 'add_channel')[0]
    # kwargs['name'] = fakerist.word()
    # res1 = station_apply.add_station_apply(**kwargs)
    # assert res1.status is True
