import pytest

from case.conftest import bbc_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return bbc_data.get(testcase_name)
