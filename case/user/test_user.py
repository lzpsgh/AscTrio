#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:14

import pytest

from api.account import account
from api.user import user
from util.data_util import data_pool
from util.log_util import logger
from util.mysql_util import mysqler


class TestUser:

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize("phone", data_pool.supply('test_user.yml', 'test_reset_pwd'))
    def test_modify_users_owner(self, phone):
        account.crm_login()
        logger.info(phone)
        user_id = mysqler.query("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        res1 = user.reset_pwd(user_id)
        assert res1.status is True

    @pytest.mark.skip
    @pytest.mark.single
    def test_leads_exist(self, phone):
        res = user.phone_exist(phone)
        assert res.status is True
        assert res.sdata['isLeads'] is True

    @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize(
        "phone", data_pool.supply('test_user.yml', 'test_reset_pwd'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_reset_pwd(self, phone):
        userid = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        logger.info(f'userid是{userid}')
        res = user.reset_pwd(userid)
        assert res.status is True

    # @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize("phone", data_pool.supply('.yml', ''))
    @pytest.mark.parametrize("phone", ['18899022003'])
    @pytest.mark.usefixtures('crm_login_with_mm', 'h5_login')
    # 宝贝作品的登录接口
    def test_user_login(self, phone):
        # user.get_current_user_nocookie()
        userid = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
        logger.info(f'用户的phone是{phone}, userid是{userid}')
        user.reset_pwd(userid)
        res = user.login(phone)
        # 设置该用户的wxparentid为'o-12n0z07Zc6aLI9sAYouWkAojmA'
        assert res.status is True
        assert res.sdata.get('userId') == userid


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_user.py::TestUser"])
