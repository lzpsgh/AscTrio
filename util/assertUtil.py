__author__ = 'leifen'


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
