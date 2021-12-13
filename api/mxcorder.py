#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/13 下午4:10

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class MxcOrder(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(MxcOrder, self).__init__(root_url, **kwargs)

    def send_coupon_to_user(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/coupon/sendCoupon2User'
        self.req_body = kwargs
        self.req_headers = {
            'mxc-token': auth_util.get_token('mxc', 'mxc-token'),
        }
        # self.req_cookies = {
        #     'JSESSIONID': auth_util.get_cookie('crm'),
        #     'exam_token': auth_util.get_token('bbc', 'exam_token'),
        # }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    def order_detail(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/order/orderDetail'
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


mxc_order = MxcOrder(common_util.env('DOMAIN_GZ') + '/mxcorder')

if __name__ == '__main__':
    kwargs = data_pool.supply('mxcorder_data.yml', 'send_coupon_to_user')[0]
    kwargs['userId'] = '4003926'  # 18899708134
    kwargs['couponId'] = '4393'
    res = mxc_order.send_coupon_to_user(**kwargs)
    assert res.status is True

    kwargs1 = data_pool.supply('mxcorder_data.yml', 'order_detail')[0]
    kwargs['userId'] = '4003926'  # 18899708134
    kwargs['goodsId'] = '765'
    res1 = mxc_order.order_detail(**kwargs)
    order_id = res1.sdata.get('id')  # 订单ID
    assert res1.status is True
