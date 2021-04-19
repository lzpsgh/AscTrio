import json
from configparser import ConfigParser

import yaml

from config import envar
from util.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData:

    def __init__(self):
        pass

    def save_cookie_yml(self, yml_data):
        file_path = envar.COOKIE_YML
        logger.debug(f"打开文件: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            tmp_data = yaml.safe_dump(yml_data, f, default_flow_style=False)  # 写入文件，不是用flow流格式
        logger.debug(f"写入数据: {tmp_data} ")
        return tmp_data

    def load_yaml(self, file_path):
        # logger.debug(f"加载文件 {file_path}")
        print(f"加载文件 {file_path}")
        with open(file_path, encoding='utf-8') as f:
            tmp_data = yaml.safe_load(f)
        print(f"读取数据 {tmp_data}")
        return tmp_data

    def load_json(self, file_path):
        logger.debug("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.debug("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.debug("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data


data_tool = ReadFileData()

if __name__ == '__main__':
    pass
