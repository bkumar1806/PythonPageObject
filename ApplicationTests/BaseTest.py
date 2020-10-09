import pytest
from ApplicationTests.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass