# coding     : utf-8
# @Time      : 2021/4/12 下午6:09
from base.base_result import BaseResult
from uoactivity.competition_pk import competiiton_enter
from util import auth


# 提交报名信息
def submit_enter_name_info(
        competitionId, age, countryCode, phone,
        fullName, gender, certificateType, idNumber,
):
    result = BaseResult()
    req_data = {
        "age": age,
        "countryCode": countryCode,
        "phone": phone,
        "fullName": fullName,
        "gender": gender,
        "certificateType": certificateType,
        "idNumber": idNumber,
        "competitionId": competitionId,
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    res = competiiton_enter.submit_enter_name_info(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200 and res.json()['success'] is True:
        result.status = True
    result.response = res


# 作品点赞
def works_like(param1):
    result = BaseResult()
    req_data = {
        "id": param1,
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = competiiton_enter.works_like(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200 and res.json()['success'] is True:
        result.status = True
    result.response = res


if __name__ == '__main__':
    # submit_enter_name_info('66', 8, '86', '18659107886', '随便用', 'M', "IDCARD", '441481199407171234')
    submit_enter_name_info('66', 9, '86', '18989750002', 'z最终版', 'M', "IDCARD", '441481199407175678')
    # submit_enter_name_info('65', 7, '86', '18666024993', '签约客', 'M', "IDCARD", '441481199407173333')
