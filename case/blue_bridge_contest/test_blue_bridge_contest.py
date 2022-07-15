#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from api.blue_bridge_contest_match import bbc_match
from api.blue_bridge_contest_signup import bbc_signUp
from api.user import user
from serv import bbc_serv
from util import sql_util
from util.data_util import data_pool
from util.faker_util import fakerist
from util.log_util import logger


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestBlueBridgeContest:

    @pytest.mark.repeat(5)
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'h5_query444'))
    # @pytest.mark.parametrize("kwargs", None)
    def test_result_inquiry(self, kwargs):
        kwargs_query = dict(identityNo='111', phone='222')
        kwargs_query['identityNo'] = kwargs['identityNo']
        kwargs_query['phone'] = kwargs['phone']
        kwargs_query['identityType'] = 'IDCARD'
        res = bbc_match.result_inquiry(**kwargs_query)
        # award = res.sdata.get('resultInquiryList')[0].get('winningResults')
        # logger.info(f'获奖情况={award}')
        # assert award == kwargs['award']
        prom = res.sdata.get('resultInquiryList')[0].get('promotionResult')
        logger.info(f'晋级情况={prom}')
        assert prom == kwargs['prom']

    @pytest.mark.skip
    @pytest.mark.parametrize("match_id", [70])
    def test_manual_mark(self, match_id):
        # match_id = 70  # 报名活动ID
        res = bbc_match.manual_mark(match_id)
        assert res.status is True

    # 完整流程,执行前需修改【报名活动id，试卷id，考试id】
    # @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_pay_audit(self, kwargs):
        match_id = '90'
        paper_id = '65'
        exam_id = '89'
        # res = bbc_serv.sub_pay_audit(kwargs, match_id)
        res = bbc_serv.sub_pay_audit_login_answer(kwargs, match_id, paper_id, exam_id)
        assert res.status is True

    # 提交答卷
    @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_submit_paper.yml', 'submit_official_paper'))
    def test_submit_official_paper(self, kwargs):
        res = bbc_match.submit_official_paper(**kwargs)
        assert res.status is True

    # 保存作品
    @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_submit_paper.yml', 'save_project_43'))
    def test_save_project(self, kwargs):
        res = bbc_match.submit_official_paper(**kwargs)
        assert res.status is True

    # 登录考试系统
    @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login2'))
    def test_exam_login(self, kwargs):
        kwargs['examId'] = 'e0e684cd-5e9e-476c-89c4-9e99437ebfe8'  # 考试id对应的uuid
        kwargs['identityType'] = 'IDCARD'
        kwargs['identityNo'] = '371325198509024721'
        res = bbc_match.exam_login(**kwargs)
        assert res.status is True

    # 新增正式考试
    @pytest.mark.skip
    # @pytest_autoparam
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_exam_formal_enable(self, kwargs):
        res = bbc_match.new_exam(**kwargs)
        assert res.status is True
        exam_id = res.sdata
        bbc_match.enable_exam(exam_id)

    # 新增正式考试
    @pytest.mark.skip
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_contest_data.yml', 'add_exam_formal_senior'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_exam_formal_enable(self, kwargs):
        res = bbc_match.new_exam(**kwargs)
        assert res.status is True
        exam_id = res.sdata
        bbc_match.enable_exam(exam_id)

    # 新增模拟考试
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_contest_data.yml', 'add_exam_simu'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_exam_formal_enable(self, kwargs):
        kwargs['examName'] = fakerist.word() + fakerist.numerify()
        kwargs['startTime'] = "2021-11-03 11:32:00"
        kwargs['testpaperId'] = 79
        kwargs['sortWeight'] = 32
        res = bbc_match.new_exam(**kwargs)
        assert res.status is True
        exam_id = res.sdata
        bbc_match.enable_exam(exam_id)

    @pytest.mark.skip
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_signup_data.yml', 'audit_fail'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_audit_fail(self, kwargs):
        res = bbc_signUp.audit(**kwargs)
        assert res.status is True

    @pytest.mark.skip
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_signup_data.yml', 'audit_pass'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_audit_pass(self, kwargs):
        res = bbc_signUp.audit(**kwargs)
        assert res.status is True

    # 创建单选题题目
    @pytest.mark.skip
    @pytest.mark.parametrize('kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_single'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_single(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建多选题题目
    @pytest.mark.skip
    @pytest.mark.parametrize('kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_multi'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_multi(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建判断题题目
    @pytest.mark.skip
    @pytest.mark.parametrize('kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_judge'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_judge(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建填空题题目
    @pytest.mark.skip
    @pytest.mark.parametrize('kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_blank'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_blank(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建编程题题目
    @pytest.mark.skip
    @pytest.mark.parametrize('kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_code'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_code(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_signup_data.yml', 'submit_reg_info'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_registration_information(self, kwargs):
        kwargs['matchId'] = '58'
        phone = kwargs['phone']
        userid = sql_util.sql_phone_to_userid(phone)
        user.reset_pwd(userid)
        user.login(phone)
        res = bbc_signUp.submit_registration_information(**kwargs)
        assert res.status is True
        signin_id = res.sdata.get('id')
        logger.info(f"报名ID是{signin_id}")
        sql_util.sql_fix_openid(signin_id)

    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_knowpoint(self):
        res = bbc_match.new_knowpoint("abbbccc")
        assert res.status is True

    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_signup_data.yml', 'save_match_1'))
    def test_save_match_enable(self, kwargs):
        res = bbc_serv.save_match_enable(kwargs)


if __name__ == '__main__':
    pass
    # res = bbc_signUp.enable(1, 61)
    # assert res.status is True
    # bbc_signUp.test_submit_pay_audit() "-n auto",
    # pytest.main(["-q", "-s", "-n", "auto", "test_blue_bridge_contest.py::TestBlueBridgeContest::test_result_inquiry"])

