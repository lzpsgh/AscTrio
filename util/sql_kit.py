#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 上午11:01

from util.mysql_kit import mysqler


# 查询数据库：手机号对应的userid
def sql_phone_to_userid(phone):
    user_id = mysqler.query(f"SELECT id FROM user WHERE user.phone = \'{phone}\'")[0][0]
    return user_id


# 查询数据库：payRecordId对应的outTradeNo
def sql_payrecordid_to_outtradeno(prid):
    out_trade_no = mysqler.query(
        f"SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE pr.id = '{prid}';")[
        0][0]
    return out_trade_no


# 查询数据库：最新创建的报名活动id
def sql_matchid():
    match_id = mysqler.query(f"SELECT id FROM bbc_match ORDER BY create_time DESC LIMIT 1")[0][0]
    return match_id


# 更新数据库：将对应报名ID用户的openid改成自己的
def sql_fix_openid(signin_id):
    res = mysqler.query(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = \'{signin_id}\'")


if __name__ == '__main__':
    pass