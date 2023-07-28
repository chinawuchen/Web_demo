"""
condition_loctor
    个人资料页面-联系方式tab页面元素
"""

     
import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By



class ContactLocator(object):

    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用
    qq_locator = (By.ID, 'qq') # qq输入框
    qqvisible_locator = (By.NAME, 'privacy[qq]') # qq是否可见
    qqopvisible_locator = (By.CSS_SELECTOR, 'option[selected="selected"]') # qq是否可见
    msn_locator = (By.ID, 'msn') # msn输入框
    taobao_locator = (By.ID, 'taobao') # 阿里旺旺输入框
    submit_locator = (By.ID, 'profilesubmitbtn') # 保存按钮

    error_qq_locator = (By.ID, 'showerror_qq') # qq敏感词错误信息
    error_msn_locator = (By.ID, 'showerror_msn') # msn敏感词错误信息
    error_taobao_locator = (By.ID, 'showerror_taobao') # taobao敏感词错误信息
    