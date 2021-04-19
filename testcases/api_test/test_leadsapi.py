import pytest

from service import leads_api
from testcases.conftest import leadsapi_data
from util.logger import logger


class TestLeadsApi:
    @pytest.mark.single
    @pytest.mark.parametrize("secret, except_result, except_code, except_msg",
                             leadsapi_data["test_get_token"])
    def test_get_token(self, secret, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = leads_api.get_token(secret)
        print(result.__dict__)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_leadsapi.py"])
