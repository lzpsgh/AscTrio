#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 上午12:58

import pytest

from api.sample import sample
from util.data_util import data_pool
from util.log_util import logger


class TestSample:

    # @allure.story("故事：leadsapi获取token后提交入库")
    # @allure.description("该用例是针对 leadsapi获取token后提交入库 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("标题：leadsapi获取token后提交入库")
    # @pytest.mark.single
    # @pytest.mark.repeat(3)
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('leads_api_data.yml', 'upload_info'))
    def test_sample_get(self, kwargs):
        # case层可直接调用api层发起请求，请求前可自行修改kwargs任意键的值
        kwargs['token'] = 'res_token'
        result = sample.req_get(kwargs)
        prom = result.sdata.get('resultInquiryList')[0].get('promotionResult')
        logger.info('prom的值')
        assert prom == 4

        # case层也能直接调用serv层发起请求
        # kwargs3 = data_pool.supply('bbc_signup_data.yml', 'create_order')[0]
        # kwargs3['payType'] = "WX"
        # serv_sample.save_match_enable(kwargs3)
        # res3 = sample.request(kwargs3)
        # pay_record_id = res3.sdata.get("payrecordId")
        # out_trade_no = sql_util.sql_payrecordid_to_outtradeno(pay_record_id)
        # assert result.status is True
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        # logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # pytest.main(["-q", "-s", "-n", "auto", "test_blue_bridge_contest.py::TestBlueBridgeContest::test_result_inquiry"])
    pass
