# coding     : utf-8
# @Time      : 2021/4/25 下午11:10


from base.base_result import BaseResult
from project import project
from util import auth_kit


# 其Content-Type为multipart/form-data，需要使用files
def save_competition_project(competition_id):
    result = BaseResult()
    req_data = {
        "competitionId": competition_id,
        "comment": "来自AscTrio",
        "projectName": 'AscTrio11',
        "dataURL": 'https://res.miaocode.com/b2f78f02-8515-48ad-bd09-1768395b89b7.mxc',
        "thumbnailURL": 'https://res.miaocode.com/07b9d0ab-6a53-4373-95a3-ac01821890d8.png'
    }
    req_headers = {
        # "Host": "sit.miaocode.com",
        # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
        "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
    }
    req_cookies = {
        'token': auth_kit.get_cookie('gz')
    }
    res = project.save_competition_project(files=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["code"] == '000001':
            result.status = True
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':
    save_competition_project('66')
