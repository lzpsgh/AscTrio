# coding     : utf-8
# @Time      : 2021/4/19 下午1:40
# coding: utf-8

# 项目配置
PROJECT_ROOT = ''
COOKIE_YML = f''

# 数据库-mysql
MYSQL_HOST = ""
MYSQL_PORT = ""
MYSQL_USER = ""
MYSQL_PASSWD = ""
MYSQL_DB = ""
MYSQL_CHARSET = ""

# 数据库-redis
REDIS_ADDRESS = ""

# 服务器环境
# test prod sta dev
env = "test"
# 测试环境
if env == "test":
    BASE_URL_CORE = ""
    BASE_URL_GZ = ""
# 生产环境
elif env == "prod":
    BASE_URL_CORE = ""
    BASE_URL_GZ = ""
# 预生产环境
elif env == "sta":
    pass
# 开发环境
elif env == "dev":
    pass
else:
    raise Exception("环境变量env错误")
