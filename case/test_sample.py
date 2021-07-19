#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 上午12:58

import pytest

from api.sample import sample
from util.data_kit import data_pool


# @allure.severity(allure.severity_level.NORMAL)
# @allure.epic("针对业务场景的测试")
# @allure.feature("场景：leadsapi获取token后提交入库")
class TestSample:

    # @allure.story("故事：leadsapi获取token后提交入库")
    # @allure.description("该用例是针对 leadsapi获取token后提交入库 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("标题：leadsapi获取token后提交入库")
    @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('data_leads_api.yml', 'upload_info'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_sample_get(self, kwargs):
        # 传给api层调用之前可自行修改kwargs任意键的值
        kwargs['token'] = 'res_token'
        result = sample.req_get(**kwargs)
        assert result.status is True
        # logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        # logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_sample.py::TestSample"])
