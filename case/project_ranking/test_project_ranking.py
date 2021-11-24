#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 下午3:06

import pytest

from api.project_ranking import project_ranking
from faker_util import fakerist
from serv import channel_serv
from util.data_util import data_pool
from util.sql_util import mysqler


class TestProjectRanking:

    # @pytest.mark.skip
    @pytest.mark.repeat(1)
    @pytest.mark.usefixtures("crm_login_with_mm")
    @pytest.mark.parametrize("kwargs", data_pool.supply('project_ranking_data.yml', 'save_activity'))
    def test_save_activity(self, kwargs):
        # 数据统计页面是根据渠道码而非具体活动来统计，所以每个活动尽量要用专门的渠道码，方便排查
        channel_code = channel_serv.add_channel_random()

        # 新建作品排名活动
        kwargs = data_pool.supply('project_ranking_data.yml', 'save_activity')[0]
        kwargs['channelCode'] = channel_code
        kwargs['activityName'] = fakerist.word()
        kwargs['howToPlay'] = 1  # 1点赞 2注册
        kwargs['chooseStartTime'] = '2020-01-22 00:00:00'
        kwargs['chooseEndTime'] = '2021-11-22 00:00:00'
        kwargs['startTime'] = '2021-11-20 00:00:00'
        kwargs['endTime'] = '2021-12-22 00:00:00'
        res1 = project_ranking.save_activity(**kwargs)
        assert res1.status is True

        # 活动启用 需确保没有其他在进行的活动
        query_latest_id = 'SELECT pa.id FROM mxc_activity.project_activity pa WHERE 1=1 ORDER BY id DESC limit 1'
        latest_id = mysqler.query(query_latest_id)[0][0]
        kwargs2 = data_pool.supply("project_ranking_data.yml", 'update_status')[0]
        kwargs2['id'] = latest_id
        kwargs2['status'] = 1  # 1启用 0禁用
        res2 = project_ranking.update_status(**kwargs2)


if __name__ == '__main__':
    pass
