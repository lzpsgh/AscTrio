# coding     : utf-8
# @Time      : 2021/4/12 下午6:09
from api.competition_pk.competition_enter import competiiton_enter
from core.result_base import ResultBase
from util import auth


# 提交报名信息
def submit_enter_name_info(
        age, countryCode, phone, fullName, gender, certificateType, idNumber,
        competitionId, competitionName):
    result = ResultBase()
    req_data = {
        "age": age,
        "countryCode": countryCode,
        "phone": phone,
        "fullName": fullName,
        "gender": gender,
        "certificateType": certificateType,
        "idNumber": idNumber,
        "competitionId": competitionId,
        "competitionName": competitionName
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('web'),
    }
    res = competiiton_enter.submit_enter_name_info(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200 and res.json()['success'] is True:
        result.status = True
    result.response = res


if __name__ == '__main__':
    submit_enter_name_info(6, '86', '18659107886', 'asdfa', 'M', "IDCARD", '452352345234',
                           '46', 'asctrio046')
