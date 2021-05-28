#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 上午9:57

import pytest
from util.logger import logger
from api.account.account import account
from api.user.user import user
from util.mysql_operate import db


class TestUser:

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_reset_pwd(self, user_phone):
        account.crm_login_with_mm()
        # phone = '13006166591'
        user_id = db.select_db("SELECT id FROM user WHERE phone=\'" + user_phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_user.py::TestUser::test_reset_pwd"])
