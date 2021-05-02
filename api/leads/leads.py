# coding     : utf-8
# @Time      : 2021/4/30 下午2:12

from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common


class Leads(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Leads, self).__init__(api_root_url, **kwargs)

    # 新建预约试听课leads
    def booking_demo(self):
        self.req_method = 'POST'
        self.req_url = '/course/bookingDemo'
        self.req_body = {
            "accountName": "zhaopeng.li@miaocode.com",
            'phone': '1888888888',
            'childName': 'child8888',
            'childSex': 'M',
            'childAge': 10,
            'countryCode': 86,
            'address': 'addr_1234',
            'channel': 'testtest'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        common.result_check(result)
        return result


leads = Leads(envar.BASE_URL_CORE)

if __name__ == '__main__':
    leads.booking_demo()
