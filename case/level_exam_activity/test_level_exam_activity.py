#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 16:32

import pytest

from api.level_exam_activity import level_exam_activity
from util.faker_util import fakerist


class TestLevelExamActivity:

    @pytest.mark.usefixtures("crm_login_with_mm")
    # @pytest.mark.usefixtures("upload_excel")
    @pytest.mark.auto_kwargs
    def test_save(self, auto_kwargs):
        auto_kwargs['activityName'] = 'Asc23' + fakerist.word()
        res = level_exam_activity.save(auto_kwargs)
        assert res.status is True


if __name__ == '__main__':
    pass
