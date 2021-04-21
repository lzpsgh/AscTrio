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
    res = other.send_paysucmsg_fast(param=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["success"] is True:
            result.status = True
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':
    send_paysucmsg_fast("18899758128")
