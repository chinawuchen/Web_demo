import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Case.PersonalCase.personal_data import information_cases_success, conditions_cases_success, conditions_cases_error
from Pages.PersonalPage.personal_page import PersonalPage
from Common.base_log import Log

logger = Log()


class TestPersonal(object):

    # 正常用例:基本资料修改成功
    @pytest.mark.information
    @pytest.mark.parametrize("test_info", information_cases_success)
    def test_information_success(sefl, test_info, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        driver = login_page
        personal_page = PersonalPage(driver)
        logger.info(f" 基本资料正常测试用例：{test_info['CaseName']} ")
        personal_page.get().choose_bloodtype(test_info["bloodtype"]).choose_gender(test_info["gender"]).choose_ymd(
            test_info["birthyear"], test_info["birthmonth"], test_info["birthday"]).choose_birth(test_info["birthprovince"], test_info["birthcity"], test_info["birthdist"], test_info["birthcommunity"]).choose_reside(test_info["resideprovince"], test_info["residecity"], test_info["residedist"], test_info["residecommunity"]).choose_submit()
        user_info = personal_page.get_information_success()
        logger.info(f"预期结果：{test_info['expected']}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert set(test_info["expected"]) == set(user_info), "基本资料修改成功"
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            personal_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            raise e

    # 正常用例:工作情况修改成功
    @pytest.mark.condition
    @pytest.mark.parametrize("test_info, compare", conditions_cases_success)
    def test_condition_success(sefl, test_info, compare, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        driver = login_page
        condition_page = PersonalPage(driver)
        logger.info(f" 工作情况正常测试用例：{test_info['CaseName']} ")
        condition_page.get().click_conditions_btn().send_visitors(test_info["visempty"], test_info["visitors"]).choose_gender(
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
    def test_condition_error(self, test_info, compare, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        driver = login_page
        condition_page = PersonalPage(driver)
        logger.info(f" 工作情况异常测试用例：{test_info['CaseName']} ")
        condition_page.get().click_conditions_btn().send_visitors(test_info["visempty"], test_info["visitors"]).choose_gender(
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