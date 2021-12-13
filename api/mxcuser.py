#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 上午11:02

from base.base_request import BaseRequest
from faker_util import fakerist
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class MxcUser(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(MxcUser, self).__init__(root_url, **kwargs)

    # 新增leads
    # 要先调用 api-sit.miaocode.com/api/mxcaccount/account/logout接口
    # 获取响应头中的 Set-Cookie: SESSION=O
    def add_visit_leads(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/leads/visit/addVisitLeads'
        self.req_body = kwargs
        self.req_headers = {
            'mxc-token': auth_util.get_token('mxc', 'mxc-token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result


mxc_user = MxcUser(common_util.env('DOMAIN_GZ') + '/mxcuser')

if __name__ == '__main__':
    kwargs = data_pool.supply('mxcuser_data.yml', 'add_visit_leads')[0]
    kwargs['childName'] = 'Asc' + fakerist.word()
    kwargs['phone'] = '18899708135'
    res1 = mxc_user.add_visit_leads(**kwargs)
    userid = res1.sdata.get('userId')  # 4003926
    childName = res1.sdata.get('childName')  # Asc以及
    assert res1.status is True
