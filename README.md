# 一. AscTrio 是什么?

AscTrio 是一个基于 Pytest 的接口自动化测试工具，其中 A、S、C 分别代表该项目接口用例组成部分的 Api层、Service层 和 Case层。

特点如下：
1. 容易上手，尽可能简化编写接口测试代码的步骤，就算没有代码基础，也可以模仿 sample 文件进行接口用例编写。
2. 丰俭由人，既可直接调接口，也可以结合数据驱动和用例流程执行完整的自动化测试验证和报告统计显示。
3. 朴实无华，为了能处理某些特殊场景，没有写太多骚操作，以追求可扩展性和普适性。

# 二. 为什么用 AscTrio?

- 关于接口自动化有很多现成、成熟的框架和工具，例如饿了么团队带有可视化页面的 Yapi，以及同样基于 Pytest、注重数据驱动的 HttpRunner 等等。
- AscTrio 希望使用者能更专注在代码层面，进行更丰富灵活的操作。只要代码封装合理，上手门槛就不再是问题。
- 当我们在编写代码来做接口测试过程中尝到甜头，或许我们就不再想用回测试用例平台对着那些控件点点点来录入测试用例了。

# 三. 怎么使用 AscTrio?

## 组成架构

![](https://github.com/lzpsgh/AscTrio/raw/master/IMG/asctrio-%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

    Base层 ===============> 基础层，对通用代码进行封装抽象
    Api层  ===============> 接口层，对接开发写的接口
    Serv层 ===============> 服务层，一组常用api的组合
    Case层 ===============> 用例层，在用例里面写断言验证
    Data层 ===============> 数据层，用于传输请求体，用于数据驱动
    log/  ===============> 记录接口请求日志
    util/ ===============> 各种工具类
    .env  ===============> 环境变量，包括域名和相关账号密码
    pytest.ini ==========> pytest 配置文件

## 使用步骤

1. 【环境】确保安装的 Python 版本是3.7以上。 理论上 Python 3.6 也能运行
2. 【依赖】命令行进入项目目录，使用`pip install -r requirements.txt`安装好相关依赖。
3. 【配置】将 env 文件重命名为 .env ，并修改相应域名和 ip 端口
4. 【Api层】如果想要简单发起1个 api 请求，甚至懒得做响应校验，可直接在 api 层的对应模块中编写新的方法（自己新建模块也可以）。 这个新建的方法就对应发编写某个具体 api。 写完后可直接调用2处的绿色按钮直接运行即可。
   ![](https://github.com/lzpsgh/AscTrio/raw/master/IMG/asctrio-api%E5%B1%82.jpg)

5. 【Case层】如果 api 调试无误，需要做详细点的接口用例设计，也只需要再在 case 层的对应模块中编写1个新的方法（自己新建模块也可以）。这个新建的方法对应试编写的某条测试用例 case，在方法里调用刚才的 api 并写上相关
   assert 断言即可。
   ![](https://github.com/lzpsgh/AscTrio/raw/master/IMG/asctrio-case%E5%B1%82.jpg)

6. 【Data层】如果某个 api 接口要传的参数字段比较多，或者想要多次重复执行接口生成大量数据，这时就需要用到参数化和数据驱动了。在 data
   层的对应模块中增一对象（自己新建个文件也可以）。这个对象就是对应1条测试用例中用到的1组或n组测试数据。然后通过 pytest 的 parametrize 标记将该对象传进方法中以供调用，对中有n组数据，就会自动执行多少次该用例。
   当获取到 data层的数据时，无论 api层或者 case层，都不需要将 每个字段都在函数签名中再声明一次，直接用 **kwargs 代替即可。

7.【Serv层】如果在 case 层需要先后调用多个 api，可以自行将一组较常用的 api 组合封装成 service，这里不需要用类来包装，直接写成函数就可以了。
![](https://github.com/lzpsgh/AscTrio/raw/master/IMG/asctrio-serv%E5%B1%82.jpg)

## 注意事项

1. 现有的大部分代码都是调通过的。但由于中途进行过大大小小几次方案的重构，难保有些接口还在沿用之前已废弃的写法。这里建议以 sample 的相关文件为准，比如 Api 层的 sample.py , Serv 层的
   sample_serv.py, Case 层的 test_sample.py

## TODO

1. [ ] 【断言】用 deepdiff 进行 json 差异对比
2. [ ] 【断言】用 jmespath 来断言 response 中各种 复杂的 key 和 value 判断，类似 xpath（ jsonschema 只适合验证里面的key）
3. [ ] 【执行】用 pytest-rerunfailures 重新运行失败的用例
4. [ ] 【执行】用 pytest-xdist 实行进程级并发测试
5. [ ] 【执行】用 httpx 做异步请求，代替 requests，异步日志准确性
6. [ ] 【日志】使用 allure2 进行用例统计和生成
7. [ ] 【同步】本地代码库不再维护 api 接口层信息，统一从 yapi 的 mongodb 接口库中获取接口信息
8. [ ] 【架构】抽象出 common_api，从 mondodb 接口库中获取到接口信息后直接注入到 common_api，并由 case层直接发起请求。无需编写 api层 代码。

## 参考资料

本项目参考了 Github 上的项目 [pytestDemo](https://github.com/wintests/pytestDemo) 。

主要改动点如下：

1. 将原项目中的 api 层和 operation层 合并为现在的 api 层。
2. 将项目中的 api 层、case 层的各个字段统一用 **kwargs 关键字参数代替
3. 新增加 service 层。
4. 新增加各层对应的 sample 文件。
