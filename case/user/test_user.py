#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:14

import pytest

from api.common.account import account
from api.common.user import user
from case.conftest import user_data
from util.logger import logger
from util.mysql_operate import db


class TestUser:

    # todo 增加日志格式可读性
    @pytest.mark.skip
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

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_leads_exist(self, phone):
        res = user.phone_exist(phone)
        assert res.status is True
        assert res.sdata['isLeads'] is True

    @pytest.mark.single
    @pytest.mark.parametrize("phone", ['19123457283'])
    def test_reset_pwd(self, phone):
        # phone = 19123457283
        userid = db.select_db(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        logger.info(f'userid是{userid}')
        res = user.reset_pwd(userid)
        assert res.status is True


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_user.py::TestUser::test_reset_pwd"])
