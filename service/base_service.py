# coding     : utf-8
# @Time      : 2021/4/16 下午3:52
# 环境变量: prod test stage
env_name = 'test'
env_path = f'/Users/lensaclrtn/Project/AscTrio/{env_name}.env'


class BaseService:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass
        # load_dotenv(dotenv_path=env_path)
