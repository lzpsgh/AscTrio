#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import pytest

from api.goods_order import goods_order
from util.data_kit import data_pool


class TestBlueBridgeContest:
    # @allure.story("用例--注册/登录/查看--预期成功")
    # @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("用户注册登录查看-预期成功")

    """官网-创建订单-微信支付
        购买k1课程 5280块
    """

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('goods_order_data.yml', 'demolition_order_k1'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_demolition_order_k1(self, kwargs):
        res = goods_order.demolition_order(**kwargs)
        assert res.status is True
        # signin_id = res.sdata.get('id')
        # logger.info(f"报名ID是{signin_id}")

    """官网-创建订单-微信支付
        购买s5课程 6000块
    """

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('goods_order_data.yml', 'demolition_order_s5'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_demolition_order_s5(self, kwargs):
        # kwargs['orderNo'] = pre_orderNo
        res = goods_order.demolition_order(**kwargs)
        assert res.status is True

    """微信支付页 购买k1课程 5280块
    """

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('goods_order_data.yml', 'get_pay_page_k1'))
    def test_get_pay_page_k1(self, kwargs):
        res = goods_order.getPayPage(**kwargs)
        assert res.status is True

    """微信支付页 购买s5课程 6000块
    """

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('goods_order_data.yml', 'get_pay_page_s5'))
    def test_get_pay_page_s5(self, kwargs):
        res = goods_order.getPayPage(**kwargs)
        assert res.status is True

    """微信支付模拟回调成功
        SQL_ORDERNO_OUTTRADENO = SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE go.orderNo = 'xxxx' AND pr.payStatus = 'WAITING';
    """

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('goods_order_data.yml', 'simulation_call_back'))
    def test_simulation_call_back(self, kwargs):
        # sql_orderno = "SELECT outTradeNo FROM payrecord WHERE payStatus = 'WAITING' AND payType = 'WX'"
        # sql_result = mysqler.query(sql_orderno)
        # logger.info(sql_result)
        # if sql_result == '' or sql_result is None:
        #     exit("sorry, goodbye!")
        #     # pass
        #
        # out_trade_no = sql_result[0][0]
        # logger.info("out_trade_no是 " + out_trade_no)
        #
        # result = goods_order.pay_callback_suc(out_trade_no)
        # # print(result.__dict__)
        # assert result.response.status_code == 200
        res = goods_order.getPayPage(**kwargs)
        assert res.status is True


if __name__ == '__main__':
    pytest.main(
        ["-q", "-s", "test_blue_bridge_contest.py::TestBlueBridgeContest"])
