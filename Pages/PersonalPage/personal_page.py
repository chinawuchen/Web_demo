import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLocators.personal_locator import PersonalLocator as loc
from Common.base_page import BasePage
from Pages.PersonalPage.condition_page import ConditionPage
from Pages.PersonalPage.contact_page import ContactPage
from Config import page_urls



"""设置-个人资料页面-基本资料tab操作"""


class PersonalPage(BasePage):

    # 访问个人资料页面:默认进入基本资料tab
    def get(self):
        self.driver.get(page_urls.personal_url)
        return self
    
    # 点击工作情况按钮进入:工作情况tab
    def click_conditions_btn(self):
        self.find(loc.condition_locator).click()
        return ConditionPage(self.driver)
    
    # 点击联系方式按钮进入:联系方式tab
    def click_contact_btn(self):
        self.find(loc.contact_locator).click()
        return ContactPage(self.driver)

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

    # 基本资料:根据断言方式key，获取对应的实际结果
    def get_information_success(self, key):
        expected = None
        contact_methods = {
            "bloodtype":loc.success_bloodtype_locator,
            "gender":loc.success_gender_locator,
            "birth":loc.success_birth_locator,
            "reside":loc.success_reside_locator
        }
        if key in contact_methods:
            locator = contact_methods[key]
            expected = self.get_text(locator)
        return expected