import allure
import pytest

from api.uoactivity.dragon_boat_festival import dbf
from util.logger import logger


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestDragonBoatFestival:

    # @allure.story("用例--注册/登录/查看--预期成功")
    # @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.skip
    @pytest.mark.single
    # @pytest.mark.usefixtures("delete_register_user")
    def test_dbf_accept_zong_zi(self):
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.skip
    @pytest.mark.single
    def test_dbf_leader_board(self):
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.single
    def test_dbf_set_time_running(self):
        # dbf.dbf_set_time('1624204800000', '1625065200000')  # 21-30 未开始
        dbf.dbf_set_time('1622476800000', '1625065200000')  # 1-30  进行中
        # dbf.dbf_set_time('1622476800000', '1622646000000')  # 1-2   已结束
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_dragon_boat_festival.py::TestDragonBoatFestival::test_dbf_set_time_running"])
