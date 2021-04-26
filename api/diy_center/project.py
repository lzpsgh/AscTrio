# coding     : utf-8
# @Time      : 2021/4/25 下午10:28

from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_GZ


class Project(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(Project, self).__init__(api_root_url, **kwargs)

    # 提交作品
    def save_competition_project(self, **kwargs):
        return self.request("POST", "/gzproject/project/saveCompetitionProject", **kwargs)


project = Project(api_root_url)
