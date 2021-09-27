#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 下午4:22

# 模块名称：蓝桥杯编程比赛-报名系统
# Swagger： 蓝桥杯报名类接口，蓝桥杯赛事管理类接口

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class BBCSignUp(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(BBCSignUp, self).__init__(api_root_url, **kwargs)

    def submit_registration_information(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/bbcEnterName/submitRegistrationInformation'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 创建订单并返回支付所需参数，订单不包含课程, 微信的用以前的支付回调，支付宝的
    def create_order(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/bbcEnterName/createOrder'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 创建订单并返回支付所需参数，订单不包含课程
    def get_order_status(self, id):
        self.req_method = 'GET'
        self.req_url = '/core/bbcEnterName/getOrderStatus'
        self.req_body = {
            "id": id
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 审核通过不通过
    def audit(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/matchManager/audit'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 启用禁用赛事
    def enable(self, is_enable, match_id):
        self.req_method = 'POST'
        self.req_url = '/core/matchManager/enableMatch'
        self.req_body = {
            "enable": is_enable,  # 1启用 0禁用
            "id": match_id
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 保存赛事优化版
    def save_match(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/matchManager/saveMatch'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        res = self.x_request()
        assert_util.result_check(res)
        return res


bbc_signUp = BBCSignUp(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    bbc_signUp.save_match()
