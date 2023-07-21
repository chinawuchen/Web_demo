import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Common.base_page import BasePage
from Config import page_urls
from Loctors.InquireLoctors.inquire_loctor import InquireLocator as loc


"""查询页面操作"""
class InquirePage(BasePage):

    # 访问查询页面
    def get(self):
        self.driver.get(page_urls.inquire_url)
        return self
    
    # 输入关键字查询
    def inquire(self, inquire_name):
        nquire_elem = self.find(loc.inquire_locator)
        nquire_elem.send_keys(inquire_name)
        self.find(loc.submit_locator).click()
        return self
    
    # 获取查询成功信息
    def get_inquire_success(self):
        e = self.wait_element_visible(loc.success_inquire_locator)
        return e.text.strip()
    
    # 获取没有找到匹配结果
    def get_inquire_error(self):
        e = self.wait_element_visible(loc.error_inquire_locator)
        return e.text.strip()