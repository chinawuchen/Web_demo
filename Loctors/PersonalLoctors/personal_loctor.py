"""
personal_loctor
    个人资料页面-基本资料tab页面元素
"""

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By


class PersonalLoctor(object):
    """修改基本资料元素"""
    page_load__locator = (By.TAG_NAME, 'html') # 等待页面刷新的元素，通用
    information_locator = (By.XPATH, '//ul[@class="tb cl"]/li[1]') # 基本资料tab
    contact_locator = (By.XPATH, '//ul[@class="tb cl"]/li[2]') # 联系方式tab
    condition_locator = (By.XPATH, '//ul[@class="tb cl"]/li[3]') # 工作情况tab

    bloodtype_locator = (By.XPATH, '//select[@id="bloodtype"]') # 血型
    gender_locator = (By.XPATH, '//select[@id="gender"]') # 性别，通用

    birthyear_locator = (By.XPATH, '//select[@id="birthyear"]') # 生日年
    birthmonth_locator = (By.XPATH, '//select[@id="birthmonth"]') # 生日月
    birthday_locator = (By.XPATH, '//select[@id="birthday"]') # 生日日
    
    birth_locator = (By.XPATH, '//td[@id="td_birthcity"]/a') # 修改出生地
    birthprovince_locator = (By.XPATH, '//select[@id="birthprovince"]') # 出生地省
    birthcity_locator = (By.XPATH, '//select[@id="birthcity"]') # 出生地市
    birthdist_locator = (By.XPATH, '//select[@id="birthdist"]') # 出生地县/区
    birthcommunity_locator = (By.XPATH, '//select[@id="birthcommunity"]') # 出生地乡
    
    reside_locator = (By.XPATH, '//td[@id="td_residecity"]/a') # 修改居住地
    resideprovince_locator = (By.XPATH, '//select[@id="resideprovince"]') # 居住地省	
    residecity_locator = (By.XPATH, '//select[@id="residecity"]') # 居住地市
    residedist_locator = (By.XPATH, '//select[@id="residedist"]') # 居住地县/区
    residecommunity_locator = (By.XPATH, '//select[@id="residecommunity"]') # 居住地乡

    submit_locator = (By.ID, 'profilesubmitbtn') # 保存按钮，通用
    # 基本资料断言元素
    success_bloodtype_locator = (By.XPATH, '(//option[@selected="selected"])[1]') # 血型
    success_gender_locator = (By.XPATH, '(//option[@selected="selected"])[3]') # 性别
    success_birth_locator = (By.XPATH, '//td[@id="td_birthcity"]') # 出生地
    success_reside_locator = (By.XPATH, '//td[@id="td_residecity"]') # 居住地