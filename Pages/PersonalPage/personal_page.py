import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLoctors.personal_loctor import PersonalLoctor as loc
from Common.base_page import BasePage
from Config import page_urls



"""个人资料页面操作"""


class PersonalPage(BasePage):

    # 访问个人资料页面:默认进入基本资料tab
    def get(self):
        self.driver.get(page_urls.personal_url)
        return self

    # 基本资料:选择血型
    def choose_bloodtype(self, value=None):
        self.choice_select(loc.bloodtype_locator, value) if value else None
        return self

    # 基本资料:选择性别 / 工作情况tab通用
    def choose_gender(self, value=None):
        self.choice_select(loc.gender_locator, value) if value else None
        return self

    # 基本资料:选择生日年、月、日
    def choose_ymd(self, year, month, day):
        options = [
            (loc.birthyear_locator, year),
            (loc.birthmonth_locator, month),
            (loc.birthday_locator, day)
        ]
        for locator, value in options:
            if value:
                self.choice_select(locator, value)
        return self

    # 基本资料:选择出生地省、市、县/区、乡
    def choose_birth(self, province=None, city=None, dist=None, community=None):
        if self.wait_element_present(loc.birth_locator):
            self.find(loc.birth_locator).click()
        options = [
            (loc.birthprovince_locator, province),
            (loc.birthcity_locator, city),
            (loc.birthdist_locator, dist),
            (loc.birthcommunity_locator, community)
        ]
        for locator, value in options:
            if value:
                self.choice_select(locator, value)
        return self

    # 基本资料:选择居住地省省、市、县/区、乡
    def choose_reside(self, province, city, dist, community):
        if self.wait_element_present(loc.reside_locator):
            self.find(loc.reside_locator).click()
        options = [
            (loc.resideprovince_locator, province),
            (loc.residecity_locator, city),
            (loc.residedist_locator, dist),
            (loc.residecommunity_locator, community)
        ]
        for locator, value in options:
            if value:
                self.choice_select(locator, value)
        return self

    # 点击保存 / 工作情况tab通用
    def choose_submit(self):
        try:
            self.find(loc.submit_locator).click()
            self.wait_page_load(loc.page_load__locator)
        except Exception:
            pass
        return self
    
    # 获取修改后基本资料信息
    def get_information_success(self):
        information_success = []
        information_success.append(
            self.get_text(loc.success_bloodtype_locator))
        information_success.append(self.get_text(loc.success_gender_locator))
        information_success.append(self.get_text(
            loc.success_birth_locator).replace(" (修改)", ""))
        information_success.append(self.get_text(
            loc.success_reside_locator).replace(" (修改)", ""))
        return information_success

    # 点击工作情况按钮进入:工作情况tab
    def click_conditions_btn(self):
        e = self.find(loc.condition_locator).click()
        return self

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

    # 工作情况:选择公司属性,单选项
    def send_companylog(self, value=None):
        click_mapping = {
            "猎头": loc.headhunters_locator,
            "企业": loc.enterprise_locator
        }
        if value and value in click_mapping:
            self.find(click_mapping[value]).click()
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