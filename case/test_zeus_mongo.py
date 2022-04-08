#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 下午6:19

import pytest


class TestZeusMongo:

	# 用parametrize的处理方法
	# @pytest.mark.parametrize(
	# 	"kwargs", data_pool.supply('test_zeus_mongo.yml', 'test_hook_supply_dict'))
	# def test_old(self, kwargs):
	# 	print(kwargs)

	# 用 autoparam 来参数化, 会被 parametrize 覆盖
	# @pytest.mark.parametrize("kwargs", data_pool.supply('test_zeus_mongo.yml', 'test_single'))
	@pytest.mark.auto_kwargs
	def test_hook_supply_dict(self, auto_kwargs):
		print(auto_kwargs)


if __name__ == '__main__':
	pass