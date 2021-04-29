"""
自定义示例：
result = ResultBase()
result.success = False
result.msg = res.json()["msg"]
result.response = res
"""


# 当且仅当 响应码为【200】 且 响应体中success为【True】时，status置为True


class BaseResult:
    status = False
    rsp = {}
