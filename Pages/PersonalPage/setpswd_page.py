import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLocators.setpswd_locator import SetpswdLocator as loc
from Common.base_page import BasePage

"""设置-密码安全页面操作"""


class SetpswdPage(BasePage):

    # 输入旧密码、新密码、确认密码
    def send_password(self, *passwords):
        password_elements = [
            (loc.oldpassword_locator, passwords[0], passwords[1]),
            (loc.newpassword_locator, passwords[2], passwords[3]),
            (loc.newpassword2_locator, passwords[4], passwords[5])
        ]  # (元素, 是否清空输入, 需要输入的值)
        for locator, clear, password in password_elements:
            if clear == "yes":
                elem = self.clear_input(locator)
            if password:
                elem.send_keys(password)
        return self

    # 点击保存
    def choose_submit(self):
        try:
            self.find(loc.submit_locator).click()
            self.wait_page_load(loc.page_load__locator)
        except Exception:
            pass
        return self
    
    # 保存成功失败信息
    def get_export(self):
        expected = self.get_text(loc.successfully_locator)
        return expected
