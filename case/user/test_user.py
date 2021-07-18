#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:14

import pytest

from api.account import account
from api.user import user
from case.conftest import user_data
from util.log_kit import logger
from util.mysql_kit import mysqler


class TestUser:

    # todo 增加日志格式可读性
    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_reset_pwd(self, phone):
        account.crm_login()
        logger.info(phone)
        user_id = mysqler.select_db("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_modify_users_owner(self, phone):
        account.crm_login()
        logger.info(phone)
        user_id = mysqler.select_db("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_leads_exist(self, phone):
        res = user.phone_exist(phone)
        assert res.status is True
        assert res.sdata['isLeads'] is True

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize("phone", ['18502937862'])
    @pytest.mark.usefixtures("crm_login_with_mm")
    # @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    def test_reset_pwd(self, phone):
        userid = mysqler.select_db(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        logger.info(f'userid是{userid}')
        res = user.reset_pwd(userid)
        assert res.status is True

    @pytest.mark.skip
    # @pytest.mark.parametrize("phone", user_data["test_reset_pwd"])
    @pytest.mark.parametrize("phone", ['18502937862'])
    # 宝贝作品的登录接口
    def test_user_login(self, phone):
        # TODO 加异常判断
        user.get_current_user_nocookie()
        userid = mysqler.select_db(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        logger.info(f'用户的phone是{phone}, userid是{userid}')
        # user.reset_pwd(userid)
        res = user.login(phone)
        # 设置该用户的wxparentid为'o-12n0z07Zc6aLI9sAYouWkAojmA'
        assert res.status is True
        assert res.sdata.get('userId') == userid


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_user.py::TestUser"])
