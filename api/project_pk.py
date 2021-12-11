#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 下午2:18

from base.base_request import BaseRequest
from faker_util import fakerist
from mysql_util import mysqler
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool
from util.log_util import logger


class ProjectPK(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(ProjectPK, self).__init__(root_url, **kwargs)

    def test(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/account/submit'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 提交报名信息
    def submit_enter_name_info(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/submitEnterNameInfo'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 作品点赞
    def works_like(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/worksLike'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 保存赛事
    def save_competition(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/competitionManager/saveCompetition'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        cid = mysqler.query('select id FROM competition where competition_name = \'赛事h5跳转\' ')[0][0]
        if cid is not None:
            print(cid)
        return result

    # 删除评分维度
    def del_scoring_dimension_by_id(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/delScoringDimensionById'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # id获取评分维度
    def get_scoring_dimension_by_id(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/getScoringDimensionById'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 获取评分维度列表
    def get_scoring_dimension_list(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/getScoringDimensionList'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 保存评分维度-修改
    def edit_scoring_dimension(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/saveScoringDimension'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        finvalue = mysqler.query('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 2:
            logger.info(finvalue)
        return result

    # 保存评分维度-新增
    def add_scoring_dimension(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/saveScoringDimension'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        return result


project_pk = ProjectPK(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    kwargs = data_pool.supply('project_pk_data.yml', 'add_scoring_dimension')[0]
    kwargs['name'] = fakerist.word()
    res1 = project_pk.add_scoring_dimension(**kwargs)
    assert_util.result_check(res1)
    assert res1.status is True
