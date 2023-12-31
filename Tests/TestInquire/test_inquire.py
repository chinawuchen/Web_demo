import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Pages.InquirePage.inquire_page import InquirePage
from Case.InquireCase.inquire_data import cases_success, cases_error
from Common.base_log import Log
import time

logger = Log()

@pytest.mark.usefixtures('login_page')
class TestInquire(object):
    
    # 正常用例:查询成功
    @pytest.mark.smoke # 冒烟测试
    @pytest.mark.parametrize("test_info", cases_success)
    def test_inquire_success(self, test_info, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 查询正常测试用例：{test_info['CaseName']} ")
        inquire_page = InquirePage(login_page)
        user_info = inquire_page.get().inquire(test_info['iqname']).get_inquire_success()
        logger.info(f"等待 10 秒，避免频繁搜索")
        time.sleep(10)
        logger.info(f"预期结果：{test_info['expected']}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert test_info["expected"] == user_info
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            inquire_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {test_info['expected']}")
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e
    
    # 异常用例:查询失败
    # @pytest.mark.skip(reason="无条件跳过")
    @pytest.mark.parametrize("test_info", cases_error)
    def test_inquire_error(self, test_info, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 查询异常测试用例：{test_info['CaseName']} ")
        inquire_page = InquirePage(login_page)
        user_info = inquire_page.get().inquire(test_info['iqname']).get_inquire_error()
        logger.info(f"等待 10 秒，避免频繁搜索")
        time.sleep(10)
        logger.info(f"预期结果：{test_info['expected']}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert test_info["expected"] == user_info
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            inquire_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {test_info['expected']}")
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e