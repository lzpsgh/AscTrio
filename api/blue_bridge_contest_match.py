# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class BBCMatch(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(BBCMatch, self).__init__(root_url, **kwargs)

    # 登录答题页面-正式考试
    def exam_login(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzlqb/scienceart/user/login'
        self.req_body = kwargs
        self.req_cookies = {
            'exam_token': auth_util.get_bbc_token('crm'),
        }
        result = self.request(
            method='POST', url=self.req_url, headers=self.req_headers,
            data=self.req_body)
        assert_util.result_check(result)
        # auth_util.set_cookie('bbc', result.rsp.cookies["exam_token"])
        auth_util.set_token('bbc', 'exam_token', result.rsp.cookies["exam_token"])
        return result

    # 启用考试
    def enable_exam(self, exam_id):
        self.req_method = 'POST'
        self.req_url = '/gzlqb/scienceart/examination/enable'
        self.req_body = {
            "id": exam_id,
            "enable": 1
        }
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.request(
            method='POST', url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            data=self.req_body)
        assert_util.result_check(result)
        return result

    # 新建考试
    def add_exam(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzlqb/scienceart/examination/examinationAdd'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 新建试卷
    def add_paper(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzlqb/scienceart/paper/add'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 新建题目
    def new_subject(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzlqb/scienceart/subject/newSubject'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_bbc_token('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


bbc_match = BBCMatch(common_util.env('BASE_URL_GZ'))

if __name__ == '__main__':
    kwargs = data_pool.supply('bbc_contest_data.yml', 'new_subject_single')[0]
    bbc_match.new_subject(**kwargs)
