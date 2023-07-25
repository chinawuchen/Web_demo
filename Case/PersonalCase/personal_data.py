"""
    个人资料页面测试用例
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



# 修改工作情况测试用例
conditions_cases_success = [
    ({"CaseName": "个人资料_工作情况_修改成功_自我介绍输入长", "visempty": "yes", "visitors": "三星堆古遗址位于四川省广汉市西北的鸭子河南岸，分布面积12平方千米，距今已有3000至5000年历史，是迄今在西南地区发现的范围最大、延续时间最长、文化内涵最丰富的古城、古国、古蜀文化遗址。现有保存最完整的东、西、南城墙和月亮湾内城墙。三星堆遗址被称为20世纪人类最伟大的考古发现之一，昭示了长江流域与黄河流域一样，同属中华文明的母体，被誉为“长江文明之源”。",
        "gender": "0", "cisempty": "yes", "company": "mou蔡徐坤有限公司有限公司有限公司有限公司", "companylog": "企业"}, {"visitors": "三星堆古遗址位于四川省广汉市西北的鸭子河南岸，分布面积12平方千米，距今已有3000至5000年历史，是迄今在西南地区发现的范围最大、延续时间最长、文化内涵最丰富的古城、古国、古蜀文化遗址。现有保存最完整的东、西、南城墙和月亮湾内城墙。三星堆遗址被称为20世纪人类最伟大的考古发现之一，昭示了长江流域与黄河流域一样，同属中华文明的母体，被誉为“长江文明之源”。"}),
    ({"CaseName": "个人资料_工作情况_修改成功_自我介绍输入短", "visempty": "yes", "visitors": "我是蔡徐坤", "gender": "1", "cisempty": "yes", "company": "蔡徐坤有限公司",
        "companylog": "猎头"}, {"visitors": "我是蔡徐坤"}),
    ({"CaseName": "个人资料_工作情况_修改成功_性别女", "visempty": "no", "visitors": "", "gender": "2", "cisempty": "no", "company": "",
      "companylog": ""}, {"gender": "女"}),
    ({"CaseName": "个人资料_工作情况_修改成功_性别保密", "visempty": "no", "visitors": "", "gender": "0", "cisempty": "no", "company": "",
      "companylog": ""}, {"gender": "保密"}),
    ({"CaseName": "个人资料_工作情况_修改成功_公司名输入长", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司",
      "companylog": "猎头"}, {"company": "蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司"}),
    ({"CaseName": "个人资料_工作情况_修改成功_公司名输入中英文标点符号", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "da大会，。qweu",
      "companylog": "猎头"}, {"company": "da大会，。qweu"}),
]

conditions_cases_error = [
    ({"CaseName": "个人资料_工作情况_自我介绍含有敏感词汇", "visempty": "yes", "visitors": "通过与项目团队（含客户、产品）",
        "gender": "", "cisempty": "no", "company": "", "companylog": ""}, {"visitors": "请检查该资料项 (含有敏感词汇)"}),
    ({"CaseName": "个人资料_工作情况_公司名称为空", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "",
     "companylog": "猎头"}, {"company": "请检查该资料项"}),
    ({"CaseName": "个人资料_工作情况_公司名称含有敏感词汇", "visempty": "no", "visitors": "",
      "gender": "", "cisempty": "yes", "company": "通过与项目团队（含客户、产品）", "companylog": ""}, {"company": "请检查该资料项 (含有敏感词汇)"}),
]