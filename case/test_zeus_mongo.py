#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import pytest

from data_util import data_pool


class TestZeusMongo:

	@pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'test_func_name'))
	# @pytest.mark.auto_kwargs
	def test_func_name(self, kwargs):
		print(kwargs)

	# @pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'submit_11'))
	@pytest.mark.auto_kwargs
	def test_11(self, auto_kwargs):
		print(auto_kwargs)

# @pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'submit_22'))
# @pytest.mark.auto_kwargs
# def test_22(self, kwargs):
# 	print(kwargs)

# 用 autoparam 来参数化, 会被 parametrize 覆盖
# @pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'test_single'))
# @pytest.mark.auto_kwargs
# def test_hook_supply_dict(self, auto_kwargs):
# 	print(auto_kwargs)

# @pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'test_single'))
# # @pytest.mark.auto_kwargs
# def test_hook_supply_dictaa(self, kwargs):
# 	print(kwargs)


# 通过该装饰器，将api信息传给case
# 注意要增加 @wrapper，保留元信息
# 1。写装饰器      			  @monor.mxcapi(10023)
# 2。在conftest里写fixture     @pytest.mark.usefixtures('monor')
# 3。在conftest里写hook函数     def pytest_generate_tests()
# @pytest.mark.usefixtures('monor')
# @pytest.mark.auto_kwargs
# @monor.mxcapi(10023)
# @monor.mxctoken()


if __name__ == '__main__':
	pass