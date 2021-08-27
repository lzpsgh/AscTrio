#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 上午11:02


from base.base_request import BaseRequest
from util import assert_util
from util import common_util


class TeachersDayVote(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(TeachersDayVote, self).__init__(root_url, **kwargs)

    # 拉票主页
    def get_canvass_info(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/user/activity/canvass/getCanvassInfo'
        self.req_body = kwargs
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 学员创建拉票
    def save_user_canvass(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/user/activity/canvass/saveUserCanvass'
        self.req_body = kwargs
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 投票信息
    def get_vote_info(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/teacherVote/info'
        self.req_body = kwargs
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 用户投票
    def vote(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/teacherVote/vote'
        self.req_body = kwargs
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 学员的用户投票详情
    def get_user_canvass_dto_list(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/user/activity/canvass/getUserCanvassDtoList'
        self.req_body = kwargs
        result = self.x_request()
        assert_util.result_check(result)
        return result


teachers_day_vote = TeachersDayVote(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    teachers_day_vote.save_match()
