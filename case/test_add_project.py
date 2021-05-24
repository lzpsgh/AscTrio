#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 下午10:25

import pytest
from util.logger import logger
from api.user.user import user
from api.diy_center.user import gzuser
from api.diy_center.project import project


class TestLeadsAddProject:

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_add_user_add_project(self):

        phone = '18844550007'
        project_name_1 = 'zuopin7'

        res1 = user.send_sms2(phone)
        assert res1.rsp.status_code == 200
        res2 = user.register(phone)
        assert res2.rsp.status_code == 200
        res3 = gzuser.login(phone)
        assert res3.status is True

        res4 = project.save_scratch_project_for_user(project_name_1)
        assert res4.status is True
        project_id_1 = res4.sdata.get('id')
        res5 = project.publish(project_name_1, project_id_1)
        assert res5.sdata.get('status') == 'P'

    @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo", '202103251226456923966257')
    def test_user_add_project(self):

        phone = '18844550007'
        project_name_1 = 'zuopin8'

        res3 = gzuser.login(phone)
        assert res3.status is True
        res4 = project.save_scratch_project_for_user(project_name_1)
        assert res4.status is True
        project_id_1 = res4.sdata.get('id')
        res5 = project.publish(project_name_1, project_id_1)
        assert res5.sdata.get('status') == 'P'


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_add_project.py::TestLeadsAddProject::test_user_add_project"])
