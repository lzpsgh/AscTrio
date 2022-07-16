#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 16:07
from api.location import location
from faker_util import fakerist
from util.data_util import data_pool
from util.log_util import logger


def flow_project(self):
    # 新建场地并获取场地id
    xdata1 = data_pool.supply("test_location.yml", 'test_add_location')[0]
    # 网规通道编码
    xdata1['networkPlanningLocationCode'] = 'serv' + fakerist.numerify()
    # 场地名称
    xdata1['locationName'] = 'serv' + fakerist.word()
    res1 = location.add_location(xdata1)
    location_id = res1.sdata
    logger.info(f'新建场地的id是={location_id}')  # 190

    # 新建对应立项并获取立项id
    xdata2 = data_pool.supply("test_location.yml", 'test_add_project')[0]
    # 所属场地id
    xdata1['locationId'] = int(location_id)

    station_type = fakerist.station_type()
    xdata1['stationType'] = station_type
    xdata1['projectName'] = location_id + '-' + station_type
    xdata1['type'] = 1
    res2 = location.add_project(xdata2)
    project_id = res2.sdata
    logger.info(f'新建场地的id是={project_id}')  # 218

    # 新建建站申请
