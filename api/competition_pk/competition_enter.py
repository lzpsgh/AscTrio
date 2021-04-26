# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 下午1:39

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE

"""
作品PK-参赛管理
"""


class CompetitonEnter(BaseRequest):
    def __init__(self, api_root_url, **kwargs):
        super(CompetitonEnter, self).__init__(api_root_url, **kwargs)

    # 赛事详情
    def get_competition_by_id(self, **kwargs):
        return self.request("GET", "/competitionEnterName/getCompetitionById", **kwargs)

    # 赛事总览
    def get_competition_list(self, **kwargs):
        return self.request("GET", "/competitionEnterName/getCompetitionList", **kwargs)

    # 提交报名信息
    def submit_enter_name_info(self, **kwargs):
        return self.request("POST", "/competitionEnterName/submitEnterNameInfo", **kwargs)

    # 获取报名进度
    def get_registration_progress(self, **kwargs):
        return self.request("GET", "/competitionEnterName/getRegistrationProgress", **kwargs)

    # 作品点赞
    def works_like(self, **kwargs):
        return self.request("POST", "/competitionEnterName/worksLike", **kwargs)


competiiton_enter = CompetitonEnter(api_root_url)
