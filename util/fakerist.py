# coding     : utf-8
# @Time      : 2021/5/5 上午12:59

from faker import Faker

# 语言环境
# fake = Faker(['zh_CN', 'en_US', 'ja_JP'])

fakerist = Faker('zh_CN')

if __name__ == '__main__':
    print(fakerist.name())
