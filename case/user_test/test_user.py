#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:14

import pytest
from util.logger import logger
from api.account.account import account
from api.user.user import user
from util.mysql_operate import db
from case.conftest import user_data


class TestUser:

    # todo 增加日志格式可读性

    @pytest.mark.single
    @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_reset_pwd(self, phone):
        account.crm_login_with_mm()
        logger.info(phone)
        user_id = db.select_db("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_modify_users_owner(self, phone):
        account.crm_login_with_mm()
        logger.info(phone)
        user_id = db.select_db("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_user.py"])
