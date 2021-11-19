# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考，无法执行

from functools import wraps

import task_util
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

    # 作品排名活动优化
    def save_activity(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzactivity/projectActivityManage/saveActivity'
        # self.req_headers = {
        #     "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        # }
        self.req_cookies = {
            "token": "accoundPhonetoken0f77f84d-e07f-4004-af15-33018be469a1",
            "api_account_token": "api_account_token_AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93",
        }
        #
        self.req_body = kwargs
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 期中期末新增考试
    def add_exam(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/exam/examination/add'
        # self.req_headers = {
        #     "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        # }
        self.req_cookies = {
            "token": "api_token_78FFF87040F1D73F58CE527C892B5FD4",
            "api_account_token": "api_account_token_AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93",
            "SESSION": 'YjgyNWI5NjgtODY2Mi00MDQ5LWE1ODctMmQzN2FjZmRmOWEx'
        }
        self.req_body = kwargs
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result


other = Other(common_util.env('DOMAIN_GZ') + '/gzexam')

if __name__ == '__main__':
    # test_data1 = {
    #     "activityName": "冒烟66",
    #     "activeObject": 1,
    #     "participationAward": 66,
    #     "channelCode": "testtesttest",
    #     "startTime": "2021-10-24 00:00:01",
    #     "endTime": "2021-10-29 00:01:00",
    #     "chooseStartTime": "2020-11-09 00:00:00",
    #     "chooseEndTime": "2020-11-16 00:00:00",
    #     "headImg": "https://res.miaocode.com/f776b2b4-b2c9-4e9f-ba50-4bb6d79d89ce.jpeg",
    #     "howToPlay": 1,
    #     "invitationButtonColor": "#f8da73",
    #     "leaderboardColor": "#f8da73",
    #     "shareDesc": "测试活动作品分享描述文案常常吃",
    #     "shareIcon": "https://res.miaocode.com/e7b1abf7-8819-40cc-9b28-cf9410146170.png",
    #     "shareTitle": "测试活动作品分享标题",
    #     "frontShareDesc": "测试活动首页分享描述文案常常吃",
    #     "frontShareIcon": "https://res.miaocode.com/49d91132-0de2-475c-ba09-52b7c4697877.jpeg",
    #     "frontShareTitle": "测试活动首页分享标题",
    #     "posterImgList": ["https://res.miaocode.com/3026ddcf-b327-4c9a-b43f-f026f2152cdd.jpeg"],
    #     "detailImgList": ["https://res.miaocode.com/cf3cf6ec-8150-4f6a-ba28-f41bf9922499.jpeg"],
    #     "rewardList": [
    #         {
    #             "rankingAbove": 1,
    #             "pointsReward": 10,
    #             "gradient": 1,
    #             "isActive": False
    #         }
    #     ]
    # }
    # other.add_exam(**test_data1)
    #

    # kwargs = data_pool.supply('other.yml', 'add_exam')[0]
    # kwargs['examName'] = '中文' + fakerist.word()
    # kwargs['englishExamName'] = 'eng_' + fakerist.numerify()
    # kwargs['timeInterval'][0] = '2020-12-09 00:00:00'
    # kwargs['timeInterval'][1] = '2021-05-25 22:00:00'
    # other.add_exam(**kwargs)

    task_util.call_method('https://api-sit.miaocode.com/api/gzexam/teacherexam/notice?date=2020-12-10&sendMsg=false')

    # other.func2(1, 2, a=3, b=4)
    # print(f'装饰外模块名:{other.__module__.__}')
    # print(f'装饰外函数名:{other.func2.__name__}')
    # other.upload_material('pwd')
