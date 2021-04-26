# coding     : utf-8
# @Time      : 2021/4/25 下午11:10


from api.diy_center.project import project
from base.base_result import BaseResult


# 注册用boundary，得引入第三方库来生成
def save_competition_project(competition_id):
    result = BaseResult()
    req_data = {
        "competitionId": competition_id,
        "comment": "第二次修改啦",
        "projectName": '第二次修改啦',
        "dataURL": 'https://res.miaocode.com/b2f78f02-8515-48ad-bd09-1768395b89b7.mxc',
        "thumbnailURL": 'https://res.miaocode.com/07b9d0ab-6a53-4373-95a3-ac01821890d8.png'
    }
    req_headers = {
        # "Host": "sit.miaocode.com",
        # "Connection": "keep-alive", #在HTTP1.1规范中默认开启
        "Content-Type": 'multipart/form-data; boundary=----WebKitFormBoundaryAoRHItbAqq1AUjaW'
    }
    req_cookies = {
        'token': 'registertoken49a8cfcd-ec20-44f6-bfce-8f49c83bc374'
    }
    res = project.save_competition_project(params=req_data, headers=req_headers, cookies=req_cookies)
    status_code = res.status_code
    resjson = res.json()

    if status_code == 200:
        if resjson["code"] == '000003':
            result.status = True
    else:
        print(status_code)
    result.response = res


if __name__ == '__main__':
    save_competition_project('53')
