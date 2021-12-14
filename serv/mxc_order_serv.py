#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
from api.mxcorder import mxc_order
from util.data_util import data_pool


# 3运营推送优惠券给B端角色
def send_coupon_to_user(user_id, coupon_id):
    kwargs = data_pool.supply('mxcorder_data.yml', 'send_coupon_to_user')[0]
    kwargs['userId'] = user_id  # 18899708134
    kwargs['couponId'] = coupon_id
    res = mxc_order.send_coupon_to_user(**kwargs)
    assert res.status is True


# 5从订单详情获取订单ID
def order_detail(user_id, goods_id):
    kwargs1 = data_pool.supply('mxcorder_data.yml', 'order_detail')[0]
    kwargs1['userId'] = user_id  # 18899708134
    kwargs1['goodsId'] = goods_id
    res1 = mxc_order.order_detail(**kwargs1)
    order_id = res1.sdata.get('id')  # 订单ID
    assert res1.status is True


if __name__ == '__main__':
    send_coupon_to_user('4003926', '4393')
    order_detail('4003926', '765')
