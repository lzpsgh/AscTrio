#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from api.blue_bridge_contest_match import bbc_match
from api.blue_bridge_contest_signup import bbc_signUp
from api.user import user
from util import sql_util
from util.data_util import data_pool
from util.faker_util import fakerist
from util.log_util import logger


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestBlueBridgeContest:

    # 提交答卷
    # @pytest.mark.parametrize(
    #     "kwargs", data_pool.supply('bbc_contest_data.yml', 'submit_official_paper_1'))
    # # @pytest.mark.usefixtures("crm_login_with_mm")
    # def test_submit_official_paper_1(self, kwargs):
    #     res = bbc_match.submit_official_paper(**kwargs)
    #     assert res.status is True

    # 登录考试系统
    @pytest.mark.skip
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_contest_data.yml', 'exam_login'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_exam_login(self, kwargs):
        res = bbc_match.exam_login(**kwargs)
        assert res.status is True

    # @pytest.mark.parametrize(
    #     'kwargs', data_pool.supply('bbc_contest_data.yml', 'xxx'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    # def test_manual_mark(self):
    #     res = bbc_match.manual_mark('51')
    #     assert res.status is True

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

    # 新增模拟考试
    @pytest.mark.skip
    @pytest.mark.repeat(3)
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_contest_data.yml', 'add_exam_simu'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_exam_simu_enable(self, kwargs):
        kwargs['examName'] = fakerist.name() + '考试'
        res = bbc_match.add_exam(**kwargs)
        assert res.status is True
        exam_id = res.sdata
        bbc_match.enable_exam(self, exam_id)

    # 完整流程
    @pytest.mark.skip
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_signup_data_1.yml', 'submit_registration_information_senior'))
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    def test_submit_pay_audit(self, kwargs):
        phone = kwargs['phone']
        userid = sql_util.sql_phone_to_userid(phone)
        user.reset_pwd(userid)
        user.login(phone)
        kid_name = fakerist.name()

        kwargs['matchId'] = '61'  # 报名活动ID
        kwargs['dateOfBirth'] = "2014年09月01日"
        kwargs['typeOfCertificate'] = 'IDCARD'
        id_number = fakerist.ssn()
        kwargs['idNumber'] = id_number

        kwargs['participants'] = kid_name
        kwargs['guardian'] = kid_name + '的男妈妈'
        kwargs['city'] = fakerist.city()
        kwargs['mailbox'] = fakerist.email()
        kwargs['address'] = fakerist.street_address()
        kwargs['code'] = "123456"
        kwargs['areaCode'] = "86"
        kwargs['idPhoto'] = "https://res.miaocode.com/competition/files/1625672893591.jpeg"
        kwargs['gender'] = fakerist.sex()
        kwargs['province'] = fakerist.province()  # 注意在非中文语种下会报错
        kwargs['region'] = fakerist.district()
        kwargs['provinceAndCity'] = f"{kwargs['province']}，{kwargs['region']}"
        kwargs['school'] = fakerist.word()
        kwargs['typeOfCertificate'] = 'IDCARD'
        res = bbc_signUp.submit_registration_information(**kwargs)
        assert res.status is True
        signin_id = res.sdata.get('id')
        logger.info(f"报名手机号是{phone}, 报名身份证是{id_number}")
        logger.info(f"报名ID是{signin_id}")

        # 方案1，纯api层
        # 创建订单获取 payrecordId
        # kwargs2 = data_pool.supply('bbc_signup_data.yml', 'create_order_ali')[0]
        # kwargs2['id'] = int(signin_id)
        # kwargs2['userId'] = userid
        # res2 = bbc_signUp.create_order(**kwargs2)
        # pay_record_id = res2.sdata.get("payrecordId")
        # if pay_record_id is None:
        #     raise Exception("aaaa")
        # # 模拟支付回调
        # out_trade_no = sql_kit.sql_payrecordid_to_outtradeno(pay_record_id)
        # goods_order.pay_callback_suc(out_trade_no)

        # 方案2，使用serv层
        # 下单支付
        # kwargs3 = data_pool.supply('bbc_signup_data.yml', 'create_order')[0]
        # kwargs3['id'] = int(signin_id)
        # kwargs3['userId'] = userid
        # kwargs3['payType'] = "WX"
        # bbc_order_serv.pay_regfee_ali(kwargs3)

        # 审核通过
        # kwargs4 = data_pool.supply('bbc_signup_data.yml', 'audit_pass')[0]
        # kwargs4['enable'] = 1
        # kwargs4['id'] = signin_id
        # res4 = bbc_signUp.audit(**kwargs4)
        # assert res4.status is True

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
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_single'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_single(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建多选题题目
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_multi'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_multi(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建判断题题目
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_judge'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_judge(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建填空题题目
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_blank'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_blank(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建编程题题目
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'new_subject_code'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_new_subject_code(self, kwargs):
        res = bbc_match.new_subject(**kwargs)
        assert res.status is True

    # 创建试卷-无编程题
    @pytest.mark.skip
    @pytest.mark.parametrize(
        'kwargs', data_pool.supply('bbc_contest_data.yml', 'add_paper_withoutcode'))
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_add_paper(self, kwargs):
        res = bbc_match.add_paper(**kwargs)
        assert res.status is True

    @pytest.mark.skip
    # @allure.story("用例--注册/登录/查看--预期成功")
    # @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_signup_data.yml', 'save_match_1'))
    def test_save_match_enable(self, kwargs):
        res = bbc_signUp.save_match(**kwargs)
        assert res.status is True
        # match_id = sql_util.sql_matchid()
        # match_id = res.sdata
        # logger.info(f"创建的蓝桥杯赛事活动ID是{match_id}")
        # res1 = bbc_signUp.enable(1, match_id)
        # assert res1.status is True

    def test_test(self):
        res1 = bbc_signUp.enable(self, 1, 61)
        assert res1.status is True

    @pytest.mark.skip
    # @pytest.mark.single
    @pytest.mark.parametrize(
        "kwargs", data_pool.supply('bbc_signup_data.yml', 'submit_registration_information_senior'))
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


if __name__ == '__main__':
    # res = bbc_signUp.enable(1, 61)
    # assert res.status is True
    # bbc_signUp.test_submit_pay_audit()
    pytest.main(["-q", "-s", "test_blue_bridge_contest.py::TestBlueBridgeContest"])
