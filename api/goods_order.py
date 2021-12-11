from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util

sql_query_userid = "select id from activityuser where phone = "
sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "
goodsIds = '373'  # 457是S0课799块 373是K1课5280块 305是py的S5课6000块 301是S1课5280块
pay_amount = '5280'  # 价格要同时改
order_no = 'O2105207930118'


class GoodsOrder(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GoodsOrder, self).__init__(api_root_url, **kwargs)

    # 官网-创建订单-微信支付
    def demolition_order(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/goodsOrder/demolitionOrder'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 进入微信支付页下单
    def get_pay_page(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/goodsOrder/getPayPage'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 支付模拟回调成功
    SQL_ORDERNO_OUTTRADENO = '''
        SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE pr.id = '{}';
    '''

    def pay_callback_suc(self, out_trade_no):
        self.req_method = 'GET'
        self.req_url = '/core/goodsOrder/simulationCallBack'
        self.req_body = {
            'outTradeNo': out_trade_no
        }

        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 忘了嘻嘻
    def is_use_coupon(self):
        self.req_method = 'GET'
        self.req_url = '/core/goodsOrder/orderDetailForKK'
        self.req_body = {
            "goodsIds": "373",
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 校区工作台
    # 订金流水可直接调此接口退款
    # 尾款流水的type改成订金流水，然后调此接口也可
    def cancel_order(self, goid):
        self.req_method = 'POST'
        self.req_url = '/core/goodsOrder/cancelOrder'
        self.req_body = {
            'goodsOrderId': goid
        }
        self.req_headers = {
            'mxc-token': auth_util.get_token('mxc', 'mxc-token')
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result


goods_order = GoodsOrder(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    # goods_order.pay_callback_suc('202112101213017854754781')
    goods_order.cancel_order('51796')
