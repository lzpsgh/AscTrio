# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:56

from api.account import account
from core.result_base import ResultBase
from util import auth


def crm_login(account_name="zhaopeng.li@miaocode.com",
              account_password='262728293031',
              captcha=1):
    result = ResultBase()
    req_data = {
        "accountName": account_name,
        "accountPassword": account_password,
        "captcha": captcha
    }
    res = account.login(params=req_data)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
            print(resjson["data"]["token"])
            print(resjson["data"]["id"])
            print(res.headers['Set-Cookie'])
            # ymlfile.persist()
    else:
        print(status_code)

    result.response = res


# todo 处理太粗糙
def crm_login_with_mm():
    result = ResultBase()
    req_data = {
        "accountName": "zhaopeng.li@miaocode.com",
        "accountPassword": "262728293031",
        "captcha": '1'
    }
    res = account.login(params=req_data)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
            core_jsessionid = res.cookies["JSESSIONID"]
            auth.set_cookie('crm', core_jsessionid)
            print(core_jsessionid)
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':
    crm_login_with_mm()
