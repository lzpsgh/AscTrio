import leads_api
import user
from base.base_result import BaseResult
from util.log_kit import logger


def get_token(secret: str):
    """
    获取系统token
    :return: 自定义的关键字返回结果 result
    """
    result = BaseResult()
    data = {
        "secret": secret
        # "secret": data_poster.req_params.secret
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Cookie": "JSESSIONID=75924353CD4B94499927E2307FEE0065; acgtgt_rm=t; acgt_ae=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgt_an=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgtgt_c=5F9A66565E5023347EA5B8C8D34AB210F24DE7D1FA835926F0776F51; ddx_ye=DE51CC2B2447134982462C471C830C51; gtgt_rm=t; ddxs_cc=CBA4A3006A8ABC706F98A2B6F8892CC2; gt_pp=CBA4A3006A8ABC706F98A2B6F8892CC2; token=api_token_CBA4A3006A8ABC706F98A2B6F8892CC2; gtgt_c=8882F391ABF5CE28B8B44D9BA33621FB54E019E374678EADDECE1177"
    }
    res = leads_api.get_token(params=data, headers=headers)
    result.success = False
    if res.json()["code"] == '0000':
        result.success = True
        logger.info(res.json()['data'])
        # print(res.json()["data"])
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()["message"]
    result.response = res
    return result


def upload_info(username, channel, phone="", name="", purchaseTime="", token=""):
    """
    注册用户信息
    :param username: 用户名
    :param password: 密码
    :param telephone: 手机号
    :param sex: 性别
    :param address: 联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = BaseResult()
    json_data = {
        "username": username,
        "channel": channel,
        "phone": phone,
        "name": name,
        "purchaseTime": "2021-01-04 20:09:00",
        "token": "token_a60a7e5714cd4e3fb300317652990184",
    }
    header = {
        "Content-Type": "application/json",
        "Host": "sit.miaocode.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "DNT": "1",
        "Origin": "https://sit-crm.miaocode.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sit-crm.miaocode.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "JSESSIONID=7516D121823CF2F4EEA97EC48A5CB16D; acgtgt_rm=t; acgt_ae=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgt_an=AE73B820F68F421D67B1905E48015213ECC913578E81D4056E1BCBEB60CF5D93; acgtgt_c=5F9A66565E5023347EA5B8C8D34AB210F24DE7D1FA835926F0776F51; ddx_ye=DE51CC2B2447134982462C471C830C51; gtgt_rm=t; ddxs_cc=CBA4A3006A8ABC706F98A2B6F8892CC2; gt_pp=CBA4A3006A8ABC706F98A2B6F8892CC2; token=api_token_CBA4A3006A8ABC706F98A2B6F8892CC2; gtgt_c=8882F391ABF5CE28B8B44D9BA33621FB54E019E374678EADDECE1177",
    }
    res = user.register(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == '0000':
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


if __name__ == '__main__':
    get_token("w@qB^qxXHhYkLdEJOTEeWigR4rbpm8Ja")
