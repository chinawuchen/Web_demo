import pytest
import shutil
import sys
import os
# base_path = os.path.abspath("")
# sys.path.append(base_path)
from Config import config
from Common.base_shell import Shell


if __name__ == '__main__':
    # 测试结果数据保存的目录，json类型
    xml_report_path = config.XML_REPORT_PATH
    # 生成HTML格式的测试报告保存的目录
    html_report_path = config.HTML_REPORT_PATH
    # 清空测试结果目录xml，再重新创建此目录
    shutil.rmtree(xml_report_path)
    os.mkdir(xml_report_path)
    # 定义测试集合并执行
    args = ['-v', '-s', '-q', '--alluredir', xml_report_path]
    try:
        pytest.main(args)
    except Exception:
        raise

    # 生成测试报告
    shell = Shell()
    run_test_cmd = 'allure generate %s -o %s --clean' % (
        xml_report_path, html_report_path)
    open_report_cmd = "allure open %s" % (html_report_path)
    shell.invoke(run_test_cmd)
    # 打开测试报告
    shell.invoke(open_report_cmd)