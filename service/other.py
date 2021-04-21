# coding     : utf-8
# @Time      : 2021/4/20 下午3:00

from api.other import other
from base.base_result import BaseResult
from util import auth


def send_paysucmsg_fast(phone):
    result = BaseResult()
    req_data = {
        "phone": phone
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = other.send_paysucmsg_fast(params=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


def add_sprite():
    result = BaseResult()
    req_data = {
        'isCommon': False,
        'price': 8,
        'spriteName': '环保比赛-孩子8',
        'dataURL': 'https://res.miaocode.com/6ff0d74b-29e6-424f-8870-a08a6f58b995.png'
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = other.add_sprite(data=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


def add_stage():
    result = BaseResult()
    req_data = {
        'isCommon': False,
        'comment': 'asdf',
        'price': 0,
        'stageName': '环保比赛-新几4',
        'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
    }
    req_headers = {
        "Host": "sit.miaocode.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = other.add_stage(data=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':
    # send_paysucmsg_fast("18899758128")
    add_stage()
