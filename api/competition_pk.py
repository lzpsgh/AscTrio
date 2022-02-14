#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 下午1:52

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.log_util import logger
from util.mysql_util import mysqler


class CompetitionPK(BaseRequest):
    def __init__(self, api_root_url, **kwargs):
        super(CompetitionPK, self).__init__(api_root_url, **kwargs)

    # 作品点赞
    def works_like(self, param1):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/worksLike'
        self.req_body = {
            "id": param1
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


    # 启用/禁用
    # def enabled_state(self, **kwargs):
    #     return self.request("POST", "/competitionManager/enabledState", **kwargs)
    # 报名审核
    # def registration_review(self, **kwargs):
    #     return self.request("POST", "/competitionManager/registrationReview", **kwargs)

    # 删除评分维度
    def del_scoring_dimension_by_id(self, sd_id):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/delScoringDimensionById'
        self.req_body = {
            "id": sd_id
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # id获取评分维度
    def get_scoring_dimension_by_id(self, sd_id):
        self.req_method = 'GET'
        self.req_url = '/core/scoringDimension/getScoringDimensionById'
        self.req_body = {
            "id": sd_id
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 获取评分维度列表
    def get_scoring_dimension_list(self):
        self.req_method = 'GET'
        self.req_url = '/core/scoringDimension/getScoringDimensionList'
        self.req_body = {
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 保存评分维度-修改
    def save_scoring_dimension(self, sd_id, min_points, max_points, name):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/saveScoringDimension'
        self.req_body = {
            "id": sd_id,
            "maxPoints": max_points,
            "minPoints": min_points,
            "name": name
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        finvalue = mysqler.query('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 2:
            logger.info(finvalue)
        return result

    # 保存赛事
    def save_competition(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/competitionManager/saveCompetition'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 提交报名信息
    def submit_enter_name_info(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/submitEnterNameInfo'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result


cmpttn_pk = CompetitionPK(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    # competition_enter.submit_enter_name_info('66', 8, '86', '18659107886', '随便用', 'M', "IDCARD", '441481199407171234')
    # cmpttn_pk.submit_enter_name_info('67', 9, '86', '18659107886', 'z最终版', 'M', "IDCARD", '441481199407175678')
    # competition_enter.submit_enter_name_info('65', 7, '86', '18666024993', '签约客', 'M', "IDCARD", '441481199407173333')
    pass
