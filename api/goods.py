# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 下午8:54

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit
from util.log_kit import logger

"""
courseType: RECORD
title: 真实拼团测试_线上课程_商品标题_CJ04
subtitle: 真实拼团测试_线上课程_商品标语_CJ04
classType: 0
courseLayer: E4,R1
lessonQty: 10
target: 1-13
type: HEAD
platFormType: 0
originprice: 5999
price: 2
headthumburl: https://res.miaocode.com/a21933d4-9aec-487a-9f31-8b04c8a46a77.jpg
h5HeadImgUrl: https://res.miaocode.com/0fca1f50-4fe8-4ab4-99e7-09687d86f3e2.jpg
detailPics: https://res.miaocode.com/049e56f8-a967-419b-8dc4-a2228fd4b810.jpg
detailPics: https://res.miaocode.com/92400e46-5c47-4560-8e91-39445ad3d000.png
detailPics: https://res.miaocode.com/59f55227-65f8-47bb-b9e1-03434a759b56.jpg
h5DetailPics: https://res.miaocode.com/6801be5a-908e-4849-b420-9ff729ef0b3a.jpg
installmentStatus: 0
installmentFee: 0
hbInstallmentStatus: 0
hbInstallmentFee: 0
codeLanguages: ,0,1,
goodsLessonQty: [{"courseLayer":"E4","lessonQty":5},{"courseLayer":"R1","lessonQty":5}]
recordCourseId: 92678,92692
"""


class Goods(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(Goods, self).__init__(root_url, **kwargs)

    def add_new_goods_singlecourse(self):
        self.req_method = 'POST'
        self.req_url = '/goods/addNewGoods'
        self.req_body = {
            'courseType': 'RECORD',
            'title': '标题录播课商品001',
            'subtitle': '标语录播课商品001',
            'classType': 0,
            'courseLayer': 'S5,S6',
            'lessonQty': '96',
            'target': '2-12',
            'type': 'HEAD',
            'platFormType': '1',
            'originprice': 2233,
            'price': 23,
            'headthumburl': 'https://res.miaocode.com/570a8f90-332c-40f1-bfd0-db17157ca751.jpg',
            'detailPics': 'https://res.miaocode.com/932f25ce-a82b-4585-a215-8ba2ca52a4dd.jpg',
            'installmentStatus': 0,
            'installmentFee': 0,
            'hbInstallmentStatus': 0,
            'hbInstallmentFee': 0,
            'codeLanguages': 1,
            'goodsLessonQty': [{"courseLayer": "S5", "lessonQty": 48}],
            'recordCourseId': '60709'
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body, cookies=self.req_cookies
        )

        assert_kit.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth_kit.set_cookie('crm', core_jsessionid)
        logger.debug(core_jsessionid)
        return result

    def add_new_goods_doublecourse(self):
        self.req_method = 'POST'
        self.req_url = '/goods/addNewGoods'
        self.req_body = {
            'courseType': 'RECORD',
            'title': '标题录播课商品001',
            'subtitle': '标语录播课商品001',
            'classType': 0,
            'courseLayer': 'S5,S6',
            'lessonQty': '96',
            'target': '2-12',
            'type': 'HEAD',
            'platFormType': '1',
            'originprice': 2233,
            'price': 23,
            'headthumburl': 'https://res.miaocode.com/570a8f90-332c-40f1-bfd0-db17157ca751.jpg',
            'detailPics': 'https://res.miaocode.com/932f25ce-a82b-4585-a215-8ba2ca52a4dd.jpg',
            'installmentStatus': 0,
            'installmentFee': 0,
            'hbInstallmentStatus': 0,
            'hbInstallmentFee': 0,
            'codeLanguages': 1,
            'goodsLessonQty': [{"courseLayer": "S5", "lessonQty": 48}],
            'recordCourseId': '60709'
        }
        result = self.request(
            method=self.req_method, url=self.req_url, data=self.req_body, cookies=self.req_cookies
        )
        assert_kit.result_check(result)
        core_jsessionid = result.rsp.cookies["JSESSIONID"]
        auth_kit.set_cookie('crm', core_jsessionid)
        logger.debug(core_jsessionid)
        return result


goods = Goods(common_kit.env('BASE_URL_CORE'))

if __name__ == '__main__':
    # account.crm_login_with_mm()
    goods.add_new_goods_singlecourse()
