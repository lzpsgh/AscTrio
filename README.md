# AscTrio

ASCTrio 是基于 Pytest 的接口自动化测试框架。

- 【1期已实现功能】
  1. 快速编写测试用例，在一个模块中就能发起接口请求
  2. 提供接口用例模版，修改部分关键字即可自己创建接口测试用例
  3. 支持参数化和数据驱动，也支持x中途嵌入faker的动态数据
  4. 提供常用的util类
  5. 请求体使用**kwargs关键字参数进行封装，避免对大量请求体字段的重复复制粘贴
  
- 【2期待实现功能】
  1. 【数据】用 mongodb 解决yml中键key冗余的问题
  2. 【数据】用 data_lake 数据中心代替 data_pool，不再死板读取yml里的字面量，而是结合 sql_util 和 faker_util 自动获取对应数据（yml从数据源变成数据模版）
  3. 【断言】用 deepdiff 进行json差异对比
  4. 【断言】用 fuzzywuzzy 进行字符串模糊匹配
  5. 【断言】用 jmespath 来断言 response 中各种 复杂的 key和value 判断，类似xpath（jsonschema只适合验证里面的key）
  6. 【执行】用 yml/redis 保存 批量注册/登录场景下各个用户token
  7. 【执行】用 pytest-rerunfailures 重新运行失败的用例
  8. 【执行】用 pytest-xdist 实行进程级并发测试
  9. 【执行】用 httpx 做异步请求，代替requests，异步日志准确性
  10. 【日志】使用 allure2 进行用例统计和生成
  
PS：由于项目一直在迭代，自行编写代码时尽可能参考最近创建/修改的文件模块.
例如 api/blue_bridge_context_signup.py、case/blue_bridge_contest/test_blue_bridge_contest.py 和data/bbc_signup_data.yml
 

项目参考了 Github 上的项目 [pytestDemo](https://github.com/wintests/pytestDemo)，并对其做了较大改动和优化。
