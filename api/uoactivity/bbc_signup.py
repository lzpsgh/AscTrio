#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 下午4:22

# 模块名称：蓝桥杯编程比赛-报名系统
# Swagger： 蓝桥杯报名类接口，蓝桥杯赛事管理累接口

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class BBCSignUp(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(BBCSignUp, self).__init__(api_root_url, **kwargs)

    # 提交报名信息
    def submit_registration_information(self):
        self.req_method = 'POST'
        self.req_url = '/bbcEnterName/submitRegistrationInformation'
        self.req_body = {
            "address": "string",
            "areaCode": "string",
            "city": "string",
            "code": "string",
            "dateOfBirth": "2021-07-01T09:47:12.201Z",
            "gender": "string",
            "guardian": "string",
            "id": 0,
            "idNumber": "string",
            "idPhoto": "string",
            "mailbox": "string",
            "matchId": 0,
            "participants": "string",
            "phone": "string",
            "province": "string",
            "region": "string",
            "school": "string",
            "typeOfCertificate": "string"
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 创建订单并返回支付所需参数，订单不包含课程
    def create_order(self):
        self.req_method = 'POST'
        self.req_url = '/bbcEnterName/createOrder'
        self.req_body = {
            "forwordUrl": "string",
            "id": 0,
            "payStyle": "string",
            "payType": "string",
            "remark": "string",
            "userId": 0
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 审核通过不通过
    def enable_match(self):
        self.req_method = 'POST'
        self.req_url = '/matchManager/audit'
        self.req_body = {
            'enable': '1',  # 1:通过/0:不通过
            'failReason': '',  # 不通过原因
            'id': '12'  # 报名记录id
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 启用禁用赛事
    def enable_match(self, is_enable, match_id):
        self.req_method = 'POST'
        self.req_url = '/matchManager/enableMatch'
        self.req_body = {
            'enable': is_enable,  # 1:启用/0:禁用
            'id': match_id,  # 赛事id
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result

    # 保存赛事
    def save_match(self):
        self.req_method = 'POST'
        self.req_url = '/matchManager/saveMatch'
        self.req_body = {
            "name": "Asctrio0006蓝桥杯赛事",
            "expense": 300,
            "startTime": "2021-07-11 00:00:00",
            "endTime": "2021-08-01 00:00:00",
            "type": "Miaocode",  # Python
            "headImg": "https://res.miaocode.com/cd589a1b-9ea9-4d53-8b85-ab9fe1488a31.JPG",
            "detailImgList": [
                "https://res.miaocode.com/ad940da1-479e-419e-a783-05a59fb117b1.jpg",
                "https://res.miaocode.com/be06f7e9-4469-4795-9aad-7a67d4ad1191.JPG",
                "https://res.miaocode.com/ea0f4a33-756e-4bec-b600-e8fd331be652.jpg"
            ]
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        asserter.result_check(result)
        return result


bbc_signUp = BBCSignUp(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    bbc_signUp.save_match()
    bbc_signUp.enable_match(1, 22)
