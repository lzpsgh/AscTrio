# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util

'''
用前须知：

1. 关于 x_request
只有使用param参数的get请求和使用json参数的post请求能使用这个 x_request 函数,
如果对应get请求，其等价于下面用法
result = self.request(
    method=self.req_method, url=self.req_url,headers=self.req_headers,cookies=self.req_cookies
    params=self.req_body)
如果对应post请求，其等价于下面用法
result = self.request(
    method=self.req_method, url=self.req_url,headers=self.req_headers,cookies=self.req_cookies
    json=self.req_body)
详情请查阅源码base/base_request.py

'''


class BasicInfoCompany(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(BasicInfoCompany, self).__init__(root_url, **kwargs)

    # 供应商列表查询
    def req_post_with_json(self):
        self.req_method = 'POST'
        self.req_url = '/basic/api/v1.0/vehTaxiCompany/joinListPaged/'
        self.req_body = {
            "pageSize"         : 10,
            "pageIndex"        : 1,
            "companyName"      : '测试',
            "supplierLabelCode": "1",
            "cityId"           : 147,
        }
        self.req_cookies = {
            'token': auth_util.get_token('zgj', 'token')
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    '''post请求 如果传urlencoded 只能用request()'''

    def req_post_with_data(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/account/submit'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_token('crm', 'jsessionid'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        auth_util.set_token('bbc', 'exam_token', result.rsp.cookies["exam_token"])
        assert_util.result_check(result)
        return result

    '''get请求 直接用x_request()
       将多个参数合并成字段
    '''

    def req_get(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/account/login'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_token('crm', 'jsessionid')
        }
        result = self.x_request()
        # assert_util.result_check(result)
        return result


basic_info_company = BasicInfoCompany(common_util.env('DOMAIN_ASSET'))

if __name__ == '__main__':
    # kwa = data_pool.supply('sample_data.yml', 'test_reset_pwd')[0]  # 此时kwargs是dict类型
    basic_info_company.req_post_with_json()  # 通过**操作符将kwargs解包成 n个入参
    # pass
