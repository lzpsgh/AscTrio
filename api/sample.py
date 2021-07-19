# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit
from util.data_kit import data_pool

'''
用前须知：
1. 关于 req_body
不管是get请求的param参数，还是post请求的json和data参数，还是别的请求的别的参数，统一放进req_body

2. 关于 x_request
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

3. 在req_get和req_post_with_data 方法中 ,形参kwargs收到传入的n个字段，
然后通过操作符再重新打包回dict类型，即可赋值给req_body

'''


class Sample(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Sample, self).__init__(root_url, **kwargs)

    def req_get(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/account/login'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    def req_post_with_json(self, account_name):
        self.req_method = 'POST'
        self.req_url = '/core/account/submit'
        self.req_body = {
            "accountName": account_name,
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    def req_post_with_data(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/account/submit'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_kit.result_check(result)
        return result

    def req_post_with_files(self):
        self.req_method = 'POST'
        self.req_url = '/core/account/submit'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            files=self.req_body
        )
        assert_kit.result_check(result)
        return result


sample = Sample(common_kit.env('BASE_URL'))

if __name__ == '__main__':
    kwargs = data_pool.supply('xxx.yml', 'upload_info')  # 此时kwargs是dict类型
    sample.req_get(**kwargs)  # 通过**操作符将kwargs解包成 n个入参
