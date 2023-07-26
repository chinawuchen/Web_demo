"""
    个人资料页面-基本资料tab测试用例
"""

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

# 修改基本资料测试用例
information_cases_success = [
    {"CaseName": "个人资料_基本资料_修改成功-1", "bloodtype": "A", "gender": "1", "birthyear": "1993", "birthmonth": "9", "birthday": "28", "birthprovince": "江西省", "birthcity": "九江市",
        "birthdist": "湖口县", "birthcommunity": "文桥乡", "resideprovince": "广东省", "residecity": "广州市", "residedist": "海珠区", "residecommunity": "官洲街道", "expected": ["A", "男", "江西省 九江市 湖口县 文桥乡", "广东省 广州市 海珠区 官洲街道"]},
    {"CaseName": "个人资料_基本资料_修改成功-2", "bloodtype": "其它", "gender": "0", "birthyear": "1994", "birthmonth": "10", "birthday": "29", "birthprovince": "福建省", "birthcity": "龙岩市",
     "birthdist": "连城县", "birthcommunity": "北团镇", "resideprovince": "山东省", "residecity": "淄博市", "residedist": "沂源县", "residecommunity": "燕崖乡", "expected": ["其它", "保密", "福建省 龙岩市 连城县 北团镇", "山东省 淄博市 沂源县 燕崖乡"]},
]