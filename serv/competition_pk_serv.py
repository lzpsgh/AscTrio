#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
from competition_pk import cmpttn_pk
from faker_util import fakerist
from util.data_util import data_pool


# 新建赛事-不报名-groupid1
def save_cmp_nonreg_1():
    kwargs = data_pool.supply('project_pk_data.yml', 'save_competition')[0]
    kwargs['competitionName'] = 'Asc1发现' + fakerist.word() + ''
    kwargs['openRegistry'] = 0
    kwargs['callForPapersStartTime'] = '2021-12-20 00:00:00'
    kwargs['callForPapersEndTime'] = '2021-12-29 23:59:59'
    kwargs['promotionStartTime'] = '2021-12-20 00:00:00'
    kwargs['promotionEndTime'] = '2021-12-29 23:59:59'
    res = cmpttn_pk.save_competition(**kwargs)
    cmp_id = res.sdata  # 赛事ID
    if cmp_id is not None:
        return cmp_id


# 新建赛事-不报名-groupid13
def save_cmp_nonreg_13():
    kwargs = data_pool.supply('project_pk_data.yml', 'save_competition')[0]
    kwargs['competitionName'] = 'Asc13' + fakerist.word() + ''
    kwargs['openRegistry'] = 0
    kwargs['callForPapersStartTime'] = '2021-12-20 00:00:00'
    kwargs['callForPapersEndTime'] = '2021-12-27 23:59:59'
    kwargs['promotionStartTime'] = '2021-12-20 00:00:00'
    kwargs['promotionEndTime'] = '2021-12-28 23:59:59'
    res = cmpttn_pk.save_competition(**kwargs)
    cmp_id = res.sdata  # 赛事ID
    if cmp_id is not None:
        return cmp_id


# 新建赛事-不报名-groupid17
def save_cmp_nonreg_17():
    kwargs = data_pool.supply('project_pk_data.yml', 'save_competition')[0]
    kwargs['competitionName'] = 'Asc17' + fakerist.word() + ''
    kwargs['openRegistry'] = 0
    kwargs['callForPapersStartTime'] = '2021-12-20 00:00:00'
    kwargs['callForPapersEndTime'] = '2021-12-29 23:59:59'
    kwargs['promotionStartTime'] = '2021-12-20 00:00:00'
    kwargs['promotionEndTime'] = '2021-12-29 23:59:59'
    res = cmpttn_pk.save_competition(**kwargs)
    cmp_id = res.sdata  # 赛事ID
    if cmp_id is not None:
        return cmp_id


# 新建赛事-报名-groupid1
def save_cmp_reg_1():
    kwargs = data_pool.supply('project_pk_data.yml', 'save_competition')[0]
    kwargs['competitionName'] = 'Asc1报名' + fakerist.word() + ''
    kwargs['openRegistry'] = 1
    kwargs['callForPapersStartTime'] = '2021-12-20 00:00:00'
    kwargs['callForPapersEndTime'] = '2021-12-27 23:59:59'
    kwargs['promotionStartTime'] = '2021-12-28 00:00:00'
    kwargs['promotionEndTime'] = '2021-12-29 23:59:59'
    res = cmpttn_pk.save_competition(**kwargs)
    cmp_id = res.sdata  # 赛事ID
    if cmp_id is not None:
        return cmp_id


# def submit_enter_name_info_1():
#     self.req_method = 'POST'
#     self.req_url = '/core/account/submit'
#     self.req_body = kwargs
#     self.req_cookies = {
#         'JSESSIONID': auth_util.get_cookie('crm'),
#         'exam_token': auth_util.get_token('bbc', 'exam_token'),
#     }
#     result = self.request(
#         method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
#         json=self.req_body
#     )
#     assert_util.result_check(result)
#     return result

if __name__ == '__main__':
    # send_coupon_to_user('4003926', '4393')
    # order_detail('4003926', '765')
    pass
