# coding     : utf-8
# @Time      : 2021/5/2 下午1:43
from util.log_kit import logger


# todo 改用try-except异常并抛捕获
# todo 流程和异常判定优化
def result_check(result):
    origin = 'api'
    if origin == 'case':
        return

    if result.rsp is not None:
        response_code = result.rsp.status_code
        if response_code == 200:
            rsp_json = result.rsp.json()  # 响应文本如果不是合法的json文本就会报错
            if rsp_json['success'] is True:
                result.status = True  # 写入1
                if 'data' in rsp_json:
                    # 写入2
                    logger.info('响应体是: ' + str(rsp_json['data']))
                    result.sdata = rsp_json['data']
                else:
                    logger.info('接口正常，响应体内不包含data')
                    logger.info(rsp_json)
            else:
                logger.info('响应码200，但success为False')
                logger.info('rsp_json' + str(rsp_json))
        else:
            logger.error('异常响应码: ' + str(response_code))
        # logger.debug(str(result.rsp.json))
    else:
        logger.error('无法成功获取res响应体对象')
        exit()


def assertDictContainEqual(expected, result):
    """判断字典expected包含于result"""
    expectedkey = set(expected.items())
    if expectedkey.issubset(result.items()):
        assert True
    else:
        assert False


def assertListContainEqual(expected, result):
    """判断列表expected包含于result"""
    if set(expected).issubset(set(result)):
        assert True
    else:
        assert False


def assertListIsDictContainEqual(expected, result):
    """判断列表中字典expected包含于result"""
    flag = True
    for index in range(len(expected)):
        for num in range(len(result)):
            if assertDictContainEqual(dict(expected[index]), dict(result[num])):
                flag == True
                break
            else:
                flag == False
                continue
    if flag:
        assert True
    else:
        assert False
