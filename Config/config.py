"""
配置文件：
    存放常量
"""
import sys, os
import time
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)

# 隐式等待时间
IMPLICTLY_WAIT_TIMEOUT = 20
# 项目根地址
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# image_path 保存截图的路径
IMAGE_PATH = os.path.join(ROOT_PATH, "Files/screeshots")
# 日志地址
LOG_PATH = os.path.join(ROOT_PATH, "Files/log")
# 用于文件上传功能的文件地址
FILES_PATH = os.path.join(ROOT_PATH, "Files/uploadfile")
# 测试结果数据保存的目录，json类型
XML_REPORT_PATH = os.path.join(ROOT_PATH, "Files/Reports/xml")
# 生成HTML格式的测试报告保存的目录
HTML_REPORT_PATH = os.path.join(ROOT_PATH, "Files/Reports/html")


if __name__ == "__main__":
    print(IMAGE_PATH)