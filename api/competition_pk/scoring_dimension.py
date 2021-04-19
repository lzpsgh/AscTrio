# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 下午1:30

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE

"""
作品PK-评分维度
"""


class ScoringDimension(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(ScoringDimension, self).__init__(api_root_url, **kwargs)

    # 删除评分维度
    def del_scoring_dimension_by_id(self, **kwargs):
        return self.request("POST", "/scoringDimension/delScoringDimensionById", **kwargs)

    # id获取评分维度
    def get_scoring_dimension_by_id(self, **kwargs):
        return self.request("GET", "/scoringDimension/getScoringDimensionById", **kwargs)

    # 获取评分维度列表
    def get_scoring_dimension_list(self, **kwargs):
        return self.request("GET", "/scoringDimension/getScoringDimensionList", **kwargs)

    # 保存评分维度，新建和修改公用
    # id:int  maxPoints:int  minPoints:int  name:str
    def save_scoring_dimension(self, **kwargs):
        return self.request("POST", "/scoringDimension/saveScoringDimension", **kwargs)


scoring_dimension = ScoringDimension(api_root_url)
