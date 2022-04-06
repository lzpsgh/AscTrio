#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 下午6:36

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class ZeusMongo(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(ZeusMongo, self).__init__(root_url, **kwargs)

    # 保存活动
    def save(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/lottery/save'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_token('crm', 'api_account_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 抽奖活动列表
    def get_list(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/lottery/getList'
        self.req_body = {
            'pageNum' : 10,
            'pageSize': 1
        }
        self.req_cookies = {
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


zeus_mongo = ZeusMongo(common_util.env('DOMAIN_GZ') + '/gzactivity')

# if __name__ == '__main__':
#     kwargs = data_pool.supply('anniv_answer_award_data.yml', 'save_8thank')[0]
#     res1 = zeus_mongo.save(**kwargs)
#     assert res1.status is True
