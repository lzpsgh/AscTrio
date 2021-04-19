from base.base_request import BaseRequest
from config import envar

api_root_url = envar.BASE_URL_CORE


class User(BaseRequest):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def list_all_users(self, **kwargs):
        return self.request("GET", "/users", **kwargs)

    def list_one_user(self, username, **kwargs):
        return self.request("GET", "/users/{}".format(username), **kwargs)

    def register(self, **kwargs):
        return self.request("POST", "/register", **kwargs)

    def login(self, **kwargs):
        return self.request("POST", "/login", **kwargs)

    def update(self, user_id, **kwargs):
        return self.request("PUT", "/update/user/{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.request("POST", "/delete/user/{}".format(name), **kwargs)


user = User(api_root_url)
