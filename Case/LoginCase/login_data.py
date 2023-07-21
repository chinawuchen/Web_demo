"""
    登录测试用例
"""
import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

cases_success = [
    {"CaseName":"登录_登录成功", "username": "wuchen111", "password": "wu123456", "expected": "wuchen111"}
]

cases_error = [
    {"CaseName":"登录_登录失败", "username": "wuchen111", "password": "wu1234567", "expected": "密码错误"},
]