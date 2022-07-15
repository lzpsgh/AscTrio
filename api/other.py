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
    kwargs = {
        "networkPlanningLocationCode": "asc07040002",
        "locationName"               : "asc07040002",
        "cityName"                   : "广州市",
        "cityCode"                   : "440100",
        "areaName"                   : "天河区",
        "orgName"                    : "北京怀兴旺出租汽车有限公司",
        "orgId"                      : "1",
        "provinceName"               : "广东省",
        "address"                    : "侨鑫国际(南门)",
        "longitude"                  : 113.32205,
        "latitude"                   : 23.123275,
        "attribute"                  : "直营",
        "attributeCode"              : "1",
        "flag"                       : 0
    }
    other.add_location(kwargs)

    kwargs1 = {
        "stationType"                  : "Q",
        "projectName"                  : "新建站SDTQF",
        "locationId"                   : 119,
        "type"                         : "1",
        "civilBiddingEstimatedCost"    : "2",
        "highVoltageBuildEstimatedCost": "1",
        "lowVoltageBuildEstimatedCost" : "3",
        "plannedPowerCapacity"         : "4"
    }
    other.add_project(kwargs1)
