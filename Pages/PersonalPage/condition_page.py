import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLocators.condition_locator import ConditionLocator as loc
from Common.base_page import BasePage


"""设置-个人资料页面-工作情况tab操作"""


class ConditionPage(BasePage):

    # 工作情况:输入自我介绍
    def send_visitors(self, isempty, value=None):
        if isempty == 'yes':
            visitors_elem = self.clear_input(loc.visitors_locator)
        if value:
            visitors_elem.send_keys(value)
        return self

    # 工作情况:输入公司名称
    def send_company(self, isempty, value=None):
        if isempty == 'yes':
            company_elem = self.clear_input(loc.company_locator)
        if value:
            company_elem.send_keys(value)
        return self

    # 工作情况:选择性别
    def choose_gender(self, value=None):
        self.choice_select(loc.gender_locator, value) if value else None
        return self

    # 工作情况:选择公司属性,单选项
    def send_companylog(self, value=None):
        click_mapping = {
            "猎头": loc.headhunters_locator,
            "企业": loc.enterprise_locator
        }
        if value and value in click_mapping:
            self.find(click_mapping[value]).click()
        return self

    # 点击保存 / 工作情况tab通用
    def choose_submit(self):
        try:
            self.find(loc.submit_locator).click()
            self.wait_page_load(loc.page_load__locator)
        except Exception:
            pass
        return self

    # 工作情况: 根据 key 获取成功断言
    def get_conditions_success(self, key):
        conditions = {
            "visitors": loc.visitors_locator,
            "gender": loc.success_gender1_locator,
            "company": loc.company_locator,
            "companylog": (loc.headhunters_locator, loc.enterprise_locator)
        }
        if key == "companylog":
            head_button = "猎头" if self.find(conditions[key][0]).is_selected() else None
            enter_button = "企业" if self.find(conditions[key][1]).is_selected() else None
            return head_button or enter_button or ""
        elif key == "company":
            expected = self.get_key_value(conditions[key], "value")
        elif key in ["visitors", "gender"]:
            expected = self.get_text(conditions[key])
        else:
            expected = None
        return expected

    # 工作情况: 根据 key 获取失败断言
    def get_conditions_error(self, key):
        expected = None
        condition_methods = {
            "visitors": loc.error_visitors_locator,
            "company": loc.error_company_locator,
        }
        if key in condition_methods:
            loctaor = condition_methods[key]
            expected = self.get_text(loctaor)
        return expected
