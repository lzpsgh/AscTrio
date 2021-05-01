# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 上午9:15
# 模版文件，仅供参考，无法执行


from api.leads import leads
from util import auth
from util import common


def booking_demo():
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        'phone': '1888888888',
        'childName': 'child8888',
        'childSex': 'M',
        'childAge': 10,
        'countryCode': 86,
        'address': 'addr_1234',
        'channel': 'testtest'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    result = leads.booking_demo(data=req_data, headers=req_headers, cookies=req_cookies)
    common.result_check(result)
    return result


if __name__ == '__main__':
    booking_demo()
