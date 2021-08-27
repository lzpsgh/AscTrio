from base.base_request import BaseRequest
from util import assert_util
from util import auth_util
from util import common_util


class LeadsAPI(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(LeadsAPI, self).__init__(api_root_url, **kwargs)

    def get_token(self):
        self.req_method = 'GET'
        self.req_url = '/core/leadsApi/getToken'
        self.req_body = {
            "secret": 'w@qB^qxXHhYkLdEJOTEeWigR4rbpm8Ja'
        }
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('web'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result

    def upload_info(self, **kwargs):
        self.req_method = 'POST'
        self.req_url = '/core/leadsApi/upload'
        self.req_body = kwargs
        self.req_cookies = {
            'JSESSIONID': auth_util.get_cookie('crm'),
        }
        result = self.x_request()
        assert_util.result_check(result)
        return result


leads_api = LeadsAPI(common_util.env('DOMAIN_CORE'))

if __name__ == '__main__':
    leads_api.get_token()
    # leads_api.upload_info('token_9fcefa8a596b4434aac8c5ab051b5fa0')
