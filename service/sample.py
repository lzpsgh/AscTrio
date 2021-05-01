# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 上午9:15
# 模版文件，仅供参考，无法执行
from api.sample import sample
from util import auth
from util import common


def req_get(param1):
    req_data = {
        "param": param1
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    # 注意get请求要用params
    result = sample.req_get(params=req_data, headers=req_headers, cookies=req_cookies)
    common.result_check(result)


def req_post():
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "262728293031",
        "captcha": '1'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    # 注意post请求要用data或者json
    result = sample.req_post(data=req_data, headers=req_headers, cookies=req_cookies)
    common.result_check(result)

    core_jsessionid = result.rsp.cookies["JSESSIONID"]
    auth.set_cookie('crm', core_jsessionid)
    print(core_jsessionid)

    return result


if __name__ == '__main__':
    # req_get("sadfasdf")
    req_post()
