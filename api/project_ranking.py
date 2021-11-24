# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# CRM-活动管理-作品排名活动 gz-activity

from base.base_request import BaseRequest
from data_util import data_pool
from util import assert_util
from util import common_util


class ProjectRanking(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(ProjectRanking, self).__init__(root_url, **kwargs)

    # 新建活动
    def save_activity(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/projectActivityManage/saveActivity'
        self.req_cookies = {
            # "token": "accoundPhonetoken0f77f84d-e07f-4004-af15-33018be469a1",
            "api_account_token": "api_account_token_AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93",
        }
        self.req_body = kwargs
        result = self.request(
            method=self.req_method, url=self.req_url, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 更新活动 启用状态
    def update_status(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/projectActivityManage/updateStatus'
        self.req_body = kwargs
        self.req_cookies = {
            # "token": "accoundPhonetoken0f77f84d-e07f-4004-af15-33018be469a1",
            "api_account_token": "api_account_token_AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93",
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result


project_ranking = ProjectRanking(common_util.env('DOMAIN_GZ') + '/gzactivity')

if __name__ == '__main__':
    # 活动启用
    kwargs2 = data_pool.supply("project_ranking_data.yml", 'update_status')[0]
    kwargs2['id'] = 74
    kwargs2['status'] = 1  # 1启用 0禁用
    res2 = project_ranking.update_status(**kwargs2)
    assert res2.status is True
