#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 下午1:42

from api.blue_bridge_contest_signup import bbc_signUp
from api.goods_order import goods_order
from util import sql_util


def pay_regfee_ali(kwargs):
    # 提交报名记录
    res2 = bbc_signUp.create_order(**kwargs)

    pay_record_id = res2.sdata.get("payrecordId")
    if pay_record_id is None:
        raise Exception("aaaa")
    # 模拟支付回调
    out_trade_no = sql_util.sql_payrecordid_to_outtradeno(pay_record_id)
    goods_order.pay_callback_suc(out_trade_no)


if __name__ == '__main__':
    pass
