#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
from api.coupon import coupon
from log_util import logger
from util.data_util import data_pool
from util.faker_util import fakerist


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


# 用于校区工作台3.1.5 创建优惠券批次: 直减券+续费用户,
def create_coupon_campus():
    kwargs = data_pool.supply('coupon_data.yml', 'create_coupon_school')[0]
    meet_amount = kwargs['meetamount']
    sub_amount = kwargs['subamount']
    kwargs['sendType'] = 2
    kwargs['title'] = f'续费校区-{meet_amount}-{sub_amount}-{fakerist.word()}'
    res1 = coupon.create_coupon(**kwargs)
    couponId = res1.sdata.get('id')
    logger.info(f'第一张的id是{couponId}')
    assert res1.status is True


if __name__ == '__main__':
    create_coupon_campus()
