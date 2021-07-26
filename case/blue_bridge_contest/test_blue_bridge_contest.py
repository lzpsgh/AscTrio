#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from api.blue_bridge_contest_signup import bbc_signUp
from api.goods_order import goods_order
from api.user import user
from util.data_kit import data_pool
from util.log_kit import logger
from util.mysql_kit import mysqler


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestBlueBridgeContest:

    # @allure.story("用例--注册/登录/查看--预期成功")
    # @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_bbc_signup.yml', 'save_match_1'))
    def test_save_match_enable(self, kwargs):
        res = bbc_signUp.save_match(**kwargs)
        assert res.status is True
        match_id = mysqler.query("SELECT id FROM bbc_match ORDER BY create_time DESC LIMIT 1")[0][0]
        logger.info(f"创建的蓝桥杯赛事活动ID是{match_id}")
        res1 = bbc_signUp.enable(1, match_id)
        assert res1.status is True

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_bbc_signup.yml', 'submit_registration_information_senior'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_registration_information(self, kwargs):
        phone = kwargs['phone']
        userid = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        user.reset_pwd(userid)
        user.login(phone)
        res = bbc_signUp.submit_registration_information(**kwargs)
        assert res.status is True
        signin_id = res.sdata.get('id')
        logger.info(f"报名ID是{signin_id}")
        # 将用户的openid设置为iphone12mini上的
        mysqler.execute(
            f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = \'{signin_id}\' ")

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_bbc_signup.yml', 'submit_registration_information_senior'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_pay_audit(self, kwargs):
        phone = kwargs['phone']
        userid = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        user.reset_pwd(userid)
        user.login(phone)
        res = bbc_signUp.submit_registration_information(**kwargs)
        assert res.status is True
        signin_id = res.sdata.get('id')
        logger.info(f"报名ID是{signin_id}")
        # 将用户的openid设置为iphone12mini上的
        # mysqler.query(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = \'{signin_id}\' ")

        # 创建订单获取 payrecordId
        kwargs2 = data_pool.supply('data_bbc_signup.yml', 'create_order_ali')[0]
        kwargs2['id'] = int(signin_id)
        kwargs2['userId'] = userid
        res2 = bbc_signUp.create_order(**kwargs2)
        pay_record_id = res2.sdata.get("payrecordId")

        if pay_record_id is None:
            raise Exception("aaaa")

        # 模拟支付回调
        # mysqler.execute(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = 58 ")
        SQL_ORDERNO_OUTTRADENO = f"SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE pr.id = '{pay_record_id}'; "
        out_trade_no = mysqler.query(SQL_ORDERNO_OUTTRADENO)[0][0]
        goods_order.pay_callback_suc(out_trade_no)

        # 审核通过
        kwargs3 = data_pool.supply('data_bbc_signup.yml', 'audit_pass')[0]
        kwargs3['enable'] = 1
        kwargs3['id'] = signin_id
        res4 = bbc_signUp.audit(**kwargs3)
        assert res4.status is True

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_bbc_signup.yml', 'audit_fail'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_audit_fail(self, kwargs):
        res = bbc_signUp.audit(**kwargs)
        assert res.status is True

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_bbc_signup.yml', 'audit_pass'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_audit_pass(self, kwargs):
        res = bbc_signUp.audit(**kwargs)
        assert res.status is True


if __name__ == '__main__':
    pass
    # bbc_signUp.test_submit_pay_audit()
    # pytest.main(["-q", "-s", "test_blue_bridge_contest.py::TestBlueBridgeContest"])
