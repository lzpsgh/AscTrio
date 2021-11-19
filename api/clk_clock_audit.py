# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool

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


class ClkClockAudit(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(ClkClockAudit, self).__init__(root_url, **kwargs)

    # 上传打卡
    def upload_clock(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/api/clk-clock-audit/audit'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('web', 'gz_token'),  # api_token_1553151F52226FFBF1AF1343FBD8F4E5
            # 'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        # auth_util.set_token('bbc', 'exam_token', result.rsp.cookies["exam_token"])
        assert_util.result_check(result)
        return result

    # 审核通过
    def audit(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/mxc/clk-clock-audit/enabled/audit'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('web', 'gz_token'),  # api_token_1553151F52226FFBF1AF1343FBD8F4E5
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 打卡记录查询
    # phone=13391730115&pageNum=1&pageSize=20
    # data/list/auditStatus=0
    def query_audit(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/mxc/clk-clock-audit/audits'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('web', 'gz_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 撤回审核操作
    # id=1658&retrievedReason=2
    # data为null
    def retrieve_audit(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/mxc/clk-clock-audit/retrieve'
        self.req_body = kwargs
        self.req_cookies = {
            'token': auth_util.get_token('web', 'gz_token'),  # api_token_1553151F52226FFBF1AF1343FBD8F4E5
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result


clk_clock_audit = ClkClockAudit(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    kwargs = data_pool.supply('xxx.yml', 'upload_info')  # 此时kwargs是dict类型
    clk_clock_audit.req_get(**kwargs)  # 通过**操作符将kwargs解包成 n个入参
