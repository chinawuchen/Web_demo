import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Pages.LoginPage.login_page import LoginPage
from Pages.PersonalPage.personal_page import PersonalPage
from Case.LoginCase.login_data import cases_success
from Common.base_log import Log

logger = Log()


# 已登录
@pytest.fixture(scope="session")
def login_page(browser):
    login_page = LoginPage(browser)
    user_info = cases_success[0]
    login_page.get().login(user_info["username"], user_info["password"])
    yield browser

# 进入工作情况tab
@pytest.fixture(scope="class")
def enter_conditions_page(login_page):
    psl_page = PersonalPage(login_page)
    psl_page.get().click_conditions_btn()
    yield login_page


