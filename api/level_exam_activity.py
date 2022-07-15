#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 16:30

from base.base_request import BaseRequest
from faker_util import fakerist
from util import assert_util
from util import auth_util
from util import common_util
from util.data_util import data_pool


class LevelExamActivity(BaseRequest):

    def __init__(self, root_url, **kwargs):
        super(LevelExamActivity, self).__init__(root_url, **kwargs)

    def save(self, kwargs):
        self.req_method = 'POST'
        self.req_url = '/levelExamActivityManager/save'
        self.req_body = kwargs
        self.req_cookies = {
            'api_account_token': auth_util.get_token('crm', 'api_account_token'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


level_exam_activity = LevelExamActivity(common_util.env('DOMAIN_GZ') + '/gzactivity')

if __name__ == '__main__':
    kwargs = data_pool.supply('channel.yml', 'add_channel')[0]
    kwargs['name'] = fakerist.word()
    res1 = level_exam_activity.save(**kwargs)
    assert res1.status is True
