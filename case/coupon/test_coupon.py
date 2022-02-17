#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 上午11:18


import pytest

from api.coupon import coupon
from util.data_util import data_pool
from util.faker_util import fakerist
from util.log_util import logger


class TestCoupon:

    # @pytest.mark.skip
    # @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('coupon_data.yml', 'create_coupon_school'))
    def test_add_coupon_schook(self, kwargs):
        # 下发渠道分别是1，2，3
        # 金额分别是直减1011，1012，1013
        meet_amount = kwargs['meetamount']
        sub_amount = kwargs['subamount']
        kwargs['type'] = 'CASH_COUPON'  # 现金
        kwargs['couponTypeId'] = 53  # 校区直减券_不可叠加
        kwargs['couponAmount'] = 1  # 限量1张
        kwargs['sendType'] = 1
        kwargs['title'] = f'限量2校区-{meet_amount}-{sub_amount}-{fakerist.word()}'
        res1 = coupon.create_coupon(**kwargs)
        couponId = res1.sdata.get('id')
        logger.info(f'第一张的id是{couponId}')
        assert res1.status is True


if __name__ == '__main__':
    pass
