#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 下午2:48

from datetime import date, datetime, timedelta

# time.localtime()  # time.struct_time(tm_year=2019, tm_mon=8, tm_mday=23, tm_hour=18, tm_min=57, tm_sec=0, tm_wday=4, tm_yday=235, tm_isdst=0)

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 年月日 时分秒

day = date.today()  # 获取今日日期，只显示年-月-日

now = datetime.now()  # 获取当前日期以及时间（年-月-日-时-分-秒.微秒）

after_day = now + timedelta(days=3)  # 获取3天后的日期以及时间
after_hour = now + timedelta(hours=1)  # 获取当前时间1小时后的时间
after_minu = now + timedelta(minutes=3)  # 获取当前时间3分钟后的时间
after_week = now + timedelta(weeks=1)  # 获取当前时间1周后的时间


def get_ymdhms():
    return now.strftime("%Y%m%d-%H%M%S")


def get_mdhms():
    return now.strftime("%m%d-%H%M%S")


def after_min(minute=3):
    after_minu = now + timedelta(minutes=minute)  # 获取当前时间x分钟后的时间
    return after_minu.strftime("%Y-%m-%d %H:%M:%S")

# 同理“+”变成“-”，就是获取过去的时间
# 如果用年月日+未来或过去的时间，就不显示时分秒，只显示年月日
# print("未来一周的日期是：%s" % after_week.strftime("%Y-%m-%d"))
