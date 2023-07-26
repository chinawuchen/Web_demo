import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Pages.LoginPage.login_page import LoginPage
from Case.LoginCase.login_data import cases_success, cases_error
from Common.base_log import Log

logger = Log()

@pytest.mark.usefixtures('browser_login')
class TestLogin(object):

    # 登录成功
    @pytest.mark.parametrize("test_info", cases_success)
    def test_login_success(self, test_info, browser_login):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        login_page = LoginPage(browser_login)
        logger.info(f" 登录正常测试用例：{test_info['CaseName']} ")
        login_page.get().login(test_info["username"], test_info["password"])
        user_info = login_page.get_user_success()
        logger.info(f"预期结果：{test_info['expected']}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert test_info["expected"] in user_info, "登录成功"
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            login_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e