# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 上午9:15
# 模版文件，仅供参考，无法执行

from user import user
from util import auth_kit
from util.log_kit import logger
from util.mysql_kit import mysqler


def official_add_leads_1(phone):
    res0 = user.phone_exist(phone)
    if res0.sdata['isLeads'] is True:
        raise Exception('手机号已存在或其他原因')

    res1 = user.send_sms2(phone)
    if res1.status is False:
        raise Exception('验证码获取失败')

    res3 = user.booking_demo(phone)
    if res3.status is False:
        raise Exception('leads创建失败')
    core_jsessionid = res3.rsp.cookies["JSESSIONID"]
    auth_kit.set_cookie('web', core_jsessionid)

    user_id = mysqler.select_db("SELECT id FROM user WHERE phone=\'" + phone + "\'")[0][0]
    res4 = user.reset_pwd(user_id)

    logger.info(core_jsessionid)

    return res3


if __name__ == '__main__':
    # booking_demo()
    pass
