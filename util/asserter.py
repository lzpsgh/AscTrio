# coding     : utf-8
# @Time      : 2021/5/2 下午1:43

# assert "h" in "hello"  #判断h在hello中
# assert 5>6             #判断5>6为真
# assert not True        #判断xx不为真
# assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}     #判断两个字典相等


# todo 改用try-except异常并抛捕获
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
                    print('响应体是: ' + str(rsp_json['data']))
                    result.sdata = rsp_json['data']
                else:
                    print('接口正常，响应体内不包含data')
                    print(rsp_json)
            else:
                print('响应码200，但success为False')
                print('rsp_json' + str(rsp_json))
        else:
            print('异常响应码: ' + str(response_code))
        print(str(result.rsp.json))
    else:
        print('无法成功获取res响应体对象')
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
