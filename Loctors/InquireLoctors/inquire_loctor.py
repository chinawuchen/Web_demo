import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from selenium.webdriver.common.by import By


class InquireLocator(object):

    inquire_locator = (By.ID, 'scform_srchtxt')
    submit_locator = (By.XPATH, '//button')
    success_inquire_locator = (By.XPATH, '//font')
    error_inquire_locator = (By.XPATH, '//p')