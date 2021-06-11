#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:11

import pytest

from api.common.account import account


class TestAccount:

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_crm_login_with_mm(self):
        # logger.info("\n*************** 开始执行用例 ***************")
        result = account.crm_login_with_mm()
        assert result.rsp.status_code == 200
        # logger.info("\n*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_account.py"])
