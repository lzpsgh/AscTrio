# AscTrio

AscTrio 是基于 Pytest 的接口自动化测试框架。A、S、C 分别代表该项目接口用例组成部分的 Api、Service 和 Case。

![项目一览]()

## 项目结构

- /api ================ >> 接口层，对接开发写的接口
- /base =============== >> 基础层，对通用代码进行封装抽象
- /case =============== >> 用例层，对接测试写的测试用例
- /data =============== >> 数据层，yml 格式测试数据，用于数据驱动
- /log ================ >> 用于记录各种日志
- /serv =============== >> 服务层，一组常用 api 的组合，提高复用
- /util =============== >> 各种工具类
- .env ================ >> 环境变量，包括域名和相关账号密码
- pytest.ini ========== >> pytest 配置文件
- requirements.txt ==== >> 第三方依赖库


## 二期优化

- [ ] 1. 【数据】用 mongodb 解决 yml 中键 key 冗余的问题
- [ ] 2. 【数据】用 data_lake 数据中心代替 data_pool，不再死板读取 yml 里的字面量，而是结合 sql_util 和 faker_util 自动获取对应数据（ yml 从数据源变成数据模版）
- [ ] 3. 【断言】用 deepdiff 进行json差异对比
- [ ] 4. 【断言】用 jmespath 来断言 response 中各种 复杂的 key 和 value 判断，类似 xpath（ jsonschema 只适合验证里面的key）
- [ ] 5. 【执行】用 yml/redis 保存 批量注册/登录场景下各个用户token
- [ ] 6. 【执行】用 pytest-rerunfailures 重新运行失败的用例
- [ ] 7. 【执行】用 pytest-xdist 实行进程级并发测试
- [ ] 8. 【执行】用 httpx 做异步请求，代替 requests，异步日志准确性
- [ ] 9. 【日志】使用 allure2 进行用例统计和生成


## 注意

由于项目一直在迭代，自行编写代码时请尽可能参考最近创建/修改的文件模块.
例如 api 层的 blue_bridge_context_signup.py、case 层的 test_blue_bridge_contest.py 和 data 层的 bbc_signup_data.yml

## 原项目参考

本项目参考了 Github 上的项目 [pytestDemo](https://github.com/wintests/pytestDemo)，并对其做了较大改动和优化。
