# coding     : utf-8
# @Time      : 2021/5/4 下午9:08

# 测试场景
# 测试正式课学员 使用积分抵扣购买新课


# 方案1
# 确保该手机号当前不存在，如果存在就跳过，不计入执行测试用例统计
# api：官网获取验证码（手机号）
# api：官网注册
# api：分配cc
# api：官网创建订单（商品id）（order_no）。注意这里要用相应人的cookie
# api：进入微信支付提交订单（order_no）（pay_rec_id）
# api：模拟回调成功（pay_rec_id）（200）
# api：使用积分抵扣购买新课
# res1 = user.phone_login()
# var1 = res1.getxx()
# res2 = leads.booking_demo(var1)
# var2 = res2.getyyy()
# assert var2 == 'adadf'
#
#
# 方案2
# 确保该手机号当前不存在，如果存在就跳过，不计入执行测试用例统计
# service： 新建一个正式课学员(手机号)，使用yml参数1
# service：官网创建订单（商品id）使用yml参数2
# api：使用积分抵扣购买新课
# @pytest.mark.parametrize()
# res11 = service1.asdadf()
# var11 = res11.getx()
# @pytest.mark.parametrize()
# res22 = leads.booking_demo(var11)
# var2 = res2.gety()
# assert var22 == 'aaaaaa'
