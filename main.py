# coding     : utf-8
# @Time      : 2021/4/22 下午5:46
import pytest

if __name__ == '__main__':
    pytest.main(["-q", "-v", "service/account/test_account.py::Account::crm_login_with_mm"])
