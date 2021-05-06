# coding     : utf-8
# @Time      : 2021/5/6 下午11:08

import pytest

from service import leads
from util.logger import logger


class TestOfficialAddLeads:
    # @pytest.mark.parametrize("datajson",
    #                          conftest.data_tracking('test_scoring_dimension.yml',
    #                                                 'test_get_scoring_dimension_by_id'))
    @pytest.mark.parametrize("phone", ['18888655450'])
    def test_official_add_leads_1(self, phone):
        leads.official_add_leads_1(phone)
        logger.info(f'新leads注册: {phone}')


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_official_add_leads.py"])
