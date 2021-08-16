#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 下午1:50
from api.blue_bridge_contest_signup import bbc_signUp
from api.goods_order import goods_order
from util import sql_util
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


if __name__ == '__main__':
    pass
