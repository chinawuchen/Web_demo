import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

import pytest
from Case.PersonalCase.personal_data import information_cases_success
from Pages.PersonalPage.personal_page import PersonalPage
from Common.base_log import Log

logger = Log()

@pytest.mark.usefixtures('login_page')
class TestPersonal(object):

    # 正常用例:基本资料修改成功
    @pytest.mark.parametrize("test_info, compare", information_cases_success)
    def test_information_success(sefl, test_info, compare, login_page):
        logger.info(f" 执行 {sys._getframe().f_code.co_name} 测试用例 ")
        logger.info(f" 基本资料正常测试用例：{test_info['CaseName']} ")
        personal_page = PersonalPage(login_page)
        personal_page.get().choose_bloodtype(test_info["bloodtype"]).choose_gender(test_info["gender"]).choose_ymd(
            test_info["birthyear"], test_info["birthmonth"], test_info["birthday"]).choose_birth(test_info["birthprovince"], test_info["birthcity"], test_info["birthdist"], test_info["birthcommunity"]).choose_reside(test_info["resideprovince"], test_info["residecity"], test_info["residedist"], test_info["residecommunity"]).choose_submit()
        key, expected = list(compare.items())[0]  # 实际结果方式，预期结果
        user_info = personal_page.get_information_success(key)
        logger.info(f"预期结果：{expected}")
        logger.info(f"实际结果：{user_info}")
        try:
            assert expected == user_info
            logger.info(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- PASS ")
        except AssertionError as e:
            personal_page.save_screenshot(f"失败用例截图：{(test_info['CaseName'])}")
            logger.error(f"实际结果与预期结果不符: {user_info} != {expected}")
            logger.error(f" 结束执行 {sys._getframe().f_code.co_name} 测试用例， 测试结果 --- Fail ")
            raise e