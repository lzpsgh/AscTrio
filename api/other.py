# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from functools import wraps

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


def decorater(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'位置参数:{args}')
        print(f'关键字参数:{kwargs}')
        res = func(*args, **kwargs)
        print(f'装饰器内函数名: {func.__name__}')
        # print(f'返回值: {res}')
        print(f'函数func所属的类: {func.__qualname__}')
        return res

    return wrapper


class Other(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Other, self).__init__(api_root_url, **kwargs)

    @decorater
    def func2(self, *args, **kwargs):
        return 'return'

    def add_sprite(self):
        self.req_method = 'POST'
        self.req_url = '/core/mate/addSprite'
        self.req_body = {
            'isCommon': False,
            'price': 8,
            'spriteName': '环保比赛-孩子99',
            'dataURL': 'https://res.miaocode.com/6ff0d74b-29e6-424f-8870-a08a6f58b995.png'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    def add_stage(self):
        self.req_method = 'POST'
        self.req_url = '/core/mate/addStage'
        self.req_body = {
            'isCommon': False,
            'comment': 'asdf',
            'price': 0,
            'stageName': '环保比赛-新几44',
            'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    def upload_material(self, mate_path):
        self.req_method = 'POST'
        self.req_url = '/core/mate/uploadMaterial/'
        self.req_body = {
            'file': False,
            'dataURL': 'https://res.miaocode.com/29fd099f-286d-42cc-99e7-44dcb330e4e6.jpg'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            file=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 返回符合优惠券发放规则的所有学员id，在这个学员id名单中的学员才会执行跑批脚本
    def is_fit_soprule_with_userid(self):
        self.req_method = 'GET'
        self.req_url = '/core/dimissionSalesStaffLeadsAllot/getSendCouponStudentId'
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            file=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 创建作品列表banner
    def save_banner(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzactivity/projectSharingActivity/saveBanner'
        # self.req_headers = {
        #     "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        # }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        self.req_body = kwargs
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result


other = Other(common_util.env('DOMAIN_GZ'))

if __name__ == '__main__':
    test_data = {
        "bannerName": "asctrio-7",
        "bannerUrl": "https://res.miaocode.com/aec680d1-4e8f-41ca-b486-b67d42cfda0f.png",
        "jumpUrl": "https://www.taobao.com",
        "sortWeight": 100,
        "takeEffectStartTime": "2021-09-29 00:00:00",
        "takeEffectEndTime": "2021-09-30 23:59:59"
    }
    other.save_banner(**test_data)

    # other.func2(1, 2, a=3, b=4)
    # print(f'装饰外模块名:{other.__module__.__}')
    # print(f'装饰外函数名:{other.func2.__name__}')
    # other.upload_material('pwd')
