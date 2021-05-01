# coding     : utf-8
# @Time      : 2021/4/18 上午2:29
from api.user.user import user
from util import auth
from util import common
from util import tmtask
from util.mysql_operate import db


# 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）
def send_sms():
    req_data = {
        "phone": "18899112648"
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    result = user.send_sms(params=req_data, headers=req_headers)
    common.result_check(result)
    return result


# 获取手机验证码（量多应该抽出来放到/user/ccbb文件夹）
def send_sms2():
    req_data = {
        "phone": "18899112648",
        't': common.get_timestamp(),
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    result = user.send_sms2(params=req_data, headers=req_headers, cookies=req_cookies)
    common.result_check(result)
    return result


# 官网注册-数理思维
# 比官网多传3个值，分别是 cityDesc，channel，和grade
def register_mathematics():
    req_data = {
        "phone": "18899112648",
        "code": "123456",
        "cityDesc": '天津市,河东区',
        "channel": 'tMathOffice',
        "grade": '小学一年级',
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
    req_data = {
        "code": code,
        "phone": phone
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('h5'),
    }
    result = user.login_and_register(params=req_data, cookies=req_cookies)
    common.result_check(result)
    return result


# 官网密码登录
def login_web_pwd(phone, user_password, t):
    req_data = {
        "phone": phone,
        "userPassword": user_password,
        't': common.get_timestamp(),
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    result = user.login(params=req_data, cookies=req_cookies)
    common.result_check(result)
    return result


# 官网验证码登录
def login_web_vfcode(phone):
    req_data = {
        "phone": phone,
        "code": 123456,
        't': common.get_timestamp(),
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    result = user.phone_login(params=req_data, cookies=req_cookies)
    common.result_check(result)
    return result


def modify_users_owner():
    sql_query_userid = "select id from activityuser where phone = "
    sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "
    phone = '13333333333'
    req_data = {
        'salerIds': '889',  # cc倪旭(新)  ccxu.ni01@miaocode.com
        'userIds': db.select_db(sql_query_userid + phone)
        # 'userIds': 123333,
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    result = user.send_sms(params=req_data, headers=req_headers, cookies=req_cookies)
    common.result_check(result)
    return result


if __name__ == '__main__':
    # login_h5('123456', '18659107886')
    # login_web('18659107886', '262728293031', "1619155530916")  # 原始 7BBD47F6250C1D68129A3556921C27DF
    # login_web('18989750002', '262728293031', "1619155510916")  # 羽扇 A4FDD2752DE0E72D432D955AF9A4830E
    # login_web('18666024993', '262728293031', "1619155530916")  #签约 6BFF58CB26FAFDF7BFFA7BC17CE02389
    # send_sms()
    # register_mathink()
    tmtask.call_method(
        '/mxcuser/common/callMethodByAnnotation?className=com.mxc.user.task.LeadsTask&methodName=syncLeadsSignTask')
