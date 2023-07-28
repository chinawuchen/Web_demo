import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

from Loctors.PersonalLocators.condition_locator import ConditionLocator as loc
from Common.base_page import BasePage


"""设置-密码安全页面操作"""