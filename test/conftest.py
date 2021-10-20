import pytest

from helper import Helper

# Prevent pytest from trying to collect webtest's TestApp as tests:
Helper.__test__=False

    
@pytest.fixture()
def testhelper_object():
    obj = Helper()
    return obj