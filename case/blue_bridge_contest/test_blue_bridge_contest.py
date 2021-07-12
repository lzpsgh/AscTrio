#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from api.uoactivity.bbc_signup import bbc_signUp
from util.logger import logger
from util.mysql_operate import db
from util.read_data import datapool


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestBlueBridgeContest:

    # @allure.story("用例--注册/登录/查看--预期成功")
    # @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("用户注册登录查看-预期成功")

    # 数据驱动参考模版 template-ddt
    # @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.parametrize(
        "req_json", datapool.supply(
            'test_bbc_signup.yml', 'save_match'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_save_match_enable(self, req_json):
        bbc_signUp.save_match(req_json.get('name'),
                              req_json.get('expense'),
                              req_json.get('startTime'),
                              req_json.get('endTime'),
                              req_json.get('type'),
                              req_json.get('headImg'),
                              req_json.get('detailImgList'))
        # TODO 优化接口调用的字段重复
        # bbc_signUp.save_match(self, *req_json)
        match_id = db.select_db("SELECT id FROM bbc_match ORDER BY create_time DESC LIMIT 1")[0][0]
        logger.info(f"创建的蓝桥杯赛事活动ID是{match_id}")
        res = bbc_signUp.enable_match(match_id)
        assert res.status is True

    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize("req_json", datapool.supply(
    #     'test_bbc_signup.yml',
    #     'test_submit_registration_information'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_submit_registration_information(self):
        res = bbc_signUp.submit_registration_information()
        assert res.status is True
        signin_id = res.sdata.get('id')
        logger.info(f"报名ID是{signin_id}")


if __name__ == '__main__':
    pytest.main(
        ["-q", "-s", "test_blue_bridge_contest.py::TestBlueBridgeContest"])
