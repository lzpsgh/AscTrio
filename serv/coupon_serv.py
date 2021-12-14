#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
from api.coupon import coupon
from log_util import logger
from util.data_util import data_pool


# 创建优惠券批次: 现金直减券+新签用户
def create_coupon_cash_new():
    # 运营推给CC
    kwargs = data_pool.supply('coupon_data.yml', 'create_coupon')[0]
    kwargs['title'] = '减免金额8'
    kwargs['subamount'] = '8'
    kwargs['sendType'] = '1'  # 1新签 2续费
    res1 = coupon.create_coupon(**kwargs)
    couponId = logger.log(res1.sdata.get('id'))  # 返回优惠券批次id 即yml里的 couponId=4393
    assert res1.status is True


if __name__ == '__main__':
    create_coupon_cash_new()
