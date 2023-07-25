import sys, os
base_path = os.path.abspath("")
sys.path.append(base_path)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage.login_page import LoginPage
from Case.LoginCase.login_data import cases_success
from Config import config
from Common.base_log import Log


logger = Log()

# 打开关闭浏览器
@pytest.fixture(scope="session")
def browser():
    # 设置 Chrome 驱动路径
    logger.info("==========开始 执行51项目测试===========")
    driver_path = '/usr/local/bin/chromedriver_mac_arm64'
    chrome_options = Options()
    # 启动 Chrome 浏览器
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 设置隐式等待
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    # 浏览器页面最大化
    driver.maximize_window()
    # 返回一个浏览器对象
    yield driver
    driver.quit()
    logger.info("==========结束 执行51项目测试===========")

# 已登录
@pytest.fixture(scope="session")
def login_page(browser):
    login_page = LoginPage(browser)
    user_info = cases_success[0]
    login_page.get().login(user_info["username"], user_info["password"])
    yield browser

# 打开关闭浏览器，只用于登录测试
@pytest.fixture(scope="class")
def browser_login():
    # 设置 Chrome 驱动路径
    logger.info("==========开始 执行51项目登录测试===========")
    driver_path = '/usr/local/bin/chromedriver_mac_arm64'
    chrome_options = Options()
    # 启动 Chrome 浏览器
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 设置隐式等待
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    # 浏览器页面最大化
    driver.maximize_window()
    # 返回一个浏览器对象
    yield driver
    driver.quit()
    logger.info("==========结束 执行51项目登录测试===========")