'''
    这里放置各个页面的地址
    '''

import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)


# host
HOST = "http://bbs.51testing.com"
# 登录页面地址
login_url = HOST + "/forum.php"
# 查询页面地址
inquire_url = HOST + "/search.php"
# 个人资料页面地址
personal_url = HOST + "/home.php?mod=spacecp&ac=profile"
