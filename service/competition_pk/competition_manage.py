# coding     : utf-8
# @Time      : 2021/4/12 下午6:09
from api.competition_pk.competition_manage import competition_manage
from core.result_base import ResultBase
from util import auth
from util.mysql_operate import db


# 新建修改赛事
def save_competition():
    result = ResultBase()
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
        "synopsis": "asctrio-赛事主要是做什么\n法俄撒粉色\n结束了",
        "coOrganiser": "协办22-asctrio",
        "organizer": "主办11-asctrio",
        "callForPapersStartTime": "2021-04-16 00:00:00",
        "callForPapersEndTime": "2021-04-19 23:59:59",
        "promotionStartTime": "2021-04-20 00:00:00",
        "promotionEndTime": "2021-04-23 23:59:59",
        "themeList": [
            {
                "subjectName": "作品和1",
                "subjectType": "0",
                "learningVideo": "https://www.baidu.com",
                "projectId": "935522"
            }
        ],
        "bestWorksQuota": 1,
        "excellentWorksQuota": 0,
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
        "popularityAwardQuota": 2,
        "weekPopularityAwardQuota": 3,
        "competitionName": "asctrio046"
    }
    req_cookies = {
        'JSESSIONID': auth.get_cookie('crm'),
    }
    res = competition_manage.save_competition(json=req_data, cookies=req_cookies)
    result.status = False
    if res.status_code == 200 and res.json()['success'] is True:
        cid = db.select_db('select id FROM competition where competition_name = \'asctrio046\' ')[0][0]
        if cid is not None:
            print(cid)
            result.status = True
    result.response = res


if __name__ == '__main__':
    save_competition()
