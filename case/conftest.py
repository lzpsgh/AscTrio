import allure
import pytest

from account import account
from user import user
from util.log_kit import logger
from util.mysql_kit import mysqler


# 在crm后台登录，获取cookies
@pytest.fixture(scope="session")
def crm_login_with_mm():
    login_info = account.crm_login()
    # yield login_info.json()


# 在h5后台登录，获取cookies
@pytest.fixture(scope="session")
def h5_login():
    login_info = user.get_current_user_nocookie()
    # yield login_info.json()


# 注册1个leads
def reg_leads(number):
    user.phone_exist()
    user.send_sms2()
    user.register()


# 注册1个正课用户
def reg_student():
    user.phone_exist()
    user.send_sms2()
    user.register()
    user.modify_users_owner()


# 已老用户身份登录并拿到cookie
def get_user_cookie():
    user.get_current_user()
    user.login()


# 获取1个leads
def get_old_leads(phone):
    mysqler.query("SELECT * FROM activityuser AS au WHERE au.phone = " + phone)
    # 执行数据库，从leads表里取n个leads


# 获取n个正课学员
def get_old_student(number):
    pass
    # 执行数据库，从student_schedule表里取n个正课学员

# BASE_PATH = common_kit.env('PROJECT_ROOT')
# def get_data(yaml_file_name):
#     try:
#         # data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
#         yaml_file_path = f"{BASE_PATH}/data/{yaml_file_name}"
#         yaml_data = data_pool.load_yml(yaml_file_path)
#     except Exception as ex:
#         pytest.skip(str(ex))
#     else:
#         return yaml_data
# base_data = get_data("base_data.yml")
# api_data = get_data("api_test_data.yml")
# scenario_data = get_data("scenario_test_data.yml")
# leadsapi_data = get_data("leadsapi_test_data.yml")
# user_data = get_data("test_user.yml")
# get_add_leads_data = get_data("test_add_leads.yml")
# bbc_data = get_data("data_bbc_signup.yml")
#
# @pytest.fixture(scope="session")
# def login_fixture():
#     username = base_data["init_admin_user"]["username"]
#     password = base_data["init_admin_user"]["password"]
#     header = {
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     payload = {
#         "username": username,
#         "password": password
#     }
#     loginInfo = user.login(data=payload, headers=header)
#     step_login(username, password)
#     yield loginInfo.json()
#
# @pytest.fixture(scope="function")
# def insert_delete_user():
#     """删除用户前，先在数据库插入一条用户数据"""
#     insert_sql = base_data["init_sql"]["insert_delete_user"][0]
#     mysqler.execute_db(insert_sql)
#     step_first()
#     logger.info("删除用户操作：插入新用户--准备用于删除用户")
#     logger.info("执行前置SQL：{}".format(insert_sql))
#     yield
#     # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
#     del_sql = base_data["init_sql"]["insert_delete_user"][1]
#     mysqler.execute_db(del_sql)
#     step_last()
#     logger.info("删除用户操作：手工清理处理失败的数据")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
# @pytest.fixture(scope="function")
# def delete_register_user():
#     """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
#     del_sql = base_data["init_sql"]["delete_register_user"]
#     mysqler.execute_db(del_sql)
#     step_first()
#     logger.info("注册用户操作：清理用户--准备注册新用户")
#     logger.info("执行前置SQL：{}".format(del_sql))
#     yield
#     mysqler.execute_db(del_sql)
#     step_last()
#     logger.info("注册用户操作：删除注册的用户")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
# @pytest.fixture(scope="function")
# def update_user_telephone():
#     """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
#     update_sql = base_data["init_sql"]["update_user_telephone"]
#     mysqler.execute_db(update_sql)
#     step_first()
#     logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
#     logger.info("执行SQL：{}".format(update_sql))

@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))


if __name__ == '__main__':
    pass
