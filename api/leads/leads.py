# coding     : utf-8
# @Time      : 2021/4/30 下午2:12

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class Leads(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Leads, self).__init__(api_root_url, **kwargs)

    # 新建预约试听课leads
    def booking_demo(self, **kwargs):
        return self.request("POST", "/course/bookingDemo", **kwargs)


leads = Leads(api_root_url)
