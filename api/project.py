# coding     : utf-8
# @Time      : 2021/4/25 下午10:28

from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class Project(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Project, self).__init__(api_root_url, **kwargs)

    # 提交作品（仅用于编程赛事作品pk）
    # 其Content-Type为multipart/form-data，需要使用files
    def save_competition_project(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzproject/project/saveCompetitionProject'
        self.req_body = kwargs
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('gz'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    # 保存作品
    def save_scratch_project_for_user(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/gzproject/project/saveScratchProjectForUser'
        self.req_body = kwargs
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'token': auth_util.get_cookie('gz'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            params=self.req_body
        )
        assert_util.result_check(result)
        project_id = result.sdata.get('id')
        return result

    # 发布作品
    # 其Content-Type为multipart/form-data，需要使用files
    def publish(self, **kwargs):
        self.req_method = 'PUT'
        self.req_url = '/gzproject/project/publish'
        self.req_body = kwargs
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'token': auth_util.get_cookie('gz'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            params=self.req_body
        )
        assert_util.result_check(result)
        return result


project = Project(common_util.env('BASE_URL_GZ'))

if __name__ == '__main__':
    # project.save_competition_project('67')

    project_name_1 = 'zuopin1'
    result_1 = project.save_scratch_project_for_user(project_name_1)
    assert result_1.status is True
    project_id_1 = result_1.sdata.get('id')
    result_2 = project.publish(project_name_1, project_id_1)
    assert result_2.sdata.get('status') == 'P'
