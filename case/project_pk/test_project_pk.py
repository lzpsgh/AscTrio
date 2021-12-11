#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 下午2:21


import pytest

from api.project_pk import project_pk
from api.user import user
from util.data_util import data_pool
from util.log_util import logger


class TestProjectPK:

    # @pytest.mark.skip
    @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
    # @pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'h5_query444'))
    def test_aaa(self, kwargs):
        kwargs['identityNo'] = 123
        res = user.result_inquiry(**kwargs)
        prom = res.sdata.get('resultInquiryList')[0].get('promotionResult')
        logger.info(f'晋级情况={prom}')
        kwargs8 = data_pool.supply('bbc_submit_paper.yml', 'submit_official_paper')[0]
        res8 = user.submit_official_paper(**kwargs8)
        assert res.status is True

    @pytest.mark.parametrize("datajson",
                             data_pool.supply('test_scoring_dimension.yml',
                                              'test_get_scoring_dimension_by_id'))
    def test_get_scoring_dimension_by_id(self, datajson):
        echo = project_pk.get_scoring_dimension_by_id(datajson['ssid']).sdata
        assert echo.get('minPoints') == datajson['minPoints'] and \
               echo.get('maxPoints') == datajson['maxPoints'] and \
               echo.get('name') == datajson['name']

    # 查询评分维度列表-所有
    @pytest.mark.skip
    @pytest.mark.single
    def test_get_scoring_dimension_list(self):
        # logger.info("\n*************** 开始执行用例 ***************")
        result = project_pk.get_scoring_dimension_list()
        dimension_len = len(result.sdata)
        assert dimension_len > 0
        logger.info(f"评分维度总数 ==>> 期望大于0个， 实际结果：{dimension_len}")
        # logger.info("\n*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pass
