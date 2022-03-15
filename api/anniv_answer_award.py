#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 下午6:36

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class AnnivAnswerAward(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(AnnivAnswerAward, self).__init__(root_url, **kwargs)

    # 保存活动
    def save(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/lottery/save'
        self.req_body = kwargs
        self.req_cookies = {
            # 'api_account_token': auth_util.get_token('crm', 'api_account_token'),
            'api_account_token': 'api_account_token_AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93'
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 抽奖活动列表
    def get_list(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/lottery/getList'
        self.req_body = {
            'pageNum': 10,
            'pageSize': 1
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 抽奖活动详情
    def get_by_id(self, id):
        self.req_method = 'GET'
        self.req_url = '/lottery/getById'
        self.req_body = {
            'id': id
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 活动上架 id status
    def update_status(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/lottery/updateStatus'
        self.req_body = kwargs
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 中奖记录
    def get_prize_record(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/lottery/getPrizeRecord'
        self.req_body = {
            'pageNum': 10,
            'pageSize': 1,
            'id': 3
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 抽奖首页数据
    def get_user_lottery(self, id):
        self.req_method = 'GET'
        self.req_url = '/lottery/getUserLottery'
        self.req_body = {
            'id': id
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 抽奖动作
    def start(self, id):
        self.req_method = 'GET'
        self.req_url = '/lottery/start'
        self.req_body = {
            'id': id
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 保存收获地址
    # "consignee":,
    # "consigneePhone",
    # "province",
    # "city",
    # "region",
    # "deliveryAddress",
    # "recordId"
    def save_address(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/lottery/saveAddress'
        self.req_body = kwargs
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 收货地址回显
    def get_address_by_record_id(self, id):
        self.req_method = 'GET'
        self.req_url = '/lottery/getAddressByRecordId'
        self.req_body = {
            'recordId': id
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 中奖记录h5
    # id,userId
    def get_user_prize_record(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/lottery/getUserPrizeRecord'
        self.req_body = kwargs
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 导出中奖记录
    # id,userId
    def export_activity_record(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/lottery/activityRecord'
        self.req_body = kwargs
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


anniv_answer_award = AnnivAnswerAward(common_util.env('DOMAIN_GZ') + '/gzactivity')

if __name__ == '__main__':
    kwargs = data_pool.supply('anniv_answer_award_data.yml', 'save_normal')[0]
    res1 = anniv_answer_award.save(**kwargs)
    assert res1.status is True
