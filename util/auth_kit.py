# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:32


from util import common_kit
from util.data_kit import data_pool


# todo 二期-鉴权-改用RequestsCookieJar
# [https://docs.python-requests.org/zh_CN/latest/user/quickstart.html?highlight=cookie#cookie]

# todo 二期-鉴权-增加token鉴权方式

# 获取现有的cookies
def get_cookies_all():
    cookie = data_pool.load_yml(common_kit.env('COOKIE_YML'))
    return cookie


# 获取现有的cookies
def get_cookie(kw):
    cookie = data_pool.load_yml(common_kit.env('COOKIE_YML'))
    kw_cookie = cookie.get(kw).get('jsessionid')
    return kw_cookie


# 更新cookie-用于手动调用
# 判断是str(先组装再dump)还是dict(不组装直接dump)
def set_cookie(kw, tmp_data):
    if type(tmp_data) != str and type(tmp_data) != dict:
        raise TypeError
    if type(tmp_data) == str:
        tmp_cookies = get_cookies_all()
        tmp_cookies[kw]['jsessionid'] = tmp_data
        tmp_data = tmp_cookies
    data_pool.save_cookie_yml(tmp_data)


def check_auth():
    jsid = get_cookie()
    set_cookie(jsid)


if __name__ == '__main__':
    pass
