"""
    设置-密码安全页面测试用例
"""

import sys
import os
base_path = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)


# 修改密码正常测试用例
setpswd_cases_success = [
    ({"CaseName": "设置-修改密码_旧新密码正确", "clear_old": "yes", "oldpassword": "wu123456", "clear_new": "yes",
     "newpassword": "wu123456", "clear_new2": "yes", "newpassword2": "wu123456", }, {"expected": "您需要先登录才能继续本操作"}),
]

setpswd_cases_error = [
    ({"CaseName": "设置-修改密码_旧密码错误", "clear_old": "yes", "oldpassword": "wu123", "clear_new": "yes",
     "newpassword": "wu123456", "clear_new2": "yes", "newpassword2": "wu123456", }, {"expected": "原密码不正确，您不能修改密码或 Email 或安全提问"}),
    ({"CaseName": "设置-修改密码_旧密码为空", "clear_old": "yes", "oldpassword": "", "clear_new": "yes",
      "newpassword": "wu123456", "clear_new2": "yes", "newpassword2": "wu123456", }, {"expected": "原密码不正确，您不能修改密码或 Email 或安全提问"}),
    ({"CaseName": "设置-修改密码_新密码1和2不一致", "clear_old": "yes", "oldpassword": "wu123456", "clear_new": "yes",
      "newpassword": "wu123457", "clear_new2": "yes", "newpassword2": "wu12345890", }, {"expected": "抱歉，两次输入的密码不一致"}),
]
