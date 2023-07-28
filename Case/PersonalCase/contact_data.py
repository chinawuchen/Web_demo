"""
    设置-个人资料页面-联系方式tab测试用例
"""

import sys
import os
base_path = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)


contact_cases_success = [
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq号存在", "qqempty": "yes", "qq": "1102055693", "qqvisible": "", "msnempty": "no", "msn": "",
      "tbempty": "no", "taobao": ""}, {"qq": "1102055693"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq号为空", "qqempty": "yes", "qq": "", "qqvisible": "", "msnempty": "no", "msn": "",
        "tbempty": "no", "taobao": ""}, {"qq": ""}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq号字段长", "qqempty": "yes", "qq": "12311020556931102055693110205569311020556931102055693", "qqvisible": "", "msnempty": "no", "msn": "",
        "tbempty": "no", "taobao": ""}, {"qq": "12311020556931102055693110205569311020556931102055693"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq公开", "qqempty": "", "qq": "", "qqvisible": "0", "msnempty": "no", "msn": "",
    "tbempty": "no", "taobao": ""}, {"qqvisible": "公开"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq好友可见", "qqempty": "", "qq": "", "qqvisible": "1", "msnempty": "no", "msn": "",
        "tbempty": "no", "taobao": ""}, {"qqvisible": "好友可见"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_qq保密", "qqempty": "", "qq": "", "qqvisible": "3", "msnempty": "no", "msn": "",
        "tbempty": "no", "taobao": ""}, {"qqvisible": "保密"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_msn存在", "qqempty": "", "qq": "", "qqvisible": "", "msnempty": "yes", "msn": "韩国大噶监管环境",
    "tbempty": "no", "taobao": ""}, {"msn": "韩国大噶监管环境"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_msn为空", "qqempty": "", "qq": "", "qqvisible": "", "msnempty": "yes", "msn": "",
        "tbempty": "no", "taobao": ""}, {"msn": ""}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_taobao存在", "qqempty": "", "qq": "", "qqvisible": "", "msnempty": "", "msn": "",
        "tbempty": "yes", "taobao": "uqeyuqwdashdhgajhgs"}, {"taobao": "uqeyuqwdashdhgajhgs"}),
    ({"CaseName": "设置-个人资料_联系方式_修改成功_taobao为空", "qqempty": "", "qq": "", "qqvisible": "", "msnempty": "", "msn": "",
    "tbempty": "yes", "taobao": ""}, {"taobao": ""}),
]

contact_cases_error = [
    ({"CaseName": "设置-个人资料_联系方式_修改失败_qq号含有敏感词汇", "qqempty": "yes", "qq": "含客户、产品", "qqvisible": "", "msnempty": "no", "msn": "",
      "tbempty": "no", "taobao": ""}, {"qq": "请检查该资料项 (含有敏感词汇)"}),
    ({"CaseName": "设置-个人资料_联系方式_修改失败_msn含有敏感词汇", "qqempty": "yes", "qq": "", "qqvisible": "", "msnempty": "yes", "msn": "含客户、产品",
        "tbempty": "no", "taobao": ""}, {"msn": "请检查该资料项 (含有敏感词汇)"}),
    ({"CaseName": "设置-个人资料_联系方式_修改失败_taobao含有敏感词汇", "qqempty": "", "qq": "", "qqvisible": "", "msnempty": "yes", "msn": "",
        "tbempty": "yes", "taobao": "含客户、产品"}, {"taobao": "请检查该资料项 (含有敏感词汇)"}),
]
