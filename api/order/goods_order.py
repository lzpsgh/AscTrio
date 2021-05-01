from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class GoodsOrder(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(GoodsOrder, self).__init__(api_root_url, **kwargs)

    # 官网-创建订单-微信支付
    def demolition_order(self, **kwargs):
        return self.request("POST", "/goodsOrder/demolitionOrder", **kwargs)

    # 进入微信支付页下单
    def get_pay_page(self, **kwargs):
        return self.request("POST", "/goodsOrder/getPayPage", **kwargs)

    # 微信支付模拟回调成功
    def pay_callback_suc(self, **kwargs):
        return self.request("GET", "/goodsOrder/simulationCallBack", **kwargs)

    # 忘了嘻嘻
    def is_use_coupon(self, **kwargs):
        return self.request("GET", "/goodsOrder/orderDetailForKK", **kwargs)


goods_order = GoodsOrder(api_root_url)
