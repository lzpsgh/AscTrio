#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 下午4:22

# 模块名称：蓝桥杯编程比赛-报名系统
# Swagger： 蓝桥杯报名类接口，蓝桥杯赛事管理累接口

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit


class BBCSignUp(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(BBCSignUp, self).__init__(api_root_url, **kwargs)

    # 提交报名信息
    # code 000001
    # data{
    #     "id": 20
    # }'''
    def submit_registration_information(self):
        self.req_method = 'POST'
        self.req_url = '/bbcEnterName/submitRegistrationInformation'
        self.req_body = {
            "address": "asctrio地址2",
            "areaCode": "86",
            "city": "",
            "code": "12",
            "dateOfBirth": "2011年01月01日",
            "gender": "M",
            "guardian": "asc爸爸姓名2",
            "idNumber": "441481201101010014",
            "idPhoto": "https://res.miaocode.com/competition/files/1625672893591.jpeg",
            "mailbox": "lensaclrtn@gmail.com",
            "matchId": "40",
            "participants": "asc儿子姓名2",
            "phone": "18502937862",
            "province": "北京市",
            "provinceAndCity": "北京市,东城区",
            "region": "东城区",
            "school": "asctrio学校",
            "typeOfCertificate": "IDCARD"
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('h5'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result
        # 响应

    # 创建订单并返回支付所需参数，订单不包含课程
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
    def create_order(self):
        self.req_method = 'POST'
        self.req_url = '/bbcEnterName/createOrder'
        self.req_body = {
            "id": "20",
            "payType": "ALI",
            "userId": "282514",
            "forwordUrl": "https:\/\/sit.miaocode.com\/h5competition\/pay?id=20&matchId=21",
            "payStyle": "WAP"
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 创建订单并返回支付所需参数，订单不包含课程
    # code 000001
    # data{
    #     "status": "NOT_CREATED"
    # }
    def get_order_status(self):
        self.req_method = 'GET'
        self.req_url = '/bbcEnterName/getOrderStatus'
        self.req_body = {
            "id": 20
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 审核通过不通过
    def audit(self):
        self.req_method = 'POST'
        self.req_url = '/matchManager/audit'
        self.req_body = {
            'enable': '1',  # 1:通过/0:不通过
            'failReason': '',  # 不通过原因
            'id': '12'  # 报名记录id
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 启用赛事
    def enable_match(self, match_id):
        self.req_method = 'POST'
        self.req_url = '/matchManager/enableMatch'
        self.req_body = {
            'enable': 1,
            'id': match_id,  # 赛事id
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

    # 禁用赛事
    def unable_match(self, match_id):
        self.req_method = 'POST'
        self.req_url = '/matchManager/enableMatch'
        self.req_body = {
            'enable': 0,
            'id': match_id,  # 赛事id
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

    # 保存赛事
    def save_match(self, name, expense, startTime, endTime, type, headImg, detailImgList):
        self.req_method = 'POST'
        self.req_url = '/matchManager/saveMatch'
        self.req_body = {
            "name": name,
            "expense": expense,
            "startTime": startTime,
            "endTime": endTime,
            "type": type,  # Miaocode, Python
            "headImg": headImg,
            "detailImgList": detailImgList,
            # "detailImgList": [
            #     "https://res.miaocode.com/ad940da1-479e-419e-a783-05a59fb117b1.jpg",
            #     "https://res.miaocode.com/be06f7e9-4469-4795-9aad-7a67d4ad1191.JPG",
            #     "https://res.miaocode.com/ea0f4a33-756e-4bec-b600-e8fd331be652.jpg"
            # ]
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_kit.result_check(result)
        return result


bbc_signUp = BBCSignUp(common_kit.env('BASE_URL_CORE'))

if __name__ == '__main__':
    bbc_signUp.save_match()
    # bbc_signUp.enable_match(1, 24)
