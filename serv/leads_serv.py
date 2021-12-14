#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 上午10:38
from api.mxcuser import mxc_user
from util.data_util import data_pool
from util.faker_util import fakerist


# 创建B端OMO的leads
def add_omo_leads(phone):
    kwargs = data_pool.supply('mxcuser_data.yml', 'add_visit_leads')[0]
    kwargs['childName'] = 'Asc' + fakerist.word()
    kwargs['phone'] = phone
    res1 = mxc_user.add_visit_leads(**kwargs)
    userid = res1.sdata.get('userId')  # 4003926
    childName = res1.sdata.get('childName')  # Asc以及
    assert res1.status is True


if __name__ == '__main__':
    add_omo_leads('18899708135')
