"""
condition_loctor
    个人资料页面-工作情况tab页面元素
"""

     
import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By



class ConditionLoctor(object):

    """修改工作情况元素"""
    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用

    visitors_locator = (By.XPATH, '//textarea[@id="bio"]') # 自我介绍输入框
    company_locator = (By.XPATH, '//input[@id="company"]') # 公司输入框
    gender_locator = (By.XPATH, '//select[@id="gender"]') # 性别，通用
    headhunters_locator = (By.XPATH, '//input[@value="猎头"]') # 公司属性,猎头
    enterprise_locator = (By.XPATH, '//input[@value="企业"]') # 公司属性,企业
    submit_locator = (By.XPATH, '//button[@id="profilesubmitbtn"]') # 保存按钮，通用
    save_condition_locator = (By.XPATH, '//div[@class="alert_right"]/p') # 资料更新成功

    # 工作情况断言元素
    success_gender1_locator = (By.XPATH, '(//option[@selected="selected"])[2]') # 性别

    error_company_locator = (By.XPATH, '//div[@id="showerror_company"]') # 公司为空的错误检查：请检查该资料项
    error_visitors_locator = (By.XPATH, '//div[@id="showerror_bio"]')# 自我介绍错误检查：请检查该资料项 (含有敏感词汇)