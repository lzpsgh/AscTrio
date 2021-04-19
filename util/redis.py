import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

import config


class RedisUtil(object):

    def redis_init_pool(self):
        pool = redis.ConnectionPool(
            host=config.redis_host,
            port=config.redis_port,
            decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        return r


redis_util = RedisUtil().redis_init_pool()


def getKey(key):
    return redis_util.get(key)


def delKey(key):
    return redis_util.delete(key)


def setKey(key, data):
    return redis_util.set(key, data)
