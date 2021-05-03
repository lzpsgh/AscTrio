# coding     : utf-8
# @Time      : 2021/4/25 下午10:28

from base.base_request import BaseRequest
from util import asserter
from util import auth
from util import common


class Project(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Project, self).__init__(api_root_url, **kwargs)

    # 提交作品
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
            # "Host": "sit.miaocode.com",
            # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
            "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('gz'),
        }
        # todo 怎么处理files类型参数
        result = self.x_request()
        asserter.result_check(result)
        return result


project = Project(common.env('BASE_URL_GZ'))

if __name__ == '__main__':
    project.save_competition_project('66')
