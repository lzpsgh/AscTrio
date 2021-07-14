import redis_kit  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

from util import common_kit


class RedisUtil:

    def redis_init_pool(self):
        pool = redis_kit.ConnectionPool(
            host=common_kit.env('REDIS_HOST'),
            port=common_kit.env('REDIS_PORT'),
            decode_responses=True)
        r = redis_kit.Redis(connection_pool=pool)
        return r


redis_util = RedisUtil().redis_init_pool()


def get_key(key):
    return redis_util.get(key)


def del_key(key):
    return redis_util.delete(key)


def set_key(key, data):
    return redis_util.set(key, data)
