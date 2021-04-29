# coding     : utf-8
# @Time      : 2021/4/18 上午2:29
from api.user.user import user
from base.base_result import BaseResult
from util import auth
from util import common


# 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）
def send_sms():
    req_data = {
        "phone": "18899112667"
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = user.send_sms(params=req_data, headers=req_headers)
    common.result_check(result)

    return result


# 官网注册-数理思维
# 比官网多传3个值，分别是 cityDesc，channel，和grade
def register_mathink():
    req_data = {
        "phone": "18899112667",
        "code": "123456",
        # "userGrade": '小学四年级',
        "cityDesc": 'pc',
        "channel": '',
        "grade": ''
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = user.register(data=req_data, headers=req_headers)
    common.result_check(result)

    return result

# 官网注册-常规
def register():
    req_data = {
        "phone": "18899112667",
        "code": "123456",
        "userGrade": '小学四年级',
        # "origin": 'pc'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = user.register(data=req_data, headers=req_headers)
    common.result_check(result)

    return result


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


# 官网登录
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
        core_jsessionid = res.cookies["JSESSIONID"]
        auth.set_cookie('web', core_jsessionid)
    result.response = res


if __name__ == '__main__':
    # login_h5('123456', '18659107886')
    # login_web('18659107886', '262728293031', "1619155530916")  # 原始 7BBD47F6250C1D68129A3556921C27DF
    # login_web('18989750002', '262728293031', "1619155510916")  # 羽扇 A4FDD2752DE0E72D432D955AF9A4830E
    # login_web('18666024993', '262728293031', "1619155530916")  #签约 6BFF58CB26FAFDF7BFFA7BC17CE02389
    register()
    # send_sms()
