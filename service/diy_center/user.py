# coding     : utf-8
# @Time      : 2021/4/25 下午10:34

from api.diy_center.user import user
from base.base_result import BaseResult
from util import auth


def send_sms(param1):
    result = BaseResult()
    req_data = {
        "phone": param1
    }
    req_headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    res = user.send_sms(params=req_data, headers=req_headers)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


def register(param1):
    result = BaseResult()
    req_data = {
        "phone": param1,
        "userPassword": "262728293031",
        "code": '123456'
    }
    req_headers = {
        # "Host": "sit.miaocode.com",
        # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
        "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryJ8fdxxspLpykHU8t'
    }

    res = user.register(params=req_data, headers=req_headers)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["code"] == '000003':
            result.status = True
    else:
        print(status_code)
    result.response = res


def login(param1):

    req_data = {
        "phone": param1,
        'userPassword': '262728293031'
    }
    req_headers = {
        "Host": "api-sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    res = user.login(params=req_data, headers=req_headers)

    status_code = res.status_code
    resjson = res.json()
    result = BaseResult()
    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
            gz_token = res.cookies['token']
            auth.set_cookie('gz', gz_token)
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':

    # 用新用户
    # send_sms(user_phone)
    # register(user_phone)
    # 用老用户
    login('18989750002')  # registertokenc0ef1553-df12-461d-93fe-b845fcaf00f9
