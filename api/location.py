#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/15 17:31
from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class Location(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Location, self).__init__(root_url, **kwargs)

    def add_location(self, kwargs):
        self.req_method = 'POST'
        self.req_url = '/location/api/v1.0/location/add'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 新增立项
    def add_project(self, kwargs):
        self.req_method = 'POST'
        self.req_url = '/location/api/v1.0/assetProjectManage/'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 删除立项
    def rm_project(self, project_id):
        self.req_method = 'DELETE'
        self.req_url = '/location/api/v1.0/assetProjectManage/' + project_id
        # self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.request(method=self.req_method, url=self.req_url, cookie=self.req_cookies)
        assert_util.result_check(result)
        return result

location = Location(common_util.env('DOMAIN_ASSET'))

if __name__ == '__main__':
    kwargs = data_pool.supply('test_location.yml', 'add_location')[0]
    kwargs['networkPlanningLocationCode'] = "asc07160001"
    res1 = location.add_location(kwargs)
    assert res1.status is True
