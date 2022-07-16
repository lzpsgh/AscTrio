import allure
import pytest
import yaml

import common_util
from api.account import account
from api.user import user
from util.log_util import logger


def _auto_supply(file_name, key_name):
    # TODO 能从配置中读取 DATA_PATH
    DATA_PATH = common_util.env('DATA_PATH')

    yaml_file_path = f"{DATA_PATH}/{file_name}"
    try:
        with open(yaml_file_path, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        yaml_dict = yaml_data.get(key_name)
        if yaml_dict is not None:
            return yaml_dict
    except KeyError:
        raise f'未在yml中找到字段：{key_name}'
    except Exception:
        raise '''This call couldn't work.
            "Please consider raising an issue with your usage.")'''


# pytest hook函数
def pytest_generate_tests(metafunc):
    param_name = 'auto_kwargs'
    cur_module = f"{str(metafunc.cls).split('.')[-2]}.yml"
    cur_func = str(metafunc.definition).split(' ')[1][:-1]
    harry = _auto_supply(cur_module, cur_func)

    name_list = (make.name for make in metafunc.definition.own_markers)
    if param_name in name_list and 'parametrize' not in name_list:
        metafunc.parametrize(param_name, harry, scope="function")

@pytest.fixture(scope='function')
def upload_excel():
    # 上传文件
    pass

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


@pytest.fixture(scope="function")
def test_one_punch():
    print('ssss')
    list_a = [x ** 2 for x in range(101) if x % 10 == 0]
    return list_a


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
# def get_old_leads(phone):
#     mysqler.query("SELECT * FROM activityuser AS au WHERE au.phone = " + phone)
# 执行数据库，从leads表里取n个leads


# 获取n个正课学员
def get_old_student(number):
    pass
    # 执行数据库，从student_schedule表里取n个正课学员


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
