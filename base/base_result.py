"""
自定义示例：
result = ResultBase()
result.success = False
result.msg = res.json()["msg"]
result.response = res
"""


class BaseResult:
    pass
    # status
    # def __init__(self, rsp_code):
    #     self._rsp_code = rsp_code
