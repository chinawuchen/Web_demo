"""
    设置-个人资料页面-工作情况tab测试用例
"""

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

# 修改工作情况测试用例
conditions_cases_success = [
    ({"CaseName": "设置-个人资料_工作情况_修改成功_自我介绍输入长", "visempty": "yes", "visitors": "三星堆古遗址位于四川省广汉市西北的鸭子河南岸，分布面积12平方千米，距今已有3000至5000年历史，是迄今在西南地区发现的范围最大、延续时间最长、文化内涵最丰富的古城、古国、古蜀文化遗址。现有保存最完整的东、西、南城墙和月亮湾内城墙。三星堆遗址被称为20世纪人类最伟大的考古发现之一，昭示了长江流域与黄河流域一样，同属中华文明的母体，被誉为“长江文明之源”。",
        "gender": "0", "cisempty": "yes", "company": "mou蔡徐坤有限公司有限公司有限公司有限公司", "companylog": ""}, {"visitors": "三星堆古遗址位于四川省广汉市西北的鸭子河南岸，分布面积12平方千米，距今已有3000至5000年历史，是迄今在西南地区发现的范围最大、延续时间最长、文化内涵最丰富的古城、古国、古蜀文化遗址。现有保存最完整的东、西、南城墙和月亮湾内城墙。三星堆遗址被称为20世纪人类最伟大的考古发现之一，昭示了长江流域与黄河流域一样，同属中华文明的母体，被誉为“长江文明之源”。"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_自我介绍输入短", "visempty": "yes", "visitors": "我是蔡徐坤", "gender": "1", "cisempty": "yes", "company": "蔡徐坤有限公司",
        "companylog": ""}, {"visitors": "我是蔡徐坤"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_性别女", "visempty": "no", "visitors": "", "gender": "2", "cisempty": "no", "company": "",
      "companylog": ""}, {"gender": "女"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_性别保密", "visempty": "no", "visitors": "", "gender": "0", "cisempty": "no", "company": "",
      "companylog": ""}, {"gender": "保密"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_公司名输入长", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司",
      "companylog": ""}, {"company": "蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司蔡徐坤有限公司"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_公司名输入中英文标点符号", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "da大会，。qweu",
      "companylog": ""}, {"company": "da大会，。qweu"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_公司属性猎头", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "da大会，。qweu",
        "companylog": "猎头"}, {"companylog": "猎头"}),
    ({"CaseName": "设置-个人资料_工作情况_修改成功_公司属性企业", "visempty": "no", "visitors": "", "gender": "1", "cisempty": "yes", "company": "da大会，。qweu",
        "companylog": "企业"}, {"companylog": "企业"}),
]

conditions_cases_error = [
    ({"CaseName": "设置-个人资料_工作情况_自我介绍含有敏感词汇", "visempty": "yes", "visitors": "通过与项目团队（含客户、产品）",
        "gender": "", "cisempty": "no", "company": "", "companylog": ""}, {"visitors": "请检查该资料项 (含有敏感词汇)"}),
    ({"CaseName": "设置-个人资料_工作情况_公司名称为空", "visempty": "yes", "visitors": "哈哈哈哈", "gender": "1", "cisempty": "yes", "company": "",
     "companylog": "猎头"}, {"company": "请检查该资料项"}),
    ({"CaseName": "设置-个人资料_工作情况_公司名称含有敏感词汇", "visempty": "no", "visitors": "",
      "gender": "", "cisempty": "yes", "company": "通过与项目团队（含客户、产品）", "companylog": ""}, {"company": "请检查该资料项 (含有敏感词汇)"}),
]
