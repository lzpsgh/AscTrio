#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 上午11:01

from util.mysql_util import mysqler


# 查询：用户的积分数
def sql_user_integration(phone):
    inte = mysqler.query(f" SELETE integration FROM user WHERE phone=\'{phone}\'")[0][0]
    print(inte)
    return inte


# 查询：考试id对应的考试uuid 75对应dda7de8c-b5ae-4b21-8582-3c5aad76d2c2
def sql_examid_to_uuid(exam_id):
    uuid = mysqler.query(f"SELECT uuid FROM bbc_examination be WHERE be.id = \'{exam_id}\'")[0][0]
    print(uuid)
    return uuid


# 查询：手机号对应的userid
def sql_phone_to_userid(phone):
    user_id = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
    return user_id


# 查询：payRecordId对应的outTradeNo
def sql_payrecordid_to_outtradeno(prid):
    out_trade_no = mysqler.query(
        f"SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE pr.id = '{prid}';")[
        0][0]
    return out_trade_no


# 查询：最新创建的报名活动id
def sql_matchid():
    match_id = mysqler.query(f"SELECT id FROM bbc_match ORDER BY create_time DESC LIMIT 1")[0][0]
    return match_id


# 更新：将对应报名ID用户的openid改成自己的
def sql_fix_openid(signin_id):
    res = mysqler.query(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = \'{signin_id}\'")
    return res


# 查询单张票券的票券id
def sql_usercouponid(user_id, coupon_id):
    tmp = f"SELECT id FROM usercoupon uc WHERE userId = '{user_id}' AND couponRule = '{coupon_id}';"
    res = mysqler.query(tmp)
    return res


# OMO修改订金金额
def modify_sub_amount(amount):
    tmp = f"UPDATE mxc_uat.dictionary SET remark = '{amount}' WHERE code = 'DEPOSIT_AMOUNT' "
    res = mysqler.execute(tmp)
    return res

def xxx(channel_code):
    tmp = f"select channel_code from abs_organization.station_station_ext as sse where 1 and channel_code like '{channel_code}' order by create_time desc;"
    res = mysqler.query(tmp)[0][0]
    return res

if __name__ == '__main__':
    # exam_id = '75'
    # sql_examid_to_uuid(exam_id)
    res1 = xxx('GZ00200138T')
    print(res1)
