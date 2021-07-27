import redis_util  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

from util import common_util


class RedisUtil:

    def redis_init_pool(self):
        pool = redis_util.ConnectionPool(
            host=common_util.env('REDIS_HOST'),
            port=common_util.env('REDIS_PORT'),
            decode_responses=True)
        r = redis_util.Redis(connection_pool=pool)
        return r


redis_util = RedisUtil().redis_init_pool()


def get_key(key):
    return redis_util.get(key)


def del_key(key):
    return redis_util.delete(key)


def set_key(key, data):
    return redis_util.set(key, data)
