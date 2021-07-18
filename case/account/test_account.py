#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:11

import pytest

from api.account import account


class TestAccount:
    # @pytest.mark.skip
    # @pytest.mark.single
    kwargs = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "589678262728104112",  # 对应的明文是'Qwe123!@#'   589678262728104112
        "captcha": 'qwe123EWQ#@!'  # '262728293031'
    }

    def test_crm_login(self):
        result = account.crm_login()
        assert result.rsp.status_code == 200

    @pytest.mark.skip
    # cc倪旭
    def test_crm_login_with_cc(self):
        result = account.crm_login_with("ccxu.ni01@miaocode.com")
        assert result.rsp.status_code == 200

    @pytest.mark.skip
    # cc胡俊
    def test_crm_login_with_cc2(self):
        result = account.crm_login_with("ccjun.hu01@miaocode.com")
        assert result.rsp.status_code == 200

    @pytest.mark.skip
    # 赠品审核员
    def test_crm_login_with_giftaudit(self):
        result = account.crm_login_with("jingjing.hu@miaocode.com")
        assert result.rsp.status_code == 200

    @pytest.mark.skip
    # 教务老师
    def test_crm_login_with_teacher(self):
        result = account.crm_login_with("aa@miaocode.com")
        assert result.rsp.status_code == 200


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_account.py"])
