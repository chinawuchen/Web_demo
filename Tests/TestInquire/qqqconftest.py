import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage.login_page import LoginPage
from Case.LoginCase.login_data import cases_success
from Config import config
from Common.base_log import Log

logger = Log()


# 已登录
@pytest.fixture(scope="session")
def login_page(browser):
    login_page = LoginPage(browser)
    user_info = cases_success[0]
    login_page.get().login(user_info["username"], user_info["password"])
    yield browser