#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 下午2:48

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class Channel(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Channel, self).__init__(root_url, **kwargs)

    def add_channel(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/channel/addChannel'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result


channel = Channel(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    pass
    # kwargs = data_pool.supply('channel.yml', 'add_channel')[0]
    # fake = "Asc"+fakerist.month_name()
    # kwargs['name'] = fake
    # kwargs['code'] = fake
    # res1 = channel.add_channel(**kwargs)
    # assert res1.status is True
