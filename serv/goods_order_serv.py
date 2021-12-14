#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
import sql_util

from api.goods_order import goods_order
from util.data_util import data_pool


# 4创建校区工作台订单
def demolition_order(user_id, goods_id):
    kwargs0 = data_pool.supply('goods_order_data.yml', 'demolition_order_omo')[0]
    kwargs0['userId'] = user_id  # 用户的userid
    kwargs0['goodsIds'] = goods_id  # 2元的K2D
    kwargs0['orderSource'] = 'SCHOOL_ORDER'
    res0 = goods_order.demolition_order(**kwargs0)
    assert res0.status is True


# 6给订单绑定优惠券
def update_coupon(user_id, goods_id, order_id):
    # 查表获取usercoupon表的id
    couponIds = sql_util.sql_usercouponid(user_id, goods_id)

    # 更新订单:绑定优惠券
    kwargs = data_pool.supply('goods_order_data.yml', 'update_coupon')[0]
    kwargs['couponIds'] = couponIds
    kwargs['orderId'] = order_id
    kwargs['payStyle'] = 'NATIVE'
    kwargs['payType'] = 'WX'
    res1 = goods_order.update_coupon()
    assert res1.status is True


if __name__ == '__main__':
    demolition_order('155863', '765')
    update_coupon('4003926', '765', '51895')
