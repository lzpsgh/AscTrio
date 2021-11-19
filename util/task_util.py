# coding     : utf-8
# @Time      : 2021/4/30 上午10:47

import requests

from util.log_util import logger


# 转介绍
# https://sit.miaocode.com/core/sfsaferwefvcxv3r34342/CallMethodByAnotation?className=com.gz.mxc.service.timer.ReportTimerTask&methodName=referralData

def call_method(url):
    # result = base_requests.request("GET", url)
    res = requests.get(url)
    logger.info(res.text)
