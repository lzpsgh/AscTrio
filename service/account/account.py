# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:56

from api.account.account import account
from base.base_result import BaseResult
from util import auth
from util import common
from util.logger import logger


def crm_login(account_name="zhaopeng.li@miaocode.com", account_password='262728293031', captcha=1):
    result = BaseResult()
    req_data = {
        "accountName": account_name,
        "accountPassword": account_password,
        "captcha": captcha
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    res = account.login(params=req_data, headers=req_headers)

    common.rsp_check()
    status_code = res.status_code
    resjson = res.json()
    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
            print(resjson["data"]["token"])
            print(resjson["data"]["id"])
            print(res.headers['Set-Cookie'])

    else:
        print(status_code)


def crm_login_with_mm():
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "262728293031",
        "captcha": '1'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = account.login(params=req_data, headers=req_headers)
    common.result_check(result)

    core_jsessionid = result.rsp.cookies["JSESSIONID"]
    auth.set_cookie('crm', core_jsessionid)
    logger.info(core_jsessionid)
    return result


if __name__ == '__main__':
    crm_login_with_mm()
