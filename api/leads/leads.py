# coding     : utf-8
# @Time      : 2021/4/30 下午2:12

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class Leads(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Leads, self).__init__(api_root_url, **kwargs)

    # 新建预约试听课leads,官网
    def booking_demo(self, phone):
        self.req_method = 'POST'
        self.req_url = '/course/bookingDemo'
        self.req_body = {
            "isOnlyLeads": False,
            'phone': phone,
            'countryCode': 86,
            'smsCode': '123456',
            'childGrade': '五年级',
            'childName': 'child8888',
            'channel': 'official'
        }
        # self.req_body = datajson
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body
        )
        asserter.result_check(result)
        return result


leads = Leads(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    # data = {
    #     "phone": "18877771650",
    #     "code": "123456",
    #     "userGrade": '小学四年级',
    # }
    # leads.booking_demo(data)
    mphone = '18888655443'
    leads.booking_demo(mphone)
