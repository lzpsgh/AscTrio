# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午10:14
import pytest

from service.account.account import account
from util.logger import logger


class TestAccount:

    @pytest.mark.single
    @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_pay_callback_wx(self):
        logger.info("\n*************** 开始执行用例 ***************")

        result = account.crm_login()
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg

        logger.info("\n*************** 结束执行用例 ***************")


if __name__ == '__main__':
    # pytest.main(["-q", "-s", "pay_callback_wx.py"])
    # data.load_yaml("data/cookies.yml")
    pass
