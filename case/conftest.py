import allure
import pytest

from account import account
from user import user
from util import common
from util.logger import logger
from util.mysql_operate import db
from util.read_data import datapool

BASE_PATH = common.env('PROJECT_ROOT')


# 是get_data的升级增强版，不带参数默认会用当前类的当前函数来跟踪定位相应的数据源，也支持指定
# @pytest.fixture(scope="function")
# def supply(yml_name, yml_key):
#     # aaa = inspect.stack()
#     # print('类名是：'+aaa[1][3])  # TestScoringDimension
#     # print('函数名是：'+aaa[0][3])  # supply
#     # 获取被调用函数所在模块文件名
#     # print(sys._getframe().f_code.co_filename)
#     # 获取被调用函数名称
#     # print(sys._getframe().f_code.co_name)
#     try:
#         # data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
#         yaml_file_path = f"{BASE_PATH}/data/{yml_name}"
#         yaml_data = datapool.load_yml(yaml_file_path)
#         if yml_key is not None:
#             yaml_dict = yaml_data.get(yml_key)
#             return yaml_dict
#         else:
#             raise BaseException("yml中无此键名")
#     except Exception as ex:
#         pytest.skip(str(ex))


def get_data(yaml_file_name):
    try:
        # data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_file_path = f"{BASE_PATH}/data/{yaml_file_name}"
        yaml_data = datapool.load_yml(yaml_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")
leadsapi_data = get_data("leadsapi_test_data.yml")
user_data = get_data("test_user.yml")
get_add_leads_data = get_data("test_add_leads.yml")
bbc_data = get_data("test_bbc_signup.yml")

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


@pytest.fixture(scope="session")
def crm_login_with_mm():
    login_info = account.crm_login_with_mm()
    # yield login_info.json()


@pytest.fixture(scope="session")
def login_fixture():
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": username,
        "password": password
    }
    loginInfo = user.login(data=payload, headers=header)
    step_login(username, password)
    yield loginInfo.json()


@pytest.fixture(scope="function")
def insert_delete_user():
    """删除用户前，先在数据库插入一条用户数据"""
    insert_sql = base_data["init_sql"]["insert_delete_user"][0]
    db.execute_db(insert_sql)
    step_first()
    logger.info("删除用户操作：插入新用户--准备用于删除用户")
    logger.info("执行前置SQL：{}".format(insert_sql))
    yield
    # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
    del_sql = base_data["init_sql"]["insert_delete_user"][1]
    db.execute_db(del_sql)
    step_last()
    logger.info("删除用户操作：手工清理处理失败的数据")
    logger.info("执行后置SQL：{}".format(del_sql))


@pytest.fixture(scope="function")
def delete_register_user():
    """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = base_data["init_sql"]["delete_register_user"]
    db.execute_db(del_sql)
    step_first()
    logger.info("注册用户操作：清理用户--准备注册新用户")
    logger.info("执行前置SQL：{}".format(del_sql))
    yield
    db.execute_db(del_sql)
    step_last()
    logger.info("注册用户操作：删除注册的用户")
    logger.info("执行后置SQL：{}".format(del_sql))


@pytest.fixture(scope="function")
def update_user_telephone():
    """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
    update_sql = base_data["init_sql"]["update_user_telephone"]
    db.execute_db(update_sql)
    step_first()
    logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
    logger.info("执行SQL：{}".format(update_sql))


if __name__ == '__main__':
    # scoring_dimension.modify_scoring_dimension(3, 2, 30, "aaaaa")
    # print(loee)
    pass
