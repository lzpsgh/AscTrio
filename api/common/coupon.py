#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 上午10:46

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


# 总流程
# 1. 新增票圈批次
# 2. 获取cc最新的票券列表
# 3. 去特定的cc上推送1张票券给指定的用户，查看票券发放情况
# 4. 查看用户所拥有的票券情况
# 5. 实际支付使用票券


class Coupon(BaseRequest):

    # 新增票券批次
    # 返回data/id '4329', data/no 'c_asdfadsfasd'

    def create_coupon_new_version(self):
        self.req_method = 'POST'
        self.req_url = '/core/coupon/createCouponNewVersion'
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        self.req_body = {
            'title': 'title',
            'couponTypeId': 25,
            'type': 'CASH_COUPON',  # 现金 CASH_COUPON 满减 VOUCHER
            'meetamount': 0,
            'subamount': 2333,
            'couponAmount': 2,  # 0 不限
            'sendMode': 0,  # 0 手动推送
            'sendType': 2,  # 1新签 2续费
            'effectiveDate': "2021-06-10 15:15:00",  # 时间段-绝对
            'expiryDate': '2021-06-10 15:30:00',  # 时间段-绝对
            'isEnable': 0,  # 立即启用
            'accountList': [{"accountId": 3220}, {"accountId": 3155}],
            'roleList': []
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # cc推送优惠券给userid
    def send_coupon_to_user(self, couponid, userid):
        self.req_method = 'POST'
        self.req_url = '/core/coupon/sendCoupon2User'
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        self.req_body = {
            "couponId": couponid,
            "userId": userid
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result


coupon = Coupon(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    coupon.create_coupon_new_version()  # 1-30  进行中
    # dbf.dbf
