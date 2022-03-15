#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 上午1:01

from api.anniv_answer_award import anniv_answer_award


# 保存活动并上架
def save_on(var):
    # 查表获取usercoupon表的id
    anniv_answer_award.save()
    anniv_answer_award.update_status()
    # couponIds = sql_util.sql_usercouponid(user_id, goods_id)
    # kwargs0 = data_pool.supply('.yml', '')[0]
    # kwargs0['userId'] = var  
    # kwargs0['goodsIds'] = couponIds 
    # res0 = goods_order.demolition_order(**kwargs0)
    # assert res0.status is True 


# 抽奖并查看中奖记录
# 函数名
def lottery(var):
    # 查表获取usercoupon表的id
    anniv_answer_award.start()
    anniv_answer_award.get_prize_record()
    # couponIds = sql_util.sql_usercouponid(user_id, goods_id)
    # kwargs0 = data_pool.supply('.yml', '')[0]
    # kwargs0['userId'] = var
    # kwargs0['goodsIds'] = couponIds
    # res0 = goods_order.demolition_order(**kwargs0)
    # assert res0.status is True


if __name__ == '__main__':
    pass
