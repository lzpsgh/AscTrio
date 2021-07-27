#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 下午4:22

# 模块名称：蓝桥杯编程比赛-报名系统
# Swagger： 蓝桥杯报名类接口，蓝桥杯赛事管理类接口

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit


class BBCSignUp(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(BBCSignUp, self).__init__(api_root_url, **kwargs)

    def submit_registration_information(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/bbcEnterName/submitRegistrationInformation'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('web'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result
        # 响应
        # code 000001
        # data{
        #     "id": 20
        # }'''

    # 创建订单并返回支付所需参数，订单不包含课程, 微信的用以前的支付回调，支付宝的
    def create_order(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/bbcEnterName/createOrder'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # {
    #   "code" : "000001",
    #   "data" : {
    #     "payPage" : "<form name=\"punchout_form\" method=\"post\" action=\"https:\/\/openapi.alipaydev.com\/gateway.do?charset=utf-8&method=alipay.trade.wap.pay&sign=HhM2KTXaLorCdop3VvhXwHsOKdbMQj6HSoWo5EpEthM2HQ2CVa6cag6xWJk0cI0Of3WqYmycgExSX24ocAaqvee3IB5Gyq0Hd1jjL2LimHAaeShpYGNe2RXNY4yLv%2BDyHDaDPSJhOwgUwq91BMhUu4RCJkCxM%2FljzpveJInsJ3vtFuQ1BHNbg0ca0NvWQgU72bDj4vI2KVSZw4tIlmwQeRxcHav6a%2BC9s17Hm15MESUo0YRpC025JJeJ8ne47Cd3Zu%2BpUBfibZj4KIyy2yNRpBlBqz9u27AvsBvegW4R01Yk6n0YKTGIOKxdFBiZcpNzXZBO%2FsTYzKmpGlHAW4dvAA%3D%3D&return_url=https%3A%2F%2Fsit.miaocode.com%2Fh5competition%2Fpay%3Fid%3D20%26matchId%3D21&notify_url=http%3A%2F%2Fsit.miaocode.com%3A80%2Fcore%2Falipay%2FnotifyCallback&version=1.0&app_id=2016110300790491&sign_type=RSA2&timestamp=2021-07-06+14%3A45%3A00&alipay_sdk=alipay-sdk-java-3.0.52.ALL&format=json\">\n<input type=\"hidden\" name=\"biz_content\" value=\"{&quot;body&quot;:&quot;妙小程-蓝桥杯报名费&quot;,&quot;out_trade_no&quot;:&quot;202107061445009866774686&quot;,&quot;product_code&quot;:&quot;QUICK_WAP_WAY&quot;,&quot;subject&quot;:&quot;蓝桥杯报名费&quot;,&quot;timeout_express&quot;:&quot;2h&quot;,&quot;total_amount&quot;:&quot;0.50&quot;}\">\n<input type=\"submit\" value=\"立即支付\" style=\"display:none\" >\n<\/form>\n<script>document.forms[0].submit();<\/script>",
    #     "payrecordId" : 45507
    #   },
    #   "message" : "操作成功",
    #   "success" : true,
    #   "difTimeStamp" : 0
    # }

    # 创建订单并返回支付所需参数，订单不包含课程
    def get_order_status(self, id):
        self.req_method = 'GET'
        self.req_url = '/core/bbcEnterName/getOrderStatus'
        self.req_body = {
            "id": id
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # code 000001
    # data{
    #     "status": "NOT_CREATED"
    # }

    # 审核通过不通过
    def audit(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/matchManager/audit'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        # result = self.x_request()
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_kit.result_check(result)
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
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_kit.result_check(result)
        return result

    # 保存赛事优化版
    def save_match(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/matchManager/saveMatch'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        res = self.x_request()
        assert_kit.result_check(res)
        return res


bbc_sigUp = BBCSignUp(common_kit.env('BASE_URL'))

if __name__ == '__main__':
    bbc_signUp.save_match()
