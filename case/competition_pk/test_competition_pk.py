# coding     : utf-8
# @Time      : 2021/5/5 下午4:02

import pytest

from api.competition_pk import cmpttn_pk
from case import conftest
from util.log_util import logger


class TestScoringDimension:

    # 在BaseCase里面提供一个函数，将当前类对应的
    # yml中每一行用例都是一个字典
    # conftest.supply(yml_path,yml_name)
    # 类名TestScoringDimension，转化成test_scoring_dimension，找到data下该文件
    # 方法名test_get_scoring_dimension_by_id，直接找到文件内的键名
    @pytest.mark.parametrize("datajson",
                             conftest.supply('test_scoring_dimension.yml',
                                             'test_get_scoring_dimension_by_id'))
    def test_get_scoring_dimension_by_id(self, datajson):
        echo = cmpttn_pk.get_scoring_dimension_by_id(datajson['ssid']).sdata
        assert echo.get('minPoints') == datajson['minPoints'] and \
               echo.get('maxPoints') == datajson['maxPoints'] and \
               echo.get('name') == datajson['name']

    # 查询评分维度列表-所有
    @pytest.mark.skip
    @pytest.mark.single
    def test_get_scoring_dimension_list(self):
        # logger.info("\n*************** 开始执行用例 ***************")
        result = cmpttn_pk.get_scoring_dimension_list()
        dimension_len = len(result.sdata)
        assert dimension_len > 0
        logger.info(f"评分维度总数 ==>> 期望大于0个， 实际结果：{dimension_len}")
        # logger.info("\n*************** 结束执行用例 ***************")

    # 查询评分维度列表-单个赛事id
    # @pytest.mark.parametrize("xid,xname,xmin,xmax",
    #                          [[6, '体脂率', 2, 27],
    #                           [13, '舔度222', 4, 8]])
    # def test_get_scoring_dimension_by_id(self, xid, xname, xmin, xmax):
    #     echo = scoring_dimension.get_scoring_dimension_by_id(xid).sdata
    #     assert echo.get('minPoints') == xmin and \
    #            echo.get('maxPoints') == xmax and \
    #            echo.get("name") == xname


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_competition_pk.py"])
