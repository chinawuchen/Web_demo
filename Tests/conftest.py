import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage.login_page import LoginPage
from Pages.PersonalPage.personal_page import PersonalPage
from Case.LoginCase.login_data import cases_success
from Config import config
from Common.base_log import Log


logger = Log()

# 打开关闭浏览器
@pytest.fixture(scope="session")
def browser():
    logger.info("==========开始 执行51项目测试===========")
    # 设置 Chrome 驱动路径
    driver_path = '/usr/local/bin/chromedriver_mac_arm64'
    # 配置 Chrome 浏览器选项
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
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
    

# 只用于登录模块测试--打开关闭浏览器
@pytest.fixture(scope="module")
def browser_login():
    logger.info("==========开始 执行51项目登录模块测试===========")
    # 设置 Chrome 驱动路径
    driver_path = '/usr/local/bin/chromedriver_mac_arm64'
    # 配置 Chrome 浏览器选项
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
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
    logger.info("==========结束 执行51项目登录模块测试===========")