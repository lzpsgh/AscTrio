# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 下午1:39

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class CompetitionEnter(BaseRequest):
    def __init__(self, api_root_url, **kwargs):
        super(CompetitionEnter, self).__init__(api_root_url, **kwargs)

    # 提交报名信息
    def submit_enter_name_info(self, competitionId, age, countryCode, phone,
                               fullName, gender, certificateType, idNumber):
        self.req_method = 'POST'
        self.req_url = '/competitionEnterName/submitEnterNameInfo'
        self.req_body = {
            "age": age,
            "countryCode": countryCode,
            "phone": phone,
            "fullName": fullName,
            "gender": gender,
            "certificateType": certificateType,
            "idNumber": idNumber,
            "competitionId": competitionId,
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 作品点赞
    def works_like(self, param1):
        self.req_method = 'POST'
        self.req_url = '/competitionEnterName/worksLike'
        self.req_body = {
            "id": param1
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result


competition_enter = CompetitionEnter(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    # competition_enter.submit_enter_name_info('66', 8, '86', '18659107886', '随便用', 'M', "IDCARD", '441481199407171234')
    competition_enter.submit_enter_name_info('66', 9, '86', '18989750002', 'z最终版', 'M', "IDCARD", '441481199407175678')
    # competition_enter.submit_enter_name_info('65', 7, '86', '18666024993', '签约客', 'M', "IDCARD", '441481199407173333')
