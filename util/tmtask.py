# coding     : utf-8
# @Time      : 2021/4/30 上午10:47

from base.base_request import BaseRequest
from config import envar

base_requests = BaseRequest(envar.BASE_URL_GZ)


# 传入定时任务url（带相关字段）
def call_method(url):
    res = base_requests.request("GET", url)
