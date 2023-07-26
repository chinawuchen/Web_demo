import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLoctors.condition_loctor import ConditionLoctor as loc
from Common.base_page import BasePage



"""个人资料页面-工作情况tab操作"""


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

    # 工作情况:获取自我介绍信息
    def get_conditions_visitors(self):
        visitors_text = self.get_text(loc.visitors_locator)
        return visitors_text
    
    # 工作情况:获取性别信息
    def get_conditions_gender(self):
        gender_text = self.get_text(loc.success_gender1_locator)
        return gender_text
    
    # 工作情况:获取公司名称信息
    def get_conditions_company(self):
        company_text = self.get_key_value(loc.company_locator, "value")
        return company_text
    
    # 工作情况:获取公司属性信息
    def get_conditions_button(self):
        head_button = self.find(loc.headhunters_locator)
        if head_button.is_selected():
            head_button = "猎头"
        enter_button = self.find(loc.enterprise_locator)
        if enter_button.is_selected():
            enter_button = "企业"
        return head_button, enter_button
    
    # 工作情况: 根据 key 获取成功断言
    def get_conditions_success(self, key):
        if key == "visitors":
            expected = self.get_conditions_visitors()
        elif key == "gender":
            expected = self.get_conditions_gender()
        elif key == "company":
            expected = self.get_conditions_company()
        else:
            expected = self.get_conditions_button()
        return expected

    # 工作情况:公司名称错误检查
    def get_company_error(self):
        company_error = self.get_text(loc.error_company_locator)
        return company_error

    # 工作情况:自我介绍错误检查
    def get_visitors_error(self):
        visitors_error = self.get_text(loc.error_visitors_locator)
        return visitors_error
    
    # 工作情况: 根据 key 获取失败断言
    def get_conditions_error(self, key):
        if key == "visitors":
            expected = self.get_visitors_error()
        elif key == "company":
            expected = self.get_company_error()
        return expected