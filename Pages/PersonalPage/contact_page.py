import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLoctors.contact_loctor import ContactLoctor as loc
from Common.base_page import BasePage


"""个人资料页面-联系方式tab操作"""

class ContactPage(BasePage):
    
    
    # 联系方式:输入qq
    def send_qq(self, isempty, value=None):
        if isempty == 'yes':
            qq_elem = self.clear_input(loc.qq_locator)
        if value:
            qq_elem.send_keys(value)
        return self

    # 联系方式:qq是否公开，下拉框
    def send_qqvisible(self, value=None):
        self.choice_select(loc.qqvisible_locator, value) if value else None
        return self

    # 联系方式:输入msn
    def send_msn(self, isempty, value=None):
        if isempty == 'yes':
            msn_elem = self.clear_input(loc.msn_locator)
        if value:
            msn_elem.send_keys(value)
        return self

    # 联系方式:输入taobao
    def send_taobao(self, isempty, value=None):
        if isempty == 'yes':
            taobao_elem = self.clear_input(loc.taobao_locator)
        if value:
            taobao_elem.send_keys(value)
        return self

    # 点击保存
    def choose_submit(self):
        try:
            self.find(loc.submit_locator).click()
            self.wait_page_load(loc.page_load__locator)
        except Exception:
            pass
        return self
    
    # 联系方式:根据断言方式key，获取对应的实际结果
    def get_contact_success(self, key):
        expected = None
        contact_methods = {
            "qq":loc.qq_locator,
            "qqvisible":loc.qqopvisible_locator,
            "msn":loc.msn_locator,
            "taobao":loc.taobao_locator
        }
        if key in contact_methods:
            locator = contact_methods[key]
            if key == 'qqvisible':
                expected = self.get_text(locator)
            else:
                expected = self.get_key_value(locator, "value")
        return expected

    # 联系方式:根据断言方式key，获取对应实际结果(敏感词错误信息)
    def get_contact_error(self, key):
        expected = None
        contact_methods = {
            "qq":loc.error_qq_locator,
            "msn":loc.error_msn_locator,
            "taobao":loc.error_taobao_locator
        }
        if key in contact_methods:
            locator = contact_methods[key]
            expected = self.get_text(locator)
        return expected
