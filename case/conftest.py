import allure
import pytest
import yaml

import common_util
from api.account import account
from api.user import user
from data_util import data_pool
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
    # tmp_func = str(metafunc.definition)
    cur_func = str(metafunc.definition).split(' ')[1][:-1]
    # tmp_module_cls = str(metafunc.cls)
    cur_module = f"{str(metafunc.cls).split('.')[-2]}.yml"
    # cur_cls = tmp_module_cls.split('.')[-1][:-2]

    # harry = data_pool.supply(cur_module, cur_func)
    harry = _auto_supply(cur_module, cur_func)

    # 1通过mark标记来匹配，不需要固定函数入参名
    name_list = (make.name for make in metafunc.definition.own_markers)
    if param_name in name_list and 'parametrize' not in name_list:
        metafunc.parametrize(param_name, harry, scope="function")

    # 2通过函数入参来匹配
    # if "_kwargs" in metafunc.fixturenames:
    #     metafunc.parametrize("_kwargs", harry, scope="function")


@pytest.fixture(scope="function")
def lzp(request):
    func_sign_1 = str(request.function).split(' ')
    logger.info(func_sign_1)
    sun_sign = []

    # name_module = func_sign_1[4].split('.')[-2]
    name_module_tmp = 'sample_data'
    name_module = name_module_tmp + '.yml'
    logger.info('模块名：' + name_module)
    sun_sign.append(name_module)

    # name_cls = func_sign_1[2].split('.')[-2]
    name_cls = 'TestZeusMongo'
    logger.info('类名：' + name_cls)
    sun_sign.append(name_cls)

    # name_func = func_sign_1[2].split('.')[-1]
    name_func = 'test_reset_pwd2'
    logger.info('方法名：' + name_func)
    sun_sign.append(name_func)

    kwargs = data_pool.supply(sun_sign[0], sun_sign[2])
    return kwargs


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
