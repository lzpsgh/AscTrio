#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 下午1:23


import pytest

from api.teachers_day_vote import teachers_day_vote


class TestTeacherDayVote:

    # @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.parametrize(
    # "kwargs", data_pool.supply('goods_order_data.yml', 'demolition_order_k1'))
    # @pytest.mark.usefixtures("crm_login_with_mm")
    def test_vote(self, kwargs):
        res = teachers_day_vote.vote(kwargs)
        assert res.status is True


if __name__ == '__main__':
    pytest.main(
        ["-q", "-s", "test_blue_bridge_contest.py::TestBlueBridgeContest"])
