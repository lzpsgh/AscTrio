from config import envar
from core.base_request import BaseRequest

api_root_url = envar.BASE_URL_CORE


class GoodsOrder(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GoodsOrder, self).__init__(api_root_url, **kwargs)

    def pay_callback_suc(self, out_trade_no, **kwargs):
        return self.request("GET", f"/goodsOrder/simulationCallBack?outTradeNo={out_trade_no}", **kwargs)

    def is_use_coupon(self, goods_order_id, **kwargs):
        return self.request("GET", f"/goodsOrder/orderDetailForKK?goodsOrderId={goods_order_id}", **kwargs)


goods_order = GoodsOrder(api_root_url)
