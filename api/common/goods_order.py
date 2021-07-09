from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common

sql_query_userid = "select id from activityuser where phone = "
sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "
goodsIds = '373'  # 457是S0课799块 373是K1课5280块 305是py的S5课6000块 301是S1课5280块
pay_amount = '5280'  # 价格要同时改
order_no = 'O2105207930118'


class GoodsOrder(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GoodsOrder, self).__init__(api_root_url, **kwargs)

    # 官网-创建订单-微信支付
    def demolition_order(self):
        self.req_method = 'POST'
        self.req_url = '/goodsOrder/demolitionOrder'
        self.req_body = {
            'couponIds': '',
            'goodsIds': '373',
            'payType': 'WX',
            'payStyle': 'NATIVE',
            'giveCourses': '',
            'giveOtherGifts': '',
            'orderSource': 'GUAN_WANG',
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 进入微信支付页下单
    def get_pay_page(self):
        self.req_method = 'POST'
        self.req_url = '/goodsOrder/getPayPage'
        self.req_body = {
            'orderNo': 'O2105207930118',
            'payType': 'WX',
            'payStyle': 'NATIVE',
            'amount': '5280',
            'stageNum': '',
            'forwordUrl': 'https://sit-xuexi.miaocode.com/market/paySuccess',
            'cancelUrl': 'https://sit-xuexi.miaocode.com/order/457',
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 微信支付模拟回调成功
    SQL_ORDERNO_OUTTRADENO = '''
        SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE go.orderNo = 'xxxx' AND pr.payStatus = 'WAITING';
    '''

    def pay_callback_suc(self, out_trade_no):
        self.req_method = 'GET'
        self.req_url = '/goodsOrder/simulationCallBack'
        self.req_body = {
            'outTradeNo': out_trade_no  # '$sql_query_tradeno$pay_rec_id'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 忘了嘻嘻
    def is_use_coupon(self):
        self.req_method = 'GET'
        self.req_url = '/goodsOrder/orderDetailForKK'
        self.req_body = {
            "goodsIds": "373",
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result


goods_order = GoodsOrder(common.env('BASE_URL_CORE'))

if __name__ == '__main__':
    # goods_order.demolition_order()
    goods_order.pay_callback_suc('202107011506220954618219')