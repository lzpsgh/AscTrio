# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class Other(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Other, self).__init__(api_root_url, **kwargs)

    def add_sprite(self):
        self.req_method = 'POST'
        self.req_url = '/mate/addSprite'
        self.req_body = {
            'isCommon': False,
            'price': 8,
            'spriteName': '环保比赛-孩子99',
            'dataURL': 'https://res.miaocode.com/6ff0d74b-29e6-424f-8870-a08a6f58b995.png'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result

    def add_stage(self):
        self.req_method = 'POST'
        self.req_url = '/mate/addStage'
        self.req_body = {
            'isCommon': False,
            'comment': 'asdf',
            'price': 0,
            'stageName': '环保比赛-新几44',
            'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        asserter.result_check(result)
        return result

    def upload_material(self, mate_path):
        self.req_method = 'POST'
        self.req_url = '/mate/uploadMaterial/'
        self.req_body = {
            'file': False,
            'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            file=self.req_body
        )
        asserter.result_check(result)
        return result

    # 返回符合优惠券发放规则的所有学员id，在这个学员id名单中的学员才会执行跑批脚本
    def is_fit_soprule_with_userid(self):
        self.req_method = 'GET'
        self.req_url = '/dimissionSalesStaffLeadsAllot/getSendCouponStudentId'
        # self.req_body = {
        #     'file': False,
        #     'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        # }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            file=self.req_body
        )
        asserter.result_check(result)
        return result


other = Other(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    pass
    other.upload_material('pwd')
    # other.dbf_set_time('1624204800000', '1625065200000')  # 21-30 未开始
    # other.dbf_set_time('1622476800000', '1625065200000')  # 1-30  进行中
    # other.dbf_set_time('1622476800000', '1622646000000')  # 1-2   已结束