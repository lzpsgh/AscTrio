# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 下午1:30

from base.base_request import BaseRequest
from util import auth
from util import common
from util.logger import logger
from util.mysql_operate import db


class ScoringDimension(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(ScoringDimension, self).__init__(api_root_url, **kwargs)

    # 删除评分维度
    def del_scoring_dimension_by_id(self, sd_id):
        self.req_method = 'POST'
        self.req_url = '/scoringDimension/delScoringDimensionById'
        self.req_body = {
            "id": sd_id
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result

    # id获取评分维度
    def get_scoring_dimension_by_id(self):
        self.req_method = 'GET'
        self.req_url = '/scoringDimension/getScoringDimensionById'
        self.req_body = {

        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result

    # 获取评分维度列表
    def get_scoring_dimension_list(self):
        self.req_method = 'GET'
        self.req_url = '/scoringDimension/getScoringDimensionList'
        self.req_body = {
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result

    # 保存评分维度-修改
    def save_scoring_dimension(self, sd_id, min_points, max_points, name):
        self.req_method = 'POST'
        self.req_url = '/scoringDimension/saveScoringDimension'
        self.req_body = {
            "id": sd_id,
            "maxPoints": max_points,
            "minPoints": min_points,
            "name": name
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        finvalue = db.select_db('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 2:
            logger.info(finvalue)
        return result

    # 保存评分维度-新增
    def save_scoring_dimension(self, min_points, max_points, name):
        self.req_method = 'POST'
        self.req_url = '/scoringDimension/saveScoringDimension'
        self.req_body = {
            # "id": sd_id,
            "maxPoints": max_points,
            "minPoints": min_points,
            "name": name
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result


scoring_dimension = ScoringDimension(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    scoring_dimension.modify_scoring_dimension(3, 2, 30, "aaaaa")
