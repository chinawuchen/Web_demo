import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
import time
from Pages.PersonalPage.personal_page import PersonalPage
from Common.base_log import Log

logger = Log()

# 进入联系方式tab
@pytest.fixture(scope="class")
def enter_contact_page(login_page):
    psl_page = PersonalPage(login_page)
    psl_page.get().click_contact_btn()
    yield login_page

# 进入工作情况tab
@pytest.fixture(scope="class")
def enter_conditions_page(login_page):
    psl_page = PersonalPage(login_page)
    psl_page.get().click_conditions_btn()
    yield login_page