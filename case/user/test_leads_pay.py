import pytest

from user import user
from util.data_util import data_pool


# @allure.severity(allure.severity_level.CRITICAL)
# @allure.epic("针对业务场景的测试")
# @allure.feature("场景：leads入库-分配cc-官网下单-支付-成功回调")
class TestLeadsPay:

    # @allure.story("故事：leads入库-分配cc-官网下单-支付-成功回调")
    # @allure.description("该用例是针对 leads入库-分配cc-官网下单-支付-成功回调 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("leads入库分配cc官网下单支付-预期成功")
    @pytest.mark.multiple
    # @pytest.mark.usefixtures("delete_register_user")
    @pytest.mark.parametrize("datajson", data_pool.supply('test_leads.yml', 'test_leads_cc_login'))
    def test_leads_cc_order_pay(self, datajson):
        # sql_query_cc = "select salerid from activityuser where id = 889"
        result1 = user.send_sms2(datajson['phone'])
        if result1.status is True:
            result2 = user.register(datajson)
            if result2.status is True:
                result3 = user.modify_users_owner(datajson['phone'])
        assert result3.status is True
        # print(db.select_db(sql_query_cc)[0])

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_leads_pay.py"])
