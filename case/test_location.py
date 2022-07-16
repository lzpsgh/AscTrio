#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 09:53


import pytest

from api.location import location
from util.log_util import logger


class TestLocation:

    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.xdata
    def test_add_location(self, xdata):
        xdata['networkPlanningLocationCode'] = 'asc0716'
        xdata['locationName'] = 'asc0716'
        res1 = location.add_location(xdata)
        assert res1.status is True
        location_id = res1.sdata
        logger.info(f'新建场地的id是={location_id}')  # 190

    # @pytest.mark.skip
    # @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.xdata
    def test_add_project(self, xdata):
        res2 = location.add_project(xdata)
        assert res2.status is True
        project_id = res2.sdata
        logger.info(f'新建场地的id是={project_id}')  # 218
