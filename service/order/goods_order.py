from base.base_response import BaseResponse
from goods_order import goods_order
from util import auth_kit
from util import common_kit
from util.log_kit import logger
from util.mysql_kit import mysqler

sql_query_userid = "select id from activityuser where phone = "
sql_query_tradeno = "SELECT outTradeNo FROM payrecord WHERE id = "
goodsIds = '373'  # 457是S0课799块 373是K1课5280块 305是py的S5课6000块 301是S1课5280块
pay_amount = '5280'  # 价格要同时改
order_no = 'O2105207930118'


# 官网-创建订单-微信支付
def demolition_order():
    req_data = {
        'couponIds': '',
        'goodsIds': '373',
        'payType': 'WX',
        'payStyle': 'NATIVE',
        'giveCourses': '',
        'giveOtherGifts': '',
        'orderSource': 'GUAN_WANG',
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('web'),
    }
    result = goods_order.send_sms2(params=req_data, headers=req_headers, cookies=req_cookies)
    common_kit.result_check(result)

    order_no = result.rsp.data
    logger.warning(order_no)
    return result


# 进入微信支付页下单
def get_pay_page():
    req_data = {
        'orderNo': 'O2105207930118',
        'payType': 'WX',
        'payStyle': 'NATIVE',
        'amount': '5280',
        'stageNum': '',
        'forwordUrl': 'https://sit-xuexi.miaocode.com/market/paySuccess',
        'cancelUrl': 'https://sit-xuexi.miaocode.com/order/457',
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('web'),
    }
    result = goods_order.send_sms2(params=req_data, headers=req_headers, cookies=req_cookies)
    common_kit.result_check(result)

    par_record_id = result.rsp.data.payrecordId  # 43893
    logger.warning(par_record_id)
    return result


# 微信支付模拟回调成功
def pay_callback_suc(out_trade_no):
    req_data = {
        'outTradeNo': '$sql_query_tradeno$pay_rec_id'
    }
    req_headers = {
        "Cache-Control": "no-cache",
    }
    req_cookies = {
        'JSESSIONID': auth_kit.get_cookie('web'),
    }
    result = goods_order.pay_callback_suc(params=req_data, headers=req_headers, cookies=req_cookies)
    common_kit.result_check(result)
    return result


def is_use_coupon(goods_order_id):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Cookie": "JSESSIONID=7E905BAE0E302B54F4412ECFECA3C72B; acgtgt_rm=t; acgt_ae=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgt_an=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgtgt_c=5F9A66565E5023347EA5B8C8D34AB210F24DE7D1FA835926F0776F51; ddx_ye=DE51CC2B2447134982462C471C830C51; gtgt_rm=t; ddxs_cc=CBA4A3006A8ABC706F98A2B6F8892CC2; gt_pp=CBA4A3006A8ABC706F98A2B6F8892CC2; token=api_token_CBA4A3006A8ABC706F98A2B6F8892CC2; gtgt_c=8882F391ABF5CE28B8B44D9BA33621FB54E019E374678EADDECE1177"
    }

    result = BaseResponse()
    res = goods_order.is_use_coupon(goods_order_id, headers=headers)
    result.has_coupon = False
    if res.json()["code"] == '000001':
        if len(res.json()["data"]["coupon"]) > 0:
            logger.info(res.json()["data"]["coupon"])
            logger.info(len(res.json()["data"]["coupon"]))
            result.has_coupon = True
    else:
        logger.info(len(res.json()["data"]["coupon"]))
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
        logger.info(len(res.json()["data"]["coupon"]))
    result.msg = res.json()["message"]
    result.response = res
    return result


if __name__ == '__main__':
    sql_orderno = "SELECT outTradeNo FROM payrecord WHERE payStatus = 'WAITING' AND payType = 'WX'"
    pay_callback_suc(mysqler.select_db(sql_orderno)[0][0])
