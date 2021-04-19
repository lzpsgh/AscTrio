# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 下午1:39

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE

"""
作品PK-赛事管理
"""


class CompetitionManage(BaseRequest):
    def __init__(self, api_root_url, **kwargs):
        super(CompetitionManage, self).__init__(api_root_url, **kwargs)

    # 删除赛事
    def del_competition_by_id(self, **kwargs):
        return self.request("POST", "/competitionManager/delCompetitionById", **kwargs)

    # 启用/禁用
    def enabled_state(self, **kwargs):
        return self.request("POST", "/competitionManager/enabledState", **kwargs)

    # 获取评委列表
    def get_account_list(self, **kwargs):
        return self.request("GET", "/competitionManager/getAccountList", **kwargs)

    # 赛事详情
    def get_competition_by_id(self, **kwargs):
        return self.request("GET", "/competitionManager/getCompetitionById", **kwargs)

    # 获取赛事列表
    def get_competition_list(self, **kwargs):
        return self.request("GET", "/competitionManager/getCompetitionList", **kwargs)

    # 模糊查询所有赛事名称
    def get_competition_names(self, **kwargs):
        return self.request("GET", "/competitionManager/getCompetitionNames", **kwargs)

    # 上一个/下一个审核记录
    def get_next_registration_record(self, **kwargs):
        return self.request("GET", "/competitionManager/getNextRegistrationRecord", **kwargs)

    # 获取报名记录
    def get_registration_record_list(self, **kwargs):
        return self.request("GET", "/competitionManager/getRegistrationRecordList", **kwargs)

    # 报名审核
    def registration_review(self, **kwargs):
        return self.request("POST", "/competitionManager/registrationReview", **kwargs)

    # 保存赛事
    def save_competition(self, **kwargs):
        return self.request("POST", "/competitionManager/saveCompetition", **kwargs)


competition_manage = CompetitionManage(api_root_url)
