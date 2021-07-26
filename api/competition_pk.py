#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 下午1:52

from base.base_request import BaseRequest
from util import assert_kit
from util import auth_kit
from util import common_kit
from util.log_kit import logger
from util.mysql_kit import mysqler


class CompetitionPK(BaseRequest):
    def __init__(self, api_root_url, **kwargs):
        super(CompetitionPK, self).__init__(api_root_url, **kwargs)

    # 提交报名信息
    def submit_enter_name_info(self, competitionId, age, countryCode, phone,
                               fullName, gender, certificateType, idNumber):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/submitEnterNameInfo'
        self.req_body = {
            "age": age,
            "countryCode": countryCode,
            "phone": phone,
            "fullName": fullName,
            "gender": gender,
            "certificateType": certificateType,
            "idNumber": idNumber,
            "competitionId": competitionId,
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('web'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 作品点赞
    def works_like(self, param1):
        self.req_method = 'POST'
        self.req_url = '/core/competitionEnterName/worksLike'
        self.req_body = {
            "id": param1
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('web'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 保存赛事
    def save_competition(self):
        self.req_method = 'POST'
        self.req_url = '/core/competitionManager/saveCompetition'
        self.req_body = {
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
            "callForPapersStartTime": "2021-05-12 00:00:00",
            "callForPapersEndTime": "2021-05-22 23:59:59",
            "promotionStartTime": "2021-05-23 00:00:00",
            "promotionEndTime": "2021-06-06 23:59:59",
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
            "ageMax": 11,
            "ageMin": 1,
            "competitionName": "赛事h5跳转"  # asctrio赛事27
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        cid = mysqler.query('select id FROM competition where competition_name = \'赛事h5跳转\' ')[0][0]
        if cid is not None:
            print(cid)
        return result

    # 启用/禁用
    # def enabled_state(self, **kwargs):
    #     return self.request("POST", "/competitionManager/enabledState", **kwargs)
    # 报名审核
    # def registration_review(self, **kwargs):
    #     return self.request("POST", "/competitionManager/registrationReview", **kwargs)

    # 删除评分维度
    def del_scoring_dimension_by_id(self, sd_id):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/delScoringDimensionById'
        self.req_body = {
            "id": sd_id
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # id获取评分维度
    def get_scoring_dimension_by_id(self, sd_id):
        self.req_method = 'GET'
        self.req_url = '/core/scoringDimension/getScoringDimensionById'
        self.req_body = {
            "id": sd_id
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 获取评分维度列表
    def get_scoring_dimension_list(self):
        self.req_method = 'GET'
        self.req_url = '/core/scoringDimension/getScoringDimensionList'
        self.req_body = {
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        return result

    # 保存评分维度-修改
    def save_scoring_dimension(self, sd_id, min_points, max_points, name):
        self.req_method = 'POST'
        self.req_url = '/core/scoringDimension/saveScoringDimension'
        self.req_body = {
            "id": sd_id,
            "maxPoints": max_points,
            "minPoints": min_points,
            "name": name
        }
        self.req_cookies = {
            'JSESSIONID': auth_kit.get_cookie('crm'),
        }
        result = self.x_request()
        assert_kit.result_check(result)
        finvalue = mysqler.query('SELECT min_points FROM scoring_dimension where id = 3')[0][0]
        if finvalue == 2:
            logger.info(finvalue)
        return result

    # 保存评分维度-新增
    # def save_scoring_dimension(self, min_points, max_points, name):
    #     self.req_method = 'POST'
    #     self.req_url = '/scoringDimension/saveScoringDimension'
    #     self.req_body = {
    #         # "id": sd_id,
    #         "maxPoints": max_points,
    #         "minPoints": min_points,
    #         "name": name
    #     }
    #     self.req_cookies = {
    #         'JSESSIONID': auth.get_cookie('crm'),
    #     }
    #     result = self.x_request()
    #     asserter.result_check(result)
    #     return result


cmpttn_pk = CompetitionPK(common_kit.env('BASE_URL'))

if __name__ == '__main__':
    # competition_enter.submit_enter_name_info('66', 8, '86', '18659107886', '随便用', 'M', "IDCARD", '441481199407171234')
    cmpttn_pk.submit_enter_name_info('67', 9, '86', '18659107886', 'z最终版', 'M', "IDCARD", '441481199407175678')
    # competition_enter.submit_enter_name_info('65', 7, '86', '18666024993', '签约客', 'M', "IDCARD", '441481199407173333')
