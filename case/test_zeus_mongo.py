#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from conftest import lzp
from util.data_util import data_pool
from util.log_util import logger


@allure.feature("")
class TestZeusMongo:

	# 用hook函数来参数化, 未调试过和parametrize和fixture共同使用的场景
	def test_auto_supply(self, __kwargs):
		print(__kwargs)

	# 叠加parametrize. case层可以直接调用api层
	@pytest.mark.parametrize('api_id', ['10023'])
	@pytest.mark.parametrize('kwargs', data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
	def test_double_parametrize(self, api_id, kwargs):
		# res = base_api(sapidata, kwargs)
		# return res
		print(kwargs["phone"] + api_id)

	# 叠加parametrize. case层接受参数，调用server层
	@pytest.mark.parametrize('api_id', ['10023'])
	@pytest.mark.parametrize('kwargs', data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
	def test_double_parametrize(self, api_id, kwargs):
		# res = base_api(apidata, kwargs)
		# return res
		print(kwargs["phone"] + api_id)

	# 以前的case层，需要创建api层代码，然后在这里关联api层模块
	@pytest.mark.skip
	@pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login2'))
	def test_exam_login(self, kwargs):
		kwargs['examId'] = 'e0e684cd-5e9e-476c-89c4-9e99437ebfe8'  # 考试id对应的uuid
		kwargs['identityType'] = 'IDCARD'
		kwargs['identityNo'] = '371325198509024721'
		# res = bbc_match.exam_login(**kwargs)
		res = 0
		assert res.status is True

	# 方案0：在parametrize里指定2个参数，不合理，kwargs里的多个字段都要使用同一个接口的
	# 方案1： 在函数签名后加上fixture参数，不方便，需要进函数内部修改
	@pytest.mark.parametrize("kwargs", ['001', '002', '003'])
	def test_lensaclrtn(self, kwargs, fix_bind_api):
		print('test_lensaclrtn主体' + kwargs)
		res = base_api(fix_bind_api('12233'), kwargs)
		return res

	# 优化方案2： 自己写个注解，不确定和pytest原有装饰器共用是否会有什么问题，而且参数传递和处理流程不明
	# @deco.find_bind_api('12333')
	@pytest.mark.parametrize("kwargs", ['001', '002', '003'])
	def test_lensaclrtn(self, kwargs, fix_bind_api):
		print('test_lensaclrtn主体' + kwargs)
		res1 = base_api.get(api_data, kwargs)
		return res

	# 优化方案3： 将kwargs的值传到fixture中包装，然后再传回函数。
	# @pytest.mark.parametrize('kwargs', data_pool.supply("aaa.yml", 'keyword')[0])
	# @pytest.mark.usefixtures('bind_api')
	# def test_lensaclrtn(self, kwargs, bind_api):
	#     print('test_lensaclrtn主体' + kwargs)
	#     return res

	# 完整流程,执行前需修改【报名活动id，试卷id，考试id】
	@pytest.mark.skip
	@pytest.mark.parametrize("kwargs", data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
	@pytest.mark.usefixtures("crm_login_with_mm", "h5_login")
	def test_submit_pay_audit(self, kwargs):
		match_id = '90'
		paper_id = '65'
		exam_id = '89'
		pass

	@pytest.mark.parametrize('kwargs', [lzp])
	def test_pytest_collect_file(self, kwargs):
		# print("hello", path)
		# sun_sign_ret = lzp
		# print(sun_sign_ret)
		logger.info(kwargs)
# logger.info('')  # function node class
# func_sign_1 = str(lzp.function).split(' ')
# logger.info(func_sign_1)
# logger.info('方法名：' +func_sign_1[2].split('.')[-1])
# logger.info('类名：' +func_sign_1[2].split('.')[-2])
# logger.info('模块名：' +func_sign_1[4].split('.')[-2])


if __name__ == '__main__':
	pass

# [2022-04-05 01:17:21,128] [test_leads_pay.py 32][INFO ] <Function test_pytest_collect_file>
# [2022-04-05 01:17:21,129] [test_leads_pay.py 33][INFO ] <bound method TestLeadsPay.test_pytest_collect_file of <case.user.test_leads_pay.TestLeadsPay object at 0x7fb2c855c5c0>>
# [2022-04-05 01:17:21,129] [test_leads_pay.py 34][INFO ] <class 'case.user.test_leads_pay.TestLeadsPay'>

# [2022-04-05 01:26:33,778] [test_leads_pay.py 32][INFO ] <class '_pytest.python.Function'>
# [2022-04-05 01:26:33,778] [test_leads_pay.py 33][INFO ] <class 'method'>
# [2022-04-05 01:26:33,779] [test_leads_pay.py 34][INFO ] <class 'type'>
