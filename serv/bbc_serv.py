#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 下午1:42
from api.blue_bridge_contest_match import bbc_match
from api.blue_bridge_contest_signup import bbc_signUp
from api.goods_order import goods_order
from api.user import user
from util import sql_util
from util.data_util import data_pool
from util.faker_util import fakerist
from util.log_util import logger


# 已弃用 提交报名记录
def pay_regfee_ali(kwargs):
    res2 = bbc_signUp.create_order(**kwargs)
    pay_record_id = res2.sdata.get("payrecordId")
    if pay_record_id is None:
        raise Exception("aaaa")
    # 模拟支付回调
    out_trade_no = sql_util.sql_payrecordid_to_outtradeno(pay_record_id)
    goods_order.pay_callback_suc(out_trade_no)


# 创建报名活动并开启
def save_match_enable(kwargs):
    res = bbc_signUp.save_match(**kwargs)
    match_id = sql_util.sql_matchid()
    # match_id = res.sdata  # TODO 等开发改好接口后要换成这个
    logger.info(f"创建的蓝桥杯赛事活动ID是{match_id}")
    res1 = bbc_signUp.enable(1, match_id)
    assert res1.status is True


# 考生登录并提交答卷,调用前请确保考生已审核通过
def exam_login_answer():
    pass


# 提交报名信息并完款支付并审核通过，登录考试并提交答卷
def sub_pay_audit_login_answer(kwargs, m_match_id, m_paper_id, m_exam_id):
    # 报名活动ID
    match_id = m_match_id
    # 试卷ID
    paper_id = m_paper_id
    # 考试ID，不是考试UUID
    exam_id = m_exam_id

    phone = kwargs['phone']
    userid = sql_util.sql_phone_to_userid(phone)
    user.reset_pwd(userid)
    user.login(phone)
    # id_number = kwargs['identityNo']
    id_number = fakerist.ssn()
    kwargs['idNumber'] = id_number
    kwargs['matchId'] = match_id
    kwargs['dateOfBirth'] = "2012年08月11日"  # TODO
    kwargs['typeOfCertificate'] = 'IDCARD'  # TODO
    kid_name = fakerist.name()
    kwargs['participants'] = kid_name
    kwargs['guardian'] = kid_name + '的男妈妈'
    kwargs['city'] = fakerist.city()
    kwargs['mailbox'] = fakerist.email()
    kwargs['address'] = fakerist.street_address()
    kwargs['code'] = "123456"  # TODO
    kwargs['areaCode'] = "86"  # TODO
    kwargs['idPhoto'] = "https://res.miaocode.com/competition/files/1625672893591.jpeg"
    kwargs['gender'] = fakerist.sex()
    kwargs['province'] = fakerist.province()  # 注意在非中文语种下会报错
    kwargs['region'] = fakerist.district()
    kwargs['provinceAndCity'] = f"{kwargs['province']}，{kwargs['region']}"
    kwargs['school'] = fakerist.word()

    # 提交报名信息
    res = bbc_signUp.submit_registration_information(**kwargs)
    signin_id = res.sdata.get('id')
    logger.info(f"报名手机号是{phone}, 报名身份证是{id_number}, 报名ID是{signin_id}")

    # 下单支付
    kwargs3 = data_pool.supply('bbc_signup_data.yml', 'create_order')[0]
    kwargs3['id'] = int(signin_id)
    kwargs3['userId'] = userid
    kwargs3['payType'] = "WX"  # TODO
    # bbc_serv.pay_regfee_ali(kwargs3)
    res3 = bbc_signUp.create_order(**kwargs3)
    # 模拟支付回调成功
    pay_record_id = res3.sdata.get("payrecordId")
    out_trade_no = sql_util.sql_payrecordid_to_outtradeno(pay_record_id)
    goods_order.pay_callback_suc(out_trade_no)

    # 审核通过
    kwargs4 = data_pool.supply('bbc_signup_data.yml', 'audit_pass')[0]
    kwargs4['enable'] = 1
    kwargs4['id'] = signin_id
    res4 = bbc_signUp.audit(**kwargs4)

    # 用户登录: 身份证-考试id为70
    # 将查到的userid保存到 临时的kwargs['userId'] 中用于后续的作品保存和答卷提交
    kwargs5 = data_pool.supply('bbc_submit_paper.yml', 'exam_login')[0]
    exam_uuid = sql_util.sql_examid_to_uuid(exam_id)
    kwargs5['examId'] = exam_uuid  # 考试uuid
    kwargs5['identityType'] = 'IDCARD'  # TODO
    kwargs5['identityNo'] = id_number
    kwargs5['phone'] = phone
    res5 = bbc_match.exam_login(**kwargs5)

    # # 保存作品 提交试卷的编程题4
    # 需要提前修改 subjectId
    # kwargs6 = data_pool.supply('bbc_submit_paper.yml', 'save_project_43')[0]
    # kwargs6['userId'] = userid
    # kwargs6['subjectId'] = '560'
    # kwargs6['examinationId'] = exam_id
    # kwargs6['dataURL'] = "https://res.miaocode.com/9c011017-e2a0-4cd8-86be-4982660c4e85.mxc"
    # res6 = bbc_match.save_project(**kwargs6)
    # assert res6.status is True
    # # 保存作品 提交试卷的编程题3
    # kwargs7 = kwargs6
    # kwargs6['userId'] = userid
    # kwargs7['subjectId'] = '561'
    # kwargs6['examinationId'] = exam_id
    # kwargs7['dataURL'] = "https://res.miaocode.com/e0519ef5-fdc9-4ecf-8129-b8bddcfb3d41.mxc"
    # res7 = bbc_match.save_project(**kwargs7)
    # assert res7.status is True

    # 提交试卷(非编程题部分)
    kwargs8 = data_pool.supply('bbc_submit_paper.yml', 'submit_official_paper')[0]
    # 实际上不是传userid，而是传 报名活动下的该用户自己的报名id
    kwargs8['userId'] = str(signin_id)
    kwargs8['examinationId'] = str(exam_id)
    kwargs8['testPaperId'] = int(paper_id)
    res8 = bbc_match.submit_official_paper(**kwargs8)
    # assert res8.status is True f返回false  # TODO 找开发改接口，返回data
    return res8


if __name__ == '__main__':
    pass
