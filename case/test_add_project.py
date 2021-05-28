#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 下午10:25

import pytest
from util.logger import logger
from api.user.user import user
from api.diy_center.user import gzuser
from api.diy_center.project import project
from util.mysql_operate import db


class TestLeadsAddProject:

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_add_user_add_project(self):

        phone = '18844550007'
        project_name_1 = 'zuopin7'

        user.send_sms2(phone)
        user.register(phone)
        gzuser.login(phone)

        res4 = project.save_scratch_project_for_user(project_name_1)
        project_id_1 = res4.sdata.get('id')
        res5 = project.publish(project_name_1, project_id_1)
        assert res5.sdata.get('status') == 'P'

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_user_add_project(self):

        phone = '18844550007'
        project_name_1 = 'zuopin8'

        gzuser.login(phone)
        res4 = project.save_scratch_project_for_user(project_name_1)
        project_id_1 = res4.sdata.get('id')
        res5 = project.publish(project_name_1, project_id_1)
        assert res5.sdata.get('status') == 'P'


if __name__ == '__main__':
    # pytest.main(["-q", "-s", "test_add_project.py::TestLeadsAddProject::test_user_add_project"])
    phone = '13006166591'
    user_id = db.select_db("SELECT id FROM user WHERE phone=\'"+phone+"\'")[0][0]
    print(user_id)
