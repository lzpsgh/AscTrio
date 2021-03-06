# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行
import assert_util
import auth_util
from base.base_request import BaseRequest
from util import common_util


class Other(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Other, self).__init__(api_root_url, **kwargs)

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

    def add_project(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/location/api/v1.0/assetProjectManage/'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


other = Other(common_util.env('DOMAIN_ASSET'))

if __name__ == '__main__':
    pass
