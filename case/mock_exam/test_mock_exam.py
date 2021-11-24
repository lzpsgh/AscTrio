#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from api.mock_exam import mock_exam
from util import time_util
from util.data_util import data_pool
from util.faker_util import fakerist


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestMockExam:

    # 新建知识点
    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('mock_exam_data.yml', 'new_knowpoint'))
    def test_new_knowpoint(self, kwargs):
        res = mock_exam.new_knowpoint(**kwargs)
        assert res.status is True

    # 新建题目
    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('mock_exam_data.yml', 'new_subject_scratch'))
    def test_new_subject(self, kwargs):
        kwargs['subDescribe'] = '随图形' + fakerist.word() + time_util.get_mdhms()
        kwargs['degree'] = 0
        kwargs['programType'] = 0  # 1 python 0图形化
        kwargs['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试
        kwargs['knowledgePointId'] = 593
        res2 = mock_exam.new_subject(**kwargs)
        assert res2.status is True

    # 新建试卷
    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('mock_exam_data.yml', 'new_paper_complex'))
    def test_new_paper(self, kwargs):
        kwargs['programType'] = 0  # 1 python 0图形化
        kwargs['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试
        kwargs['name'] = '图形等级考1357102030' + fakerist.word()
        res3 = mock_exam.new_paper(**kwargs)
        assert res3.status is True

    # 新增考试
    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('mock_exam_data.yml', 'new_exam'))
    def test_new_exam_enable(self, kwargs):
        kwargs['testpaperId'] = 121  # 修改试卷id
        kwargs['programType'] = 1  # 1 python 0图形化
        kwargs['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试 其他
        kwargs['startTime'] = time_util.after_min(3)
        kwargs['endTime'] = "2021-11-15 16:30:00"
        kwargs['examName'] = '随机2单py' + fakerist.word() + time_util.get_mdhms()
        res4 = mock_exam.new_exam(**kwargs)
        exam_id = res4.sdata

        kwargs5 = data_pool.supply('mock_exam_data.yml', 'enable_exam')[0]
        kwargs5['id'] = exam_id
        kwargs5['enable'] = 1  # 启用考试
        res5 = mock_exam.enable_exam(**kwargs5)
        assert res5.status is True


if __name__ == '__main__':
    pass
