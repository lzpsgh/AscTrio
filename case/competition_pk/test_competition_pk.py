# coding     : utf-8
# @Time      : 2021/5/5 下午4:02

import pytest

import competition_pk_serv
from api.competition_pk import cmpttn_pk
from util.log_util import logger


class TestScoringDimension:

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

    # 新建赛事
    # @pytest.mark.skip
    @pytest.mark.single
    @pytest.mark.usefixtures("crm_login_with_mm")
    def test_save_competition(self):
        cmp_id = competition_pk_serv.save_cmp_nonreg_1()
        # cmp_id = competition_pk_serv.save_cmp_nonreg_13()
        # cmp_id = competition_pk_serv.save_cmp_nonreg_17()
        # cmp_id = competition_pk_serv.save_cmp_reg_1()
        assert cmp_id
        logger.info(f"赛事ID：{cmp_id}")

        # user.login(phone)
        # project.save_scratch_project_for_user()


if __name__ == '__main__':
    # pytest.main(["-q", "-s", "test_competition_pk.py"])
    pass
