"""
login_loctor
    查询页面的元素
"""

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By

class LoginLocator():

    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用
    uname_locator = (By.ID, 'ls_username') # 账号
    pwd_locator = (By.ID, 'ls_password') # 密码
    login_btn_locator = (By.CSS_SELECTOR, 'button.pn.vm') # 登录
    
    success_msg_locator = (By.CSS_SELECTOR, 'a[title="查看个人资料"]')
    error_msg_locator = None