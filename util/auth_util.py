# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:32


from util import common_util
from util.data_util import data_pool


# 获取现有的cookies
def get_cookies_all():
    cookie = data_pool.load_yml(common_util.env('COOKIE_YML'))
    return cookie


# 获取现有的cookies
def get_cookie(kw):
    cookie = data_pool.load_yml(common_util.env('COOKIE_YML'))
    kw_cookie = cookie.get(kw).get('jsessionid')
    return kw_cookie


# 更新cookie-用于手动调用
def set_cookie(kw, tmp_data):
    if type(tmp_data) != str and type(tmp_data) != dict:
        raise TypeError
    if type(tmp_data) == str:
        tmp_cookies = get_cookies_all()
        tmp_cookies[kw]['jsessionid'] = tmp_data
        tmp_data = tmp_cookies
    data_pool.save_cookie_yml(tmp_data)


# 获取api_account_token
# usage： 'api_account_token': auth_util.get_bbc_token('crm'),
def get_gz_token(kw):
    cookie = data_pool.load_yml(common_util.env('COOKIE_YML'))
    kw_cookie = cookie.get(kw).get('api_account_token')
    return kw_cookie


# 更新api_account_token-用于蓝桥杯项目
def set_gz_token(kw, tmp_data):
    if type(tmp_data) != str and type(tmp_data) != dict:
        raise TypeError
    if type(tmp_data) == str:
        tmp_cookies = get_cookies_all()
        tmp_cookies[kw]['api_account_token'] = tmp_data
        tmp_data = tmp_cookies
    data_pool.save_cookie_yml(tmp_data)


# 通用get
# usage： 'exam_token': auth_util.get_token('bbc', 'exam_token')
def get_token(kw, kwson):
    cookie = data_pool.load_yml(common_util.env('COOKIE_YML'))
    kw_cookie = cookie.get(kw).get(kwson)
    return kw_cookie


# 通用set
# auth_util.set_token('bbc', 'exam_token', result.rsp.cookies["exam_token"])
def set_token(kw, kwson, tmp_data):
    if type(tmp_data) != str and type(tmp_data) != dict:
        raise TypeError
    if type(tmp_data) == str:
        tmp_cookies = get_cookies_all()
        tmp_cookies[kw][kwson] = tmp_data
        tmp_data = tmp_cookies
    data_pool.save_cookie_yml(tmp_data)


if __name__ == '__main__':
    pass
