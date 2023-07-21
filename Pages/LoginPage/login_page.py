import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Config import page_urls
from Common.base_page import BasePage
from Loctors.LoginLoctors.login_loctor import LoginLocator as loc


class LoginPage(BasePage):
    
    # 访问登录页面
    def get(self):
        self.driver.get(page_urls.login_url)
        return self
    
    # 登录操作
    def login(self, uname, pwd):
        uname_elem = self.find(loc.uname_locator)
        uname_elem.send_keys(uname)
        pwd_elem = self.find(loc.pwd_locator)
        pwd_elem.send_keys(pwd)
        self.click_element(loc.login_btn_locator)
        self.wait_page_load(loc.page_load__locator)
        return self
    
    # 获取登录成功信息
    def get_user_success(self):
        e = self.wait_element_visible(loc.success_msg_locator)
        return e.text.strip()
    
    # 获取登录失败信息
    def get_user_error(self):
        pass