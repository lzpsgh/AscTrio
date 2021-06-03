# coding     : utf-8
# @Time      : 2021/4/22 下午5:46
import pytest

# 只能执行case层的用例，api层因为没有强制test开头命名，无法被识别为可执行用例

if __name__ == '__main__':
    pytest.main(["-q", "-s", "account/test_account.py"])