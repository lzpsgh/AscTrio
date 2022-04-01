#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import allure
import pytest

from util.data_util import data_pool


@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
# @pytest.mark.usefixtures
class TestZeusMongo:

	# 叠加parametrize. case层可以直接调用api层
	@pytest.mark.parametrize('api_id', ['10023'])
	@pytest.mark.parametrize('kwargs',
							 data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
	def test_double_parametrize(self, api_id, kwargs):
		# res = base_api(sapidata, kwargs)
		# return res
		print(kwargs["phone"] + api_id)

	# 叠加parametrize. case层接受参数，调用server层
	@pytest.mark.parametrize('api_id', ['10023'])
	@pytest.mark.parametrize('kwargs',
							 data_pool.supply('bbc_user_batch.yml', 'user_submit_and_login3'))
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


if __name__ == '__main__':
	pass
