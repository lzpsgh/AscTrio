# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午10:14
import pytest

from service.account.account import *
from util.logger import logger


class TestAccount:

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_crm_login_with_mm(self):
        logger.info("\n*************** 开始执行用例 ***************")

        result = crm_login_with_mm()

        assert result.rsp.status_code == 200
        # assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg

        logger.info("\n*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_account.py"])
