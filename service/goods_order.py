from api.goods_order import goods_order
from core.result_base import ResultBase
from util.logger import logger
from util.mysql_operate import db


def pay_callback_suc(out_trade_no):
    """
    获取系统token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    # data = {
    #     "secret": secret
    # }
    # headers = {
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    #     "Cookie": "JSESSIONID=75924353CD4B94499927E2307FEE0065; acgtgt_rm=t; acgt_ae=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgt_an=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgtgt_c=5F9A66565E5023347EA5B8C8D34AB210F24DE7D1FA835926F0776F51; ddx_ye=DE51CC2B2447134982462C471C830C51; gtgt_rm=t; ddxs_cc=CBA4A3006A8ABC706F98A2B6F8892CC2; gt_pp=CBA4A3006A8ABC706F98A2B6F8892CC2; token=api_token_CBA4A3006A8ABC706F98A2B6F8892CC2; gtgt_c=8882F391ABF5CE28B8B44D9BA33621FB54E019E374678EADDECE1177"
    # }
    # res = goods_order.pay_callback_suc(params=data, headers=headers)
    res = goods_order.pay_callback_suc(out_trade_no)
    result.success = False
    if res.json()["code"] == '0000':
        result.success = True
        logger.info(res.json())
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()["message"]
    result.response = res
    return result


def is_use_coupon(goods_order_id):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Cookie": "JSESSIONID=7E905BAE0E302B54F4412ECFECA3C72B; acgtgt_rm=t; acgt_ae=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgt_an=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgtgt_c=5F9A66565E5023347EA5B8C8D34AB210F24DE7D1FA835926F0776F51; ddx_ye=DE51CC2B2447134982462C471C830C51; gtgt_rm=t; ddxs_cc=CBA4A3006A8ABC706F98A2B6F8892CC2; gt_pp=CBA4A3006A8ABC706F98A2B6F8892CC2; token=api_token_CBA4A3006A8ABC706F98A2B6F8892CC2; gtgt_c=8882F391ABF5CE28B8B44D9BA33621FB54E019E374678EADDECE1177"
    }

    result = ResultBase()
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
    pay_callback_suc(db.select_db(sql_orderno)[0][0])
