# coding     : utf-8
# @Time      : 2021/4/16 下午3:52

# 环境变量: prod test stage
env_name = 'test'
env_path = f'/Users/lensaclrtn/Project/AscTrio/{env_name}.env'


class BaseService:
    req_headers = {}

    def __init__(self):
        self.req_headers = {
            # "Host": "sit.miaocode.com",
            "Cache-Control": "no-cache",
            # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
        }
