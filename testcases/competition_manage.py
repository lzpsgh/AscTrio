# coding     : utf-8
# @Time      : 2021/4/12 下午6:12

import pytest

from service import goods_order
from util.logger import logger
from util.mysql_operate import db


class TestPayCallbackWX():

    # @pytest.mark.single
    # @pytest.mark.parametrize("outTradeNo",'202103251226456923966257')
    # @pytest.mark.parametrize("order_no", 'O2114666550325')
    def test_pay_callback_wx(self):
        logger.info("\n*************** 开始执行用例 ***************")

        sql_orderno = "SELECT outTradeNo FROM payrecord WHERE payStatus = 'WAITING' AND payType = 'WX'"
        sql_result = db.select_db(sql_orderno)
        logger.info(sql_result)
        if sql_result == '' or sql_result is None:
            exit("sorry, goodbye!")
            # pass

        out_trade_no = sql_result[0][0]
        logger.info("out_trade_no是 " + out_trade_no)

        result = goods_order.pay_callback_suc(out_trade_no)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_result, result.error
        # logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg

        logger.info("\n*************** 结束执行用例 ***************")

    @pytest.mark.parametrize("order_no", [
        "O2147177690311",
        "O2172773530310",
        "O2163941330310",
        "O2162371280310",
        "O2169500160310",
        "O2115445220310",
        "O2164415730309",
        "O2126644890303"
    ])
    def test_is_use_coupon(self, order_no):
        logger.info("\n*************** 开始执行用例 ***************")
        sql_orderno = "SELECT id FROM goodsorder g WHERE orderNo = '" + order_no + "'"
        # sql_orderno = "SELECT id FROM goodsorder g WHERE orderNo = 'O2163941330310' "
        logger.info(sql_orderno)
        sql_result = db.select_db(sql_orderno)
        # sql_result = db.select_db(sql_orderno + order_no)
        logger.info(sql_result)
        if sql_result == '' or sql_result is None:
            exit("sorry, goodbye!")

        goods_order_id = str(sql_result[0][0])
        logger.info("goods_order_id " + goods_order_id)
        result = goods_order.is_use_coupon(goods_order_id)

        # assert result.response.status_code == 200
        assert result.has_coupon is True

        logger.info("\n*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "pay_callback_wx.py"])
