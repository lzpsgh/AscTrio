#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 09:53


import pytest

from api.location import location


class TestLocation:

    # @pytest.mark.skip
    # @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.auto_kwargs
    def test_add_location(self, auto_kwargs):
        auto_kwargs['networkPlanningLocationCode'] = 'asc0716'
        auto_kwargs['locationName'] = 'asc0716'
        res1 = location.add_location(auto_kwargs)
        # prom = res1.sdata.get('resultInquiryList')[0].get('promotionResult')
        # logger.info(f'晋级情况={prom}') id是190
        assert res1.status is True
