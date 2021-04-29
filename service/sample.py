# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 上午9:15
# 模版文件，仅供参考，无法执行


from api.sample import sample
from base.base_result import BaseResult
from util import auth
from util import common


def req_get_with_param(param1):
    result = BaseResult()
    req_data = {
        "param": param1
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': '323697D32350F26119B35809323E26EC',
        'token': 'api_token_CBA4A3006A8ABC706F98A2B6F8892CC2',
    }
    res = sample.req_get_with_param(params=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


def req_post_old():
    result = BaseResult()
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "262728293031",
        "captcha": '1'
    }
    req_headers = {
        # "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
    }
    req_cookies = {
        'JSESSIONID': '323697D32350F26119B35809323E26EC',
        'token': 'api_token_CBA4A3006A8ABC706F98A2B6F8892CC2',
    }
    res = sample.req_post(data=req_data, headers=req_headers, cookies=req_cookies)
    # res = sample.req_post(json=req_data)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


def req_post():
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "262728293031",
        "captcha": '1'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = sample.req_post(params=req_data, headers=req_headers)
    common.result_check(result)

    core_jsessionid = result.rsp.cookies["JSESSIONID"]
    auth.set_cookie('crm', core_jsessionid)
    print(core_jsessionid)

    return result


if __name__ == '__main__':
    # req_get("sadfasdf")
    req_post()
