# coding     : utf-8
# @Time      : 2021/4/12 下午6:09
from api.competition_pk.competition_manage import competition_manage
from base.base_result import BaseResult
from util import auth
from util.mysql_operate import db


# 新建修改赛事
def save_competition():
    result = BaseResult()
    req_data = {
        "bannerList": [
            {
                "competitionId": "",
                "type": 2,
                "url": "https://res.miaocode.com/competition/1618467496618",
                "serialNum": 1
            },
            {
                "competitionId": "",
                "type": 2,
                "url": "https://res.miaocode.com/competition/1618467500999",
                "serialNum": 2
            },
            {
                "competitionId": "",
                "type": 2,
                "url": "https://res.miaocode.com/competition/1618467503896",
                "serialNum": 3
            },
            {
                "competitionId": "",
                "type": 1,
                "url": "https://res.miaocode.com/competition/1618467516939",
                "serialNum": 1
            }
        ],
        "synopsis": "赛事主要是做什么\n法俄撒粉色\n结束了",
        "coOrganiser": "协办方，asctrio",
        "organizer": "主办方，asctrio",
        "callForPapersStartTime": "2021-04-22 00:00:00",
        "callForPapersEndTime": "2021-05-16 23:59:59",
        "promotionStartTime": "2021-05-17 00:00:00",
        "promotionEndTime": "2021-06-06 23:59:59",
        # 评分时间 06-07到06-11
        "weekPopularityAwardQuota": 1,
        "popularityAwardQuota": 2,
        "bestWorksQuota": 8,
        "excellentWorksQuota": 37,
        "themeList": [
            {
                "subjectName": "主题11",
                "subjectType": "0",
                "learningVideo": "www.bing.com",
                "projectId": "935522"
            }
        ],
        "judgesList": [
            {
                "accountId": "182",
                "realName": "胡晶晶",
                "competitionId": ""
            },
            {
                "accountId": "3301",
                "realName": "李兆鹏",
                "competitionId": ""
            }
        ],
        "scoringDimensionIds": "16,18,17",
        "officialBanner": "https://res.miaocode.com/competition/1618467493120",
        "h5Banner": "https://res.miaocode.com/competition/1618467508602",
        "ageMax": 9,
        "ageMin": 1,
        "competitionName": "临时444"  # asctrio赛事27
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = competition_manage.save_competition(json=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200 and res.json()['success'] is True:
        cid = db.select_db('select id FROM competition where competition_name = \'临时444\' ')[0][0]
        if cid is not None:
            print(cid)
            result.status = True
    result.response = res


if __name__ == '__main__':
    save_competition()
