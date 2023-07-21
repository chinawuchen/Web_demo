"""
base_page
    页面对象有一些共同的基本操作，可以封装起来，并可以在基本操作当中，加上日志和截图的处理
"""

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from datetime import datetime
import pyautogui
from Config import config
from Common.base_log import Log

logger = Log()

class BasePage(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    # 查找元素
    def find(self, locator):
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            logger.error(f"元素 {locator} 定位失败！！！：{err}")
            self.save_screenshot()
        else:
            return e
    
    # 清空输入框
    def clear_input(self, locator):
        input_box = self.find(locator)
        try:
            input_box.clear()
        except Exception as err:
            logger.error(f"清空输入框 {locator} 失败！！！：{err}")
        finally:
            return input_box

    # 截图
    def save_screenshot(self, doc=None):
        ts_str = datetime.now().strftime("%y-%m_%d-%H-%M-%S")
        file_path = f"{config.IMAGE_PATH}/{doc}_{ts_str}.png"
        try:
            self.driver.save_screenshot(file_path)
            logger.info(f' 截图成功:{doc}，图片路径为: {file_path}')
        except:
            logger.error(f' 截图失败！！！: {doc}')

    def wait_element_clickable(self, locator, timeout=10, poll_frequency=0.5):
        """等待元素可以被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(EC.element_to_be_clickable(locator))
        except Exception as err:
            logger.error(f"元素 {locator} 定位失败！！！：{err}")
            self.save_screenshot()
        else:
            return e

    def wait_element_visible(self, locator, timeout=10, poll_frequency=0.5):
        """等待元素可见-1"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(EC.visibility_of_element_located(locator))
        except Exception as err:
            logger.error(f"元素 {locator} 定位失败！！！：{err}")
            self.save_screenshot()
        else:
            return e

    def wait_element_present(self, locator, timeout=10, poll_frequency=0.5):
        """等待元素被加载"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(EC.presence_of_element_located(locator))
        except Exception as err:
            logger.error(f"元素 {locator} 定位失败！！！：{err}")
            self.save_screenshot()
        else:
            return e

    # 等待点击某个元素
    def click_element(self, locator, max_attempts=5):
        for _ in range(max_attempts):
            try:
                e = self.wait_element_clickable(locator)
                e.click()
            except Exception as err:
                logger.error(f"元素 {locator} 未出现，正在重试！！！：{err}")
                self.save_screenshot()
        return self
    
    # 双击某个元素
    def double_click(self, locator):
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.driver)
        ac.double_click(e).perform()
        return self
     
    # 选中下拉框关键字
    def choice_select(self, locator, value, max_attempts=5):
        for _ in range(max_attempts):
            try:
                sel = Select(self.wait_element_clickable(locator))
                sel.select_by_value(value)
                break
            except Exception as err:
                logger.error(f" 下拉框元素 {locator} 未出现，正在重试！！！：{err}")
        return None

    # 获取页面文本信息
    def get_text(self, locator, max_attempts=5):
        for _ in range(max_attempts):
            try:
                e = self.wait_element_present(locator)
                return e.text.strip()
            except Exception as err:
                logger.error(f" 文本 {locator} 获取失败，正在重试！！！：{err}")
        return None
    
    # 根据关键字获取信息
    def get_key_value(self, locator, key):
        try:
            e = self.find(locator)
            value = e.get_property(key)
        except Exception as err:
            logger.error(f" 根据关键字 {locator} 获取信息失败：{err}")
        return value

    # 等待页面刷新完成
    def wait_page_load(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.staleness_of(self.find(locator)))
        wait.until(EC.presence_of_element_located(locator))

if __name__ == "__main__":
    doc = "个人资料_工作情况_自我介绍含有敏感词汇"
    ts_str = datetime.now().strftime("%y-%m_%d-%H-%M-%S")
    file_path = config.IMAGE_PATH + '/' + doc + ts_str + '.png'
    print(file_path)