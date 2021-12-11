#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 下午3:43

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class MxcAccount(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(MxcAccount, self).__init__(root_url, **kwargs)

    def login(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/mxcaccount/account/login'
        self.req_body = {
            'accountName': 'fp001@test.com',
            'accountPassword': '262728293031',
            'captcha': '7d5c'
        }
        self.req_headers = {
            'mxc-token': None
        }
        self.req_cookies = {
            'SESSION': auth_util.get_token('mxc', 'SESSION'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        auth_util.set_token('mxc', 'mxc-token', result.rsp.headers['mxc-token'])
        return result

    # 未调试完
    # def logout(self, **kwargs):
    #     self.req_method = 'POST'
    #     self.req_url = '/mxcaccount/account/logout'
    #     self.req_body = kwargs
    #     self.req_headers = {
    #         "mxc-token": "c065eafd-ecd5-415f-b506-ab05d1fe6369"
    #     }
    #     self.req_cookies = {
    #         'SESSION': "YmU2NjYyZjctZjUwNy00NGYwLTg3ZTUtODUzMDhjMzA5YWQw",
    #         # 'exam_token': auth_util.get_token('bbc', 'exam_token'),
    #     }
    #     result = self.request(
    #         method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
    #         json=self.req_body
    #     )
    #     assert_util.result_check(result)
    #     # auth_util.set_token('mxc', 'SESSION', result.rsp.cookies["token"]),
    #     logger.info(result.rsp.headers)
    #     auth_util.set_token('mxc', 'SESSION', result.rsp.headers['Set-Cookie']['SESSION'])
    #     logger.info(result.rsp.headers['Set-Cookie']['SESSION'])
    #     return result


mxc_account = MxcAccount(common_util.env('DOMAIN_GZ'))

if __name__ == '__main__':
    # kwargs = data_pool.supply('channel.yml', 'add_channel')[0]
    # kwargs['name'] = fakerist.word()
    res1 = mxc_account.login()
    assert res1.status is True
