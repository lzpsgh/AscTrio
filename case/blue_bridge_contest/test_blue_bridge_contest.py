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
from util.log_util import logger


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestBlueBridgeContest:

    @pytest.mark.repeat(5)
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'h5_query444'))
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

    # @pytest.mark.skip
    @pytest.mark.parametrize("match_id", [70])
    def test_manual_mark(self, match_id):
        # match_id = 70  # 报名活动ID
        res = bbc_match.manual_mark(match_id)
        assert res.status is True

    # 完整流程,执行前需修改【报名活动id，试卷id，考试id】
    @pytest.mark.skip
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login2'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_pay_audit(self, kwargs):
        match_id = '69'
        paper_id = '65'
        exam_id = '84'
        res = bbc_serv.sub_pay_audit_login_answer(kwargs, match_id, paper_id, exam_id)
        assert res.status is True
        #
        # id_number = kwargs['identityNo']
        # kwargs['idNumber'] = id_number
        #
        # phone = kwargs['phone']
        # userid = sql_util.sql_phone_to_userid(phone)
        # user.reset_pwd(userid)
        # user.login(phone)
        # kid_name = fakerist.name()
        #
        # kwargs['matchId'] = match_id
        #
        # kwargs['dateOfBirth'] = "2012年08月11日"
        # kwargs['typeOfCertificate'] = 'IDCARD'
        #
        # kwargs['participants'] = kid_name
        # kwargs['guardian'] = kid_name + '的男妈妈'
        # kwargs['city'] = fakerist.city()
        # kwargs['mailbox'] = fakerist.email()
        # kwargs['address'] = fakerist.street_address()
        # kwargs['code'] = "123456"
        # kwargs['areaCode'] = "86"
        # kwargs['idPhoto'] = "https://res.miaocode.com/competition/files/1625672893591.jpeg"
        # kwargs['gender'] = fakerist.sex()
        # kwargs['province'] = fakerist.province()  # 注意在非中文语种下会报错
        # kwargs['region'] = fakerist.district()
        # kwargs['provinceAndCity'] = f"{kwargs['province']}，{kwargs['region']}"
        # kwargs['school'] = fakerist.word()
        # kwargs['typeOfCertificate'] = 'IDCARD'
        #
        # res = bbc_signUp.submit_registration_information(**kwargs)
        # assert res.status is True
        # signin_id = res.sdata.get('id')
        # logger.info(f"报名手机号是{phone}, 报名身份证是{id_number}")
        # logger.info(f"报名ID是{signin_id}")
        #
        # # 下单支付
        # kwargs3 = data_pool.supply('bbc_signup_data.yml', 'create_order')[0]
        # kwargs3['id'] = int(signin_id)
        # kwargs3['userId'] = userid
        # kwargs3['payType'] = "WX"
        # # bbc_serv.pay_regfee_ali(kwargs3)
        # res3 = bbc_signUp.create_order(**kwargs3)
        # pay_record_id = res3.sdata.get("payrecordId")
        # out_trade_no = sql_util.sql_payrecordid_to_outtradeno(pay_record_id)
        # goods_order.pay_callback_suc(out_trade_no)
        #
        # # 审核通过
        # kwargs4 = data_pool.supply('bbc_signup_data.yml', 'audit_pass')[0]
        # kwargs4['enable'] = 1
        # kwargs4['id'] = signin_id
        # res4 = bbc_signUp.audit(**kwargs4)
        # assert res4.status is True
        #
        # # 用户登录: 身份证-考试id为70
        # # 将查到的userid保存到 临时的kwargs['userId'] 中用于后续的作品保存和答卷提交
        # kwargs5 = data_pool.supply('bbc_submit_paper.yml', 'exam_login')[0]
        # exam_uuid = sql_util.sql_examid_to_uuid(exam_id)
        # kwargs5['examId'] = exam_uuid  # 考试uuid
        # kwargs5['identityType'] = 'IDCARD'
        # kwargs5['identityNo'] = id_number
        # kwargs5['phone'] = phone
        # res5 = bbc_match.exam_login(**kwargs5)
        # assert res5.status is True
        #
        # # # 保存作品 编程题4
        # # 需要提前修改 subjectId
        # # kwargs6 = data_pool.supply('bbc_submit_paper.yml', 'save_project_43')[0]
        # # kwargs6['userId'] = userid
        # # kwargs6['subjectId'] = '560'
        # # kwargs6['examinationId'] = exam_id
        # # kwargs6['dataURL'] = "https://res.miaocode.com/9c011017-e2a0-4cd8-86be-4982660c4e85.mxc"
        # # res6 = bbc_match.save_project(**kwargs6)
        # # assert res6.status is True
        # # # 保存作品 编程题3
        # # kwargs7 = kwargs6
        # # kwargs6['userId'] = userid
        # # kwargs7['subjectId'] = '561'
        # # kwargs6['examinationId'] = exam_id
        # # kwargs7['dataURL'] = "https://res.miaocode.com/e0519ef5-fdc9-4ecf-8129-b8bddcfb3d41.mxc"
        # # res7 = bbc_match.save_project(**kwargs7)
        # # assert res7.status is True
        #
        # # 提交试卷(非编程题部分)
        # kwargs8 = data_pool.supply('bbc_submit_paper.yml', 'submit_official_paper')[0]
        # # 实际上不是传userid，而是传 报名活动下的该用户自己的报名id
        # kwargs8['userId'] = str(signin_id)
        # kwargs8['examinationId'] = str(exam_id)
        # kwargs8['testPaperId'] = int(paper_id)
        # res8 = bbc_match.submit_official_paper(**kwargs8)
        # # assert res8.status is True f返回false

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
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_contest_data.yml', 'add_exam_formal_senior'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_exam_formal_enable(self, kwargs):
        res = bbc_match.add_exam(**kwargs)
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
        # 将用户的openid设置为iphone12mini上的
        sql_util.sql_fix_openid(signin_id)

    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_knowpoint(self):
        res = bbc_match.new_knowpoint("abbbccc")
        assert res.status is True

    @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_signup_data.yml', 'save_match_1'))
    def test_save_match_enable(self, kwargs):
        res = bbc_serv.save_match_enable(kwargs)
        assert res.status is True


if __name__ == '__main__':
    pass
    # res = bbc_signUp.enable(1, 61)
    # assert res.status is True
    # bbc_signUp.test_submit_pay_audit() "-n auto",
    # pytest.main(["-q", "-s", "-n", "auto", "test_blue_bridge_contest.py::TestBlueBridgeContest::test_result_inquiry"])

