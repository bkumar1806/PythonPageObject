"""This is customized fixture defined for Page Object Model framework"""

import pytest
from selenium import webdriver
from Config.App_Configs import TestData


@pytest.fixture(params = ["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER_EXE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_DRIVER_EXE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()