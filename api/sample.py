# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common

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
'''


class Sample(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Sample, self).__init__(root_url, **kwargs)

    def req_get(self):
        self.req_method = 'GET'
        self.req_url = '/account/login'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    def req_post_with_json(self):
        self.req_method = 'POST'
        self.req_url = '/account/submit'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    def req_post_with_data(self):
        self.req_method = 'POST'
        self.req_url = '/account/submit'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result

    def req_post_with_files(self):
        self.req_method = 'POST'
        self.req_url = '/account/submit'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            "accountPassword": "262728293031",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            files=self.req_body
        )
        asserter.result_check(result)
        return result


sample = Sample(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    sample.req_post()
