import logging
import os
import time
from colorlog import ColoredFormatter
from util import common

# BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_PATH = common.env('PROJECT_ROOT')

# LOG_PATH = f"{BASE_PATH}/log"
LOG_PATH = common.env('LOG_PATH')

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        # self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)


        # 设置输出的日志字符串格式
        # fmt = '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        LOG_FORMAT_CONSOLE = "%(log_color)s[%(asctime)s] [%(filename)s %(lineno)d][%(levelname)-5.5s] %(message)s"
        LOG_FORMAT_FILE = "%(asctime)s[%(filename)s %(lineno)d][%(levelname)-5.5s] %(message)s"

        # 设置颜色
        # self.formater = logging.Formatter(LOG_FORMAT_CONSOLE)
        formatter_file = logging.Formatter(LOG_FORMAT_FILE)
        formatter_console = ColoredFormatter(
            LOG_FORMAT_CONSOLE,
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG': 'white',
                'INFO': 'cyan',
                'WARNING': 'yellow',
                'ERROR': 'red',
            },
            secondary_log_colors={},
            style='%'
        )

        # 分别设置日志和控制台
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(formatter_file)

        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.console.setFormatter(formatter_console)  # self.formater
        # 分别添加到handler中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.info("---测试结束---")
