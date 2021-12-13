from base.base_request import BaseRequest
from data_util import data_pool
from mysql_util import mysqler
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
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers,
            data=self.req_body
        )
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

    def update_coupon(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/goodsOrder/update'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
            # 'exam_token': auth_util.get_token('bbc', 'exam_token'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result


goods_order = GoodsOrder(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    # 微信支付回调
    # goods_order.pay_callback_suc('202112101213017854754781')
    # 取消订单
    # goods_order.cancel_order('51796')

    # 创建订单
    kwargs0 = data_pool.supply('goods_order_data.yml', 'demolition_order_omo')[0]
    kwargs0['userId'] = '155863'  # 用户的userid
    kwargs0['goodsIds'] = '765'  # 2元的K2D
    kwargs0['orderSource'] = 'SCHOOL_ORDER'
    res0 = goods_order.demolition_order(**kwargs0)
    assert res0.status is True

    sql = 'SELECT id FROM usercoupon uc WHERE userId = {userId} AND couponRule = {couponId};'
    couponIds = mysqler.query(sql)
    # 更新订单:绑定优惠券
    kwargs = data_pool.supply('goods_order_data.yml', 'update_coupon')[0]
    kwargs['couponIds'] = '155863'  # usercoupon表的id
    kwargs['orderId'] = '51895'  #
    kwargs['payStyle'] = 'NATIVE'
    kwargs['payType'] = 'WX'
    res1 = goods_order.update_coupon()
    assert res1.status is True
