import sys
import os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Common.base_log import Log
from Pages.PersonalPage.contact_page import ContactPage
from Case.PersonalCase.contact_data import contact_cases_success, contact_cases_error

logger = Log()

@pytest.mark.usefixtures('enter_contact_page')
class TestContact(object):

    # 正常用例:联系方式修改成功
    @pytest.mark.parametrize("test_info, compare", contact_cases_success)
    def test_contact_success(self, test_info, compare, enter_contact_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 联系方式正常测试用例：{test_info['CaseName']} ")
        contact_page = ContactPage(enter_contact_page)
        contact_page.send_qq(test_info["qqempty"], test_info["qq"]).send_qqvisible(test_info["qqvisible"]).send_msn(
            test_info["msnempty"], test_info["msn"]).send_taobao(test_info["tbempty"], test_info["taobao"]).choose_submit()
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        user_info = contact_page.get_contact_success(key)
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            contact_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {expected}")
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e

    # 异常用例:联系方式修改失败
    @pytest.mark.parametrize("test_info, compare", contact_cases_error)
    def test_contact_error(self, test_info, compare, enter_contact_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 联系方式异常测试用例：{test_info['CaseName']} ")
        contact_page = ContactPage(enter_contact_page)
        contact_page.send_qq(test_info["qqempty"], test_info["qq"]).send_qqvisible(test_info["qqvisible"]).send_msn(
            test_info["msnempty"], test_info["msn"]).send_taobao(test_info["tbempty"], test_info["taobao"]).choose_submit()
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        user_info = contact_page.get_contact_error(key)
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info
            logger.info(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            contact_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {expected}")
            logger.error(
                f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e