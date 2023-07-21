import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 设置 Chrome 驱动路径
driver_path = '/usr/local/bin/chromedriver_mac_arm64'
chrome_options = Options()
# 启动 Chrome 浏览器
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 登录
driver.get("http://bbs.51testing.com/forum.php")
aa = driver.find_element(By.XPATH, '//input[@name="username"]')
aa.send_keys("wuchen111")
bb = driver.find_element(By.XPATH, '//input[@name="password"]')
bb.send_keys("wu123456")
driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()


time.sleep(3)
# # 个人资料
driver.get("http://bbs.51testing.com/home.php?mod=spacecp&ac=profile")

time.sleep(1)
driver.find_element(By.XPATH, '//ul[@class="tb cl"]/li[3]').click()

time.sleep(1)

<input type="radio" name="field3" class="pr" value="猎头" tabindex="1" checked="checked">

get_key = driver.find_element(By.XPATH, '//input[@value="猎头"]')
checked_value = get_key.get_attribute("checked")
print(checked_value)


# time.sleep(3)

# try:
#     gettext = driver.find_element(By.XPATH, '//td[@id="td_birthcity"]')
#     print(gettext.text.strip())
# except Exception as e:
#     print(e)





