# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 下午5:58


from api.competition_pk.scoring_dimension import scoring_dimension
from base.base_result import BaseResult
from util import auth
from util.mysql_operate import db


# 删除评分维度
def del_scoring_dimension_by_id(sd_id):
    # 记录请求头请求体 响应头响应体
    result = BaseResult()
    req_data = {
        "id": sd_id
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = scoring_dimension.del_scoring_dimension_by_id(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        result.status = True
    result.response = res


# id获取评分维度
def get_scoring_dimension_by_id(self, **kwargs):
    pass


# 获取评分维度列表
def get_scoring_dimension_list(self, **kwargs):
    pass


# 保存评分维度，新建时不传id
def new_scoring_dimension(min_points, max_points, name):
    result = BaseResult()
    req_data = {
        # "id": mid,
        "maxPoints": max_points,
        "minPoints": min_points,
        "name": name
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        result.status = True
    result.response = res


# 保存评分维度，修改是要传id
def modify_scoring_dimension(sd_id, min_points, max_points, name):
    result = BaseResult()
    req_data = {
        "id": sd_id,
        "maxPoints": max_points,
        "minPoints": min_points,
        "name": name
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        finvalue = db.select_db('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 5:
            result.status = True
    result.response = res



# 保存评分维度，修改是要传id
def modify_scoring_dimension(sd_id, min_points, max_points, name):
    result = BaseResult()
    req_data = {
        "id": sd_id,
        "maxPoints": max_points,
        "minPoints": min_points,
        "name": name
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        finvalue = db.select_db('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 5:
            result.status = True
    result.response = res


def modify_scoring_dimension(**kwargs):
    result = BaseResult()
    # req_data = {
    #     "id": sd_id,
    #     "maxPoints": max_points,
    #     "minPoints": min_points,
    #     "name": name
    # }
    req_data = kwargs
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        finvalue = db.select_db('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 5:
            result.status = True
    result.response = res


if __name__ == '__main__':
    modify_scoring_dimension()
