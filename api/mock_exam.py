# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 这个是从蓝桥杯考试系统中抽离出来的模拟考，可同时用于蓝桥杯和等级考，所有接口从gzlqb重新拷贝一份到gz_activity

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class MockExam(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(MockExam, self).__init__(root_url, **kwargs)

    # 新建知识点
    def new_knowpoint(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/exam/knowLedgePoint/insert'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 新建题目
    def new_subject(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/subject/newSubject'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 新建试卷
    def new_paper(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/paper/add'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 新增考试
    def new_exam(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/examination/examinationAdd'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            json=self.req_body
        )
        assert_util.result_check(result)
        return result

    # 启用考试
    def enable_exam(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/examination/enable'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body)
        assert_util.result_check(result)
        return result


mock_exam = MockExam(common_util.env('DOMAIN_GZ') + '/gzactivity')
# 'https://api-sit.miaocode.com/api'
# https://api-sit.miaocode.com/api/gzactivity/exam/knowledgePoint/page

if __name__ == '__main__':
    pass
    # 新建知识点
    # kwargs = data_pool.supply('mock_exam_data.yml', 'new_knowpoint')[0]  # 此时kwargs是dict类型
    # mock_exam.new_knowpoint(**kwargs)  # 通过**操作符将kwargs解包成 n个入参

    # 新建单选题
    # kwargs2 = data_pool.supply('mock_exam_data.yml', 'new_subject_scratch')[0]
    # kwargs2['subDescribe'] = '随机' + fakerist.word() + time_util.get_mdhms()
    # kwargs2['degree'] = 0
    # kwargs2['programType'] = 0  # 1 python 0图形化
    # kwargs2['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试
    # kwargs2['knowledgePointId'] = 593
    # mock_exam.new_subject(**kwargs2)

    # 新建试卷
    # kwargs3 = data_pool.supply('mock_exam_data.yml', 'new_paper_simple')[0]
    # kwargs3['programType'] = 0  # 1 python 0图形化
    # kwargs3['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试
    # kwargs3['name'] = '随机' + '2多选图形' + fakerist.word()
    # res3 = mock_exam.new_paper(**kwargs3)

    # 新增考试
    # kwargs4 = data_pool.supply('mock_exam_data.yml', 'new_exam')[0]
    # kwargs4['testpaperId'] = 121  # 修改试卷id
    # kwargs4['programType'] = 1  # 1 python 0图形化
    # kwargs4['examTypeId'] = 2  # 1 蓝桥杯66 2等级考试 其他
    # kwargs4['startTime'] = time_util.after_min(3)
    # kwargs4['endTime'] = "2021-11-15 16:30:00"
    # kwargs4['examName'] = '随机2单py' + fakerist.word() + time_util.get_mdhms()
    # res4 = mock_exam.new_exam(**kwargs4)
    # exam_id = res4.sdata
    # assert res4.status is True
    #
    # kwargs5 = data_pool.supply('mock_exam_data.yml', 'enable_exam')[0]
    # kwargs5['id'] = exam_id
    # kwargs5['enable'] = 1  # 启用考试
    # res5 = mock_exam.enable_exam(**kwargs5)
    # assert res5.status is True
