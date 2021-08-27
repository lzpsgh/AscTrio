#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 下午9:14

import pytest

from api.user import user
from util import sql_util
from util.data_util import data_pool
from util.log_util import logger
from util.mysql_util import mysqler


class TestUser:

    # @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize("phone", ['18999000002'])
    def test_add_leads(self, phone):
        res = user.phone_exist(phone)
        if res.sdata.get('isLeads') is False and res.sdata.get('isUser') is False:
            res1 = user.login_and_register(phone)
            assert res1.status is True

    # @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("phone", ['13612345677'])
    def test_modify_users_owner(self, phone):
        # account.crm_login()
        # logger.info(phone)
        res1 = user.modify_users_owner(phone)
        # user_id = mysqler.query("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
        # res1 = user.reset_pwd(user_id)
        assert res1.status is True

    @pytest.mark.skip
    @pytest.mark.single
    def test_leads_exist(self, phone):
        res = user.phone_exist(phone)
        assert res.status is True
        assert res.sdata['isLeads'] is True

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize("phone", data_pool.supply('user_data.yml', 'test_reset_pwd'))
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

    @pytest.mark.usefixtures('crm_login_with_mm')
    @pytest.mark.parametrize('kwargs', data_pool.supply(
        'user_data.yml', 'reset_pwd'
    ))
    def test_batch_reset_pwd(self, kwargs):
        userid = sql_util.sql_phone_to_userid(kwargs['phone'])
        res = user.reset_pwd(userid)
        # assert res.status is None

    @pytest.mark.usefixtures('h5_login')
    @pytest.mark.parametrize('kwargs', ['13612345677'])
    def test_get_current_user(self, kwargs):
        user.get_current_user()
        res = user.get_current_user()
        assert res.status is True


if __name__ == '__main__':
    pass
    # pytest.main(["-q", "-s", "test_user.py::TestUser"])
