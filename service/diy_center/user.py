# coding     : utf-8
# @Time      : 2021/4/25 下午10:34

from api.diy_center.user import user
from base.base_result import BaseResult
from util.logger import logger

user_phone = 18659107886


def send_sms(param1):
    result = BaseResult()
    req_data = {
        "phone": param1
    }
    req_headers = {
        # "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': '323697D32350F26119B35809323E26EC',
        'token': 'api_token_CBA4A3006A8ABC706F98A2B6F8892CC2',
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


# 注册用boundary，得引入第三方库来生成
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
    req_cookies = {
        'JSESSIONID': '323697D32350F26119B35809323E26EC',
        'token': 'api_token_CBA4A3006A8ABC706F98A2B6F8892CC2',
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
    result = BaseResult()
    req_data = {
        "phone": param1,
        'userPassword': '262728293031'
    }
    req_headers = {
        "Host": "api-sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': '323697D32350F26119B35809323E26EC',
        'token': 'api_token_CBA4A3006A8ABC706F98A2B6F8892CC2',
    }
    res = user.login(params=req_data, headers=req_headers)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
            logger.info(res.cookies['token'])
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':

    # 用新用户
    # send_sms(user_phone)
    # register(user_phone)
    # 用老用户
    login(user_phone)  # registertokenc0ef1553-df12-461d-93fe-b845fcaf00f9
