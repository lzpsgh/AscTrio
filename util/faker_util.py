# coding     : utf-8
# @Time      : 2021/5/5 上午12:59

from faker import Faker
from faker.providers import BaseProvider


# 语言环境
# fake = Faker(['zh_CN', 'en_US', 'ja_JP'])


class MySex(BaseProvider):
    def sex(self):
        sexs = ['M', 'F']
        return sexs


fakerist = Faker(locale='zh_CN')
fakerist.add_provider(MySex)

if __name__ == '__main__':
    print(fakerist.name())
    print(fakerist.city())
    print(fakerist.email())
    print(fakerist.street_address())
