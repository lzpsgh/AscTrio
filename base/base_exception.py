# coding     : utf-8
# @Time      : 2021/5/1 下午9:23


class BaseException(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return 'ReplyError(' + str(self.msg) + ')'


if __name__ == '__main__':
    try:
        raise BaseException('基本异常')
    except BaseException as e:
        print(e)
