"""
condition_loctor
    设置-密码安全页面元素
"""

     
import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By


class SetpswdLocator(object):
    
    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用
    oldpassword_locator = (By.ID, 'oldpassword') # 旧密码
    newpassword_locator = (By.ID, 'newpassword') # 新密码
    newpassword2_locator = (By.ID, 'newpassword2') # 确认密码
    submit_locator = (By.CSS_SELECTOR, 'button[name="pwdsubmit"]') # 保存按钮
    
    successfully_locator = (By.ID, 'messagetext') # 个人资料保存成功
    # back_locator = (By.LINK_TEXT, '[ 点击这里返回上一页 ]') # 点击这里返回上一页

