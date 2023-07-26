import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Case.PersonalCase.condition_data import conditions_cases_success, conditions_cases_error
from Pages.PersonalPage.condition_page import ConditionPage
from Common.base_log import Log

logger = Log()

@pytest.mark.usefixtures('enter_conditions_page')
class TestCondition(object):

    # 正常用例:工作情况修改成功
    @pytest.mark.parametrize("test_info, compare", conditions_cases_success)
    def test_condition_success(sefl, test_info, compare, enter_conditions_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        driver = enter_conditions_page
        condition_page = ConditionPage(driver)
        logger.info(f" 工作情况正常测试用例：{test_info['CaseName']} ")
        condition_page.send_visitors(test_info["visempty"], test_info["visitors"]).choose_gender(
            test_info["gender"]).send_company(test_info["cisempty"], test_info["company"]).send_companylog(test_info["companylog"]).choose_submit()
        key, expected = list(compare.items())[0] # 实际结果方式，预期结果
        user_info = condition_page.get_conditions_success(key) # 实际结果
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info, "工作情况修改成功"
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            condition_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e

    # 异常用例:工作情况修改失败
    @pytest.mark.parametrize("test_info, compare", conditions_cases_error)
    def test_condition_error(self, test_info, compare, enter_conditions_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        driver = enter_conditions_page
        condition_page = ConditionPage(driver)
        logger.info(f" 工作情况异常测试用例：{test_info['CaseName']} ")
        condition_page.send_visitors(test_info["visempty"], test_info["visitors"]).choose_gender(
            test_info["gender"]).send_company(test_info["cisempty"], test_info["company"]).send_companylog(test_info["companylog"]).choose_submit()
        key, expected = list(compare.items())[0] # 实际结果方式，预期结果
        user_info = condition_page.get_conditions_error(key)
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info, "工作情况修改失败"
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            condition_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e