#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 19:00

import pytest

from api.station_apply import station_apply


class TestStationApply:

    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.xdata
    def test_add_station_apply(self, xdata):
        location_id = 190
        location_name = 'asc0716'
        project_id = 218
        project_name = '新建站S'
        station_type = 'S站'
        # TODO 以上均从场地立项详情中获取

        # 场地和立项 从响应体里获取
        xdata['constructionRequest']['locationId'] = location_id
        xdata['constructionRequest']['locationName'] = location_name
        xdata['constructionRequest']['projectId'] = project_id
        xdata['constructionRequest']['projectName'] = project_name
        # TODO 用户信息 这里待确认
        xdata['constructionRequest']['serviceOperatorId'] = 1
        # 站点信息-立项只有1个站点时

        xdata['stationRequest'][0]['stationType'] = station_type
        xdata['stationRequest'][0]['civilEngineeringEstimate'] = 3000
        xdata['stationRequest'][0]['lowVoltageBuildEstimate'] = 2000
        # 场地信息
        xdata['landRequest']['planElectricCapacityIncrease'] = 4000
        xdata['landRequest']['highVoltageEstimate'] = 1000
        # 日期
        xdata['otherRequest']['planLeaseSignDate'] = '2022-07-17'
        xdata['otherRequest']['planCivilEngineeringBiddingDate'] = '2022-08-01'
        xdata['otherRequest']['planCivilEngineeringBuildDate'] = '2022-08-02'
        xdata['otherRequest']['planCivilEngineeringFinishDate'] = '2022-08-03'
        xdata['otherRequest']['planReportElectricityFinishDate'] = '2022-08-06'
        xdata['otherRequest']['planHighVoltageBiddingDate'] = '2022-08-11'
        xdata['otherRequest']['planHighVoltageBuildDate'] = '2022-08-12'
        xdata['otherRequest']['planHighVoltageFinishDate'] = '2022-08-13'
        xdata['otherRequest']['planEquipmentOrderGoodsDate'] = '2022-08-14'
        xdata['otherRequest']['planEquipmentInstallDate'] = '2022-08-15'
        xdata['otherRequest']['planStartStationOperateDate'] = '2022-08-31'

        res = station_apply.add_station_apply(xdata)
        assert res.status is True

    # @pytest.mark.skip
    @pytest.mark.usefixtures("crm_login_with_mm")
    # @pytest.mark.xdata
    def test_withdraw_station_apply(self):
        id = 133
        res2 = station_apply.withdraw_station_apply(id)
        assert res2.status is True
