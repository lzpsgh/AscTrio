#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 16:07
from api.location import location
from api.station_apply import station_apply
from faker_util import fakerist
from util.data_util import data_pool
from util.log_util import logger


def flow_project():
    # 1新建场地并获取场地id
    xdata1 = data_pool.supply("test_location.yml", 'test_add_location')[0]
    # 网规通道编码
    xdata1['networkPlanningLocationCode'] = 'serv' + fakerist.numerify()
    # 场地名称
    xdata1['locationName'] = 'serv' + fakerist.word()
    res1 = location.add_location(xdata1)
    location_id = res1.sdata
    logger.info(f'新建场地的id是={location_id}')  # 196

    # 2新建对应立项并获取立项id
    xdata2 = data_pool.supply("test_location.yml", 'test_add_project')[0]
    # 所属场地id
    xdata2['locationId'] = int(location_id)
    station_type = fakerist.station_type()
    xdata2['stationType'] = station_type
    xdata2['projectName'] = f"{location_id}-{station_type}"
    xdata2['type'] = 1
    res2 = location.add_project(xdata2)
    project_id = res2.sdata
    logger.info(f'新建场地的id是={project_id}')  # 219

    # 新建建站申请
    xdata3 = data_pool.supply("test_station_apply.yml", 'test_add_station_apply')[0]
    xdata3['constructionRequest']['locationId'] = str(location_id)
    # xdata3['constructionRequest']['locationName'] = location_name
    xdata3['constructionRequest']['projectId'] = str(project_id)
    # xdata3['constructionRequest']['projectName'] = project_name
    res3 = station_apply.add_station_apply(xdata3)
    station_apply_id = res3.sdata
    logger.info(f'建站申请的id是={station_apply_id}')  # 133


if __name__ == '__main__':
    flow_project()
