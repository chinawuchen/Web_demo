"""
    查询测试用例
"""
import sys, os
base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(base_path)

cases_success = [
    {"CaseName":"查询_成功_输入中文", "iqname": "web自动化", "expected": "web自动化"},
    {"CaseName":"查询_成功_输入英文", "iqname": "interface", "expected": "interface"},
]

cases_error = [
    {"CaseName":"查询_失败_没有找到匹配结果1", "iqname": "jiekou", "expected": "对不起，没有找到匹配结果。"},
    {"CaseName":"查询_失败_没有找到匹配结果2", "iqname": "，。，。，。，。，，。", "expected": "对不起，没有找到匹配结果。"},
    {"CaseName":"查询_失败_没有找到匹配结果3", "iqname": "Appium 是一个非常流行的开源自动化测试框架，支持各种操作系统的自动化。它可以与本机、混合和移动 Web 应用程序一起使用，以在各种环境中进行测试。它允许用户使用各种编程语言(如 Java、Perl、Python 等)编写自动化脚本。作为一个跨平台的测试工具，它将使用户能够通过结合Selenium WebDriver协议为 iOS、Windows 和 Android 运行移动自动化测试。Appium 在客户端-服务器架构上工作，由三个组件组成：Appium 客户端：它是用任何编程语言编写的自动化代码。Appium Server：它以JSON 格式接收并执行来自客户端的命令请求。终端设备：它是执行测试的仿真器或实时设备。是什么让 Appium 成为最好的移动自动化测试工具之一?它是一个开源自动化测试工具，因此是免费的。Appium 支持多种编程语言来编写测试脚本。它可以与各种 CI 工具集成，并通过 Internet 提供广泛的支持。总而言之，Appium 移动测试是应用测试自动化的绝佳选择。但是，它有一些限制：你不能在 Windows 设备上运行 Appium 检查器。Appium 在 iOS 和 Android 上的设置时间很复杂。Windows 操作系统不支持应用程序服务器的脚本录制。在包含 3000 多台真实设备的 Appium 云上自动化您的 iOS 应用程序。", "expected": "对不起，没有找到匹配结果。"},
]
