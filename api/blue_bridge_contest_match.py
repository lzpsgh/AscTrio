# -*- coding: utf-8 -*-
# @Time    : 2021/4/6
# 模版文件，仅供参考

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class BBCMatch(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(BBCMatch, self).__init__(root_url, **kwargs)

    def req_get(self, **kwargs):
        self.req_method = 'GET'
        self.req_url = '/core/account/login'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
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
    pass
    # bbc_match.new_subject()
