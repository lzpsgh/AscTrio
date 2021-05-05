import allure
import pytest

from service.leads.leads import *
from util.logger import logger


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：leads入库-分配cc-官网下单-支付-成功回调")
class TestLeadsPay:

    @allure.story("故事：leads入库-分配cc-官网下单-支付-成功回调")
    @allure.description("该用例是针对 leads入库-分配cc-官网下单-支付-成功回调 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("leads入库分配cc官网下单支付-预期成功")
    @pytest.mark.multiple
    # @pytest.mark.usefixtures("delete_register_user")
    def test_leads_cc_order_pay(self):
        booking_demo()

        username = testcase_data["username"]
        password = testcase_data["password"]
        telephone = testcase_data["telephone"]
        sex = testcase_data["sex"]
        address = testcase_data["address"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success is True, result.error
        result = login_user(username, password)
        step_2(username)
        assert result.success is True, result.error
        result = get_one_user_info(username)
        step_3(username)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_leads_pay.py"])
