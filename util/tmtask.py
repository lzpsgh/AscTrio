# coding     : utf-8
# @Time      : 2021/4/30 上午10:47

from base.base_request import BaseRequest
from util import common

base_requests = BaseRequest(common.env('BASE_URL_GZ'))

# 转介绍
# https://sit.miaocode.com/core/sfsaferwefvcxv3r34342/CallMethodByAnotation?className=com.gz.mxc.service.timer.ReportTimerTask&methodName=referralData


# 传入定时任务url（带相关字段）
def call_method(url):
    result = base_requests.request("GET", url)

