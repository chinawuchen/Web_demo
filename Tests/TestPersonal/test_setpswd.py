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
    @pytest.mark.skip(reason="无条件跳过")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("test_info, compare", setpswd_cases_success)
    def test_setpswd_success(self, test_info, compare, enter_setpassword_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 修改密码正常测试用例：{test_info['CaseName']} ")
        setpswd_page = SetpswdPage(enter_setpassword_page)
        successfully = setpswd_page.send_password(test_info['clear_old'], test_info['oldpassword'], test_info['clear_new'],
                                                  test_info['newpassword'], test_info['clear_new2'], test_info['newpassword2']).choose_submit().choose_submit().get_export()
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{successfully}")
        try:
            assert expected == successfully
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            setpswd_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {successfully} != {expected}")
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e

    # 异常用例:修改密码失败
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("test_info, compare", setpswd_cases_error)
    def test_setpswd_error(self, test_info, compare, enter_setpassword_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 修改密码异常测试用例：{test_info['CaseName']} ")
        setpswd_page = SetpswdPage(enter_setpassword_page)
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        user_info = setpswd_page.send_password(test_info['clear_old'], test_info['oldpassword'], test_info['clear_new'],
                                                  test_info['newpassword'], test_info['clear_new2'], test_info['newpassword2']).choose_submit().choose_submit().get_export()
        enter_setpassword_page.back()
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            setpswd_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {expected}")
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e