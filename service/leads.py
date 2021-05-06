# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 上午9:15
# 模版文件，仅供参考，无法执行


from api.leads.leads import leads
from api.user.user import user
from util import auth


def official_add_leads_1(phone):
    res1 = user.send_sms2(phone)
    if res1.status is False:
        raise Exception('验证码获取失败')
    res2 = user.phone_exist(phone)
    if res2.sdata['isLeads'] is True:
        raise Exception('手机号已存在或其他原因')
    res3 = leads.booking_demo(phone)
    if res3.status is False:
        raise Exception('leads创建失败')
    core_jsessionid = res3.rsp.cookies["JSESSIONID"]
    auth.set_cookie('web', core_jsessionid)
    print(core_jsessionid)
    print(phone)


if __name__ == '__main__':
    # booking_demo()
    pass
