from base.base_request import BaseRequest
from config import envar
from util import auth
from util import common


class LeadsAPI(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(LeadsAPI, self).__init__(api_root_url, **kwargs)

    def get_token(self):
        self.req_method = 'GET'
        self.req_url = '/leadsApi/getToken'
        self.req_body = {
            "secret": 'w@qB^qxXHhYkLdEJOTEeWigR4rbpm8Ja'
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('web'),
        }
        result = self.x_request()
        common.result_check(result)
        return result

    def upload_info(self, token):
        self.req_method = 'POST'
        self.req_url = '/leadsApi/upload'
        self.req_body = {
            "username": 'aasdfa',
            "channel": 'channel666',
            "phone": '18888888879',
            "name": 'name8877',
            "purchaseTime": "2021-04-04 20:09:00",
            "token": token,
        }
        self.req_cookies = {
            'JSESSIONID': auth.get_cookie('crm'),
        }
        result = self.x_request()
        common.result_check(result)
        return result


leads_api = LeadsAPI(envar.BASE_URL_CORE)

if __name__ == '__main__':
    # leads_api.get_token()
    leads_api.upload_info('token_9fcefa8a596b4434aac8c5ab051b5fa0')
