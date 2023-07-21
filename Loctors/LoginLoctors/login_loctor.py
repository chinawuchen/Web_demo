import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By

class LoginLocator():
    
    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用
    uname_locator = (By.XPATH, '//input[@name="username"]')
    pwd_locator = (By.XPATH, '//input[@name="password"]')
    login_btn_locator = (By.XPATH, '(//button[@type="submit"])[1]')
    success_msg_locator = (By.XPATH, '//a[@title="查看个人资料"]')
    error_msg_locator = None