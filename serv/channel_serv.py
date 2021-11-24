#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 下午3:09

from api.channel import channel
from util.data_util import data_pool
from util.faker_util import fakerist


# 创建报名活动并开启
def add_channel_random():
    kwargs = data_pool.supply('channel.yml', 'add_channel')[0]
    fake = "Asctrio" + fakerist.month_name()
    kwargs['name'] = fake
    kwargs['code'] = fake
    res1 = channel.add_channel(**kwargs)
    return fake


if __name__ == '__main__':
    pass
