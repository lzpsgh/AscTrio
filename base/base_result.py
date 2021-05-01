"""
自定义示例：
result = ResultBase()
result.success = False
result.msg = res.json()["msg"]
result.response = res
"""


class BaseResult:
    # 代表requests发起请求后返回的Response对象（未经过序列化）
    rsp = {}

    # 当且仅【当响应码为200】且【success为True】时 status为True
    # 也就是 result.rsp.status_code==200 and result.rsp.json()['success'] is True
    status = False

    # 响应体中的data字段数据（经过序列化处理）
    # 也就是 result.rsp.json()['data']
    sdata = {}
