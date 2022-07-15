# coding     : utf-8
# @Time      : 2021/4/22 下午5:46
import psutil
import pytest


# -s：显示程序中的 print/logging 输出
# -v: 丰富信息模式, 输出更详细的用例执行信息
# -k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
# -q: 简单输出模式, 不输出环境信息
# -x: 出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。


def get_xdist_num():
    phy_cpu_num = psutil.cpu_count(logical=False)  # 物理cpu数 每个cpu核数 * cpu个数
    lgc_cpu_num = psutil.cpu_count(logical=True)  # 逻辑cpu数 每个cpu核数 * cpu个数 * 2（如果支持intel的HT超线程技术的话）
    xdist_num = phy_cpu_num / 2
    return xdist_num


if __name__ == '__main__':
    # pytest.main([])
    # pytest.main(["-q", "-s"])
    pytest.main(['-n', get_xdist_num(), '--reruns', '3', '--reruns-delay', '5', '-s', '-v',
                 '--html=Outputs/reports/report.html'])
