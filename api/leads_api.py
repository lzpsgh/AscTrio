from config import envar
from core.base_request import BaseRequest

api_root_url = envar.BASE_URL_CORE


class LeadsAPI(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(LeadsAPI, self).__init__(api_root_url, **kwargs)

    # todo 将api层的method和url抽到data层
    def get_token(self, **kwargs):
        return self.request("GET", "/leadsApi/getToken", **kwargs)
        # return self.request(
        #     apier.get(self.__function__).get('method'),
        #     apier.get(self.__function__).get('url')
        # )

    def upload(self, **kwargs):
        return self.request("POST", "/leadsApi/upload", **kwargs)
        # return self.request(
        #     apier.get(self.__function__).get('method'),
        #     apier.get(self.__function__).get('url')
        # )


leads_api = LeadsAPI(api_root_url)
