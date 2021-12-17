#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午11:31
import allure
import pytest

import coupon_serv
import goods_order_serv
import leads_serv
import mxc_order_serv
import sql_util


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestOmoSchool:

    # @pytest.mark.skip
    @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'h5_query444'))
    def test_all(self, kwargs):
        phone = '18899708136'
        # 新建leads
        leads_serv.add_omo_leads(phone)
        # 创建优惠券批次
        coupon_serv.create_coupon_cash_new()

        # 运营推送优惠券给B端角色
        userid = sql_util.sql_phone_to_userid(phone)
        mxc_order_serv.send_coupon_to_user(userid, "4393")

        # 创建校区工作台订单
        goods_order_serv.demolition_order()

        # 从订单详情获取订单ID
        mxc_order_serv.order_detail()

        # 给订单绑定优惠券
        goods_order_serv.update_coupon()

        # 支付回调-订金

        # 支付回调-尾款


if __name__ == '__main__':
    pass
