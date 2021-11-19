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

    # @pytest.mark.repeat(5)
    # # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'h5_query444'))
    # # @pytest.mark.parametrize("kwargs", None)
    # def test_result_inquiry(self, kwargs):
    #     kwargs_query = dict(identityNo='111', phone='222')
    #     kwargs_query['identityNo'] = kwargs['identityNo']
    #     kwargs_query['phone'] = kwargs['phone']
    #     kwargs_query['identityType'] = 'IDCARD'
    #     res = bbc_match.result_inquiry(**kwargs_query)
    #     # award = res.sdata.get('resultInquiryList')[0].get('winningResults')
    #     # logger.info(f'获奖情况={award}')
    #     # assert award == kwargs['award']
    #     prom = res.sdata.get('resultInquiryList')[0].get('promotionResult')
    #     logger.info(f'晋级情况={prom}')
    #     assert prom == kwargs['prom']
    #
    # @pytest.mark.skip
    # @pytest.mark.parametrize("match_id", [70])
    # def test_manual_mark(self, match_id):
    #     # match_id = 70  # 报名活动ID
    #     res = bbc_match.manual_mark(match_id)
    #     assert res.status is True
    #
    # # 完整流程,执行前需修改【报名活动id，试卷id，考试id】
    # # @pytest.mark.skip
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
    # @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    # def test_submit_pay_audit(self, kwargs):
    #     match_id = '90'
    #     paper_id = '65'
    #     exam_id = '89'
    #     # res = bbc_serv.sub_pay_audit(kwargs, match_id)
    #     res = bbc_serv.sub_pay_audit_login_answer(kwargs, match_id, paper_id, exam_id)
    #     assert res.status is True
    #
    # # 提交答卷
    # @pytest.mark.skip
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_submit_paper.yml', 'submit_official_paper'))
    # def test_submit_official_paper(self, kwargs):
    #     res = bbc_match.submit_official_paper(**kwargs)
    #     assert res.status is True
    #
    # # 保存作品
    # @pytest.mark.skip
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_submit_paper.yml', 'save_project_43'))
    # def test_save_project(self, kwargs):
    #     res = bbc_match.submit_official_paper(**kwargs)
    #     assert res.status is True
    #
    # # 登录考试系统
    # @pytest.mark.skip
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login2'))
    # def test_exam_login(self, kwargs):
    #     kwargs['examId'] = 'e0e684cd-5e9e-476c-89c4-9e99437ebfe8'  # 考试id对应的uuid
    #     kwargs['identityType'] = 'IDCARD'
    #     kwargs['identityNo'] = '371325198509024721'
    #     res = bbc_match.exam_login(**kwargs)
    #     assert res.status is True

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
        # assert res4.status is True

        kwargs5 = data_pool.supply('mock_exam_data.yml', 'enable_exam')[0]
        kwargs5['id'] = exam_id
        kwargs5['enable'] = 1  # 启用考试
        res5 = mock_exam.enable_exam(**kwargs5)
        assert res5.status is True


if __name__ == '__main__':
    pass
