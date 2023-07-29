import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Case.PersonalCase.setpswd_data import setpswd_cases_success, setpswd_cases_error
from Pages.PersonalPage.setpswd_page import SetpswdPage
from Common.base_log import Log

logger = Log()

@pytest.mark.usefixtures('enter_setpassword_page')
class TestSetpswd(object):

    # 正常用例:修改密码成功
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("test_info, compare", setpswd_cases_success)
    def test_setpswd_success(self, test_info, compare, enter_setpassword_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 修改密码正常测试用例：{test_info['CaseName']} ")
        driver = enter_setpassword_page
        setpswd_page = SetpswdPage(driver)
        successfully = setpswd_page.send_password(test_info['clear_old'], test_info['oldpassword'], test_info['clear_new'],
                                                  test_info['newpassword'], test_info['clear_new2'], test_info['newpassword2']).choose_submit().choose_submit().get_export()
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{successfully}")
        try:
            assert expected == successfully, "密码修改成功"
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            setpswd_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e

    # 异常用例:修改密码失败
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("test_info, compare", setpswd_cases_error)
    def test_setpswd_error(self, test_info, compare, enter_setpassword_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 修改密码异常测试用例：{test_info['CaseName']} ")
        driver = enter_setpassword_page
        setpswd_page = SetpswdPage(driver)
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        user_info = setpswd_page.send_password(test_info['clear_old'], test_info['oldpassword'], test_info['clear_new'],
                                                  test_info['newpassword'], test_info['clear_new2'], test_info['newpassword2']).choose_submit().choose_submit().get_export()
        driver.back()
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected in user_info, "密码修改失败"
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            setpswd_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e