# coding     : utf-8
# @Time      : 2021/5/5 上午12:59

from faker import Faker

# 语言环境
# fake = Faker(['zh_CN', 'en_US', 'ja_JP'])

fakerist = Faker(locale='zh_CN')
# print(fakerist.address())#海南省成市丰都深圳路p座 425541


if __name__ == '__main__':
    print(fakerist.name())
    print(fakerist.city())
    print(fakerist.email())
    print(fakerist.street_address())
