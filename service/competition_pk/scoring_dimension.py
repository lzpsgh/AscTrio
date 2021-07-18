# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 下午5:58


from base.base_response import BaseResponse
# from competition_pk import scoring_dimension
from util import auth_kit
from util import common_kit
from util.log_kit import logger
from util.mysql_kit import mysqler


# 删除评分维度
def del_scoring_dimension_by_id(sd_id):
    # 记录请求头请求体 响应头响应体
    result = BaseResponse()
    req_data = {
        "id": sd_id
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('crm'),
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
    result = BaseResponse()
    req_data = {
        # "id": mid,
        "maxPoints": max_points,
        "minPoints": min_points,
        "name": name
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('crm'),
    }
    res = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200:
        result.status = True
    result.response = res


# 保存评分维度，修改是要传id
def modify_scoring_dimension(sd_id, min_points, max_points, name):
    req_data = {
        "id": sd_id,
        "maxPoints": max_points,
        "minPoints": min_points,
        "name": name
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('crm'),
    }
    result = scoring_dimension.save_scoring_dimension(data=req_data, cookies=req_cookies)
    common_kit.result_check(result)
    finvalue = mysqler.select_db('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
    if finvalue == 2:
        logger.info(finvalue)
    return result



if __name__ == '__main__':
    modify_scoring_dimension(3, 2, 30, "aaaaa")
