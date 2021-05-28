# coding     : utf-8
# @Time      : 2021/4/25 下午10:28

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class Project(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Project, self).__init__(api_root_url, **kwargs)

    # 提交作品（仅用于编程赛事作品pk）
    # 其Content-Type为multipart/form-data，需要使用files
    def save_competition_project(self, competition_id):
        self.req_method = 'POST'
        self.req_url = '/gzproject/project/saveCompetitionProject'
        self.req_body = {
            "competitionId": competition_id,
            "comment": "来自AscTrio",
            "projectName": 'AscTrio11',
            "dataURL": 'https://res.miaocode.com/b2f78f02-8515-48ad-bd09-1768395b89b7.mxc',
            "thumbnailURL": 'https://res.miaocode.com/07b9d0ab-6a53-4373-95a3-ac01821890d8.png'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('gz'),
        }
        result = self.x_request()
        asserter.result_check(result)
        return result

    # 保存作品
    def save_scratch_project_for_user(self, project_name, id=None):
        self.req_method = 'POST'
        self.req_url = '/gzproject/project/saveScratchProjectForUser'
        self.req_body = {
            'projectName': project_name,
            'comment': '备注',
            # 'dataURL': 'https://res.miaocode.com/f4b35f3c-15b4-4a2e-a660-3d04b2ce4b1e.mxc',
            # 'thumbnailURL': 'https://res.miaocode.com/24a55eed-83e4-43a3-8b4f-0d55321b8abe.png'
            'dataURL': 'https://res.miaocode.com/464931e4-6a74-4abb-b31f-07d800cb6066.mxc',
            'thumbnailURL': 'https://res.miaocode.com/ca0339c4-6d3d-4d6c-978a-d5cdf0513db0.png'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'token': auth.get_cookie('gz'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            params=self.req_body
        )
        asserter.result_check(result)
        project_id = result.sdata.get('id')
        return result

    # 发布作品
    # 其Content-Type为multipart/form-data，需要使用files
    def publish(self, project_name, project_id):
        self.req_method = 'PUT'
        self.req_url = '/gzproject/project/publish'
        self.req_body = {
            'projectName': project_name,
            'projectId': project_id,
            'comment': '作品'+project+'描述随便'
        }
        self.req_headers = {
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'token': auth.get_cookie('gz'),
        }
        result = self.request(
            method=self.req_method, url=self.req_url, headers=self.req_headers, cookies=self.req_cookies,
            params=self.req_body
        )
        asserter.result_check(result)
        return result


project = Project(common.env('BASE_URL_GZ'))

if __name__ == '__main__':
    # project.save_competition_project('67')

    project_name_1 = 'zuopin1'
    result_1 = project.save_scratch_project_for_user(project_name_1)
    assert result_1.status is True
    project_id_1 = result_1.sdata.get('id')
    result_2 = project.publish(project_name_1, project_id_1)
    assert result_2.sdata.get('status') == 'P'
