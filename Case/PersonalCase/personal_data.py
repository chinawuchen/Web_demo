"""
    个人资料页面-基本资料tab测试用例
"""

import sys
import os
base_path = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

# 修改基本资料测试用例
information_cases_success = [
    ({"CaseName": "个人资料_基本资料_修改成功-血型其它", "bloodtype": "其它", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"bloodtype": "其它"}),
    ({"CaseName": "个人资料_基本资料_修改成功-血型A", "bloodtype": "A", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"bloodtype": "A"}),
    ({"CaseName": "个人资料_基本资料_修改成功-血型B", "bloodtype": "B", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"bloodtype": "B"}),
    ({"CaseName": "个人资料_基本资料_修改成功-血型AB", "bloodtype": "AB", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"bloodtype": "AB"}),
    ({"CaseName": "个人资料_基本资料_修改成功-血型O", "bloodtype": "O", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"bloodtype": "O"}),
    ({"CaseName": "个人资料_基本资料_修改成功-性别保密", "bloodtype": "", "gender": "0", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
        "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"gender": "保密"}),
    ({"CaseName": "个人资料_基本资料_修改成功-性别男", "bloodtype": "", "gender": "1", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
        "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"gender": "男"}),
    ({"CaseName": "个人资料_基本资料_修改成功-性别女", "bloodtype": "", "gender": "2", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
        "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"gender": "女"}),
    ({"CaseName": "个人资料_基本资料_修改成功-居住地省、市、县/区、乡", "bloodtype": "", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "", "birthcity": "",
      "birthdist": "", "birthcommunity": "", "resideprovince": "广东省", "residecity": "广州市", "residedist": "天河区", "residecommunity": "沙河街道", }, {"reside": "广东省 广州市 天河区 沙河街道 (修改)"}),
    ({"CaseName": "个人资料_基本资料_修改成功-出生地省、市、县/区、乡", "bloodtype": "", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "广东省", "birthcity": "广州市",
      "birthdist": "天河区", "birthcommunity": "沙河街道", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"birth": "广东省 广州市 天河区 沙河街道 (修改)"}),
    ({"CaseName": "个人资料_基本资料_修改成功-出生地省、市、县/区", "bloodtype": "", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "江西省", "birthcity": "九江市",
        "birthdist": "九江县", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"birth": "江西省 九江市 九江县 (修改)"}),
    ({"CaseName": "个人资料_基本资料_修改成功-出生地省、市", "bloodtype": "", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "江西省", "birthcity": "南昌市",
        "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"birth": "江西省 南昌市 (修改)"}),
    ({"CaseName": "个人资料_基本资料_修改成功-出生地省", "bloodtype": "", "gender": "", "birthyear": "", "birthmonth": "", "birthday": "", "birthprovince": "广东省", "birthcity": "",
        "birthdist": "", "birthcommunity": "", "resideprovince": "", "residecity": "", "residedist": "", "residecommunity": "", }, {"birth": "广东省 (修改)"}),
]