# coding     : utf-8
# @Time      : 2021/4/18 上午2:29
from api.user.user import user
from base.base_result import BaseResult
from util import auth


# 官网注册
def login_web(phone, user_password, t):
    result = BaseResult()
    req_data = {
        "phone": phone,
        "userPassword": user_password,
        "t": t
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    res = user.login(params=req_data, cookies=req_cookies)

    if res.status_code == 200 and res.json()["success"] is True:
        result.status = True
        # core_jsessionid = res.cookies["JSESSIONID"]
        # auth.set_cookie('web', core_jsessionid)
    result.response = res


# h5落地页登录注册
def login_h5(code, phone):
    result = BaseResult()
    req_data = {
        "code": code,
        "phone": phone
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('h5'),
    }
    res = user.login_and_register(params=req_data, cookies=req_cookies)

    if res.status_code == 200 and res.json()["success"] is True:
        result.status = True
        core_jsessionid = res.cookies["JSESSIONID"]
        auth.set_cookie('h5', core_jsessionid)
    result.response = res


if __name__ == '__main__':
    login_web('18659107886', '262728293031', "1618716324916")
    # login_h5('123456', '18659107886')
