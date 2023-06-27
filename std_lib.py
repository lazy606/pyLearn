# Python3 标准库概览
'''
os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。

sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。

time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。

datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。

random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。

math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。

re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。

json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。

urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。
'''

# 测试模块
'''
doctes模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试结构如同简单的将它的输出结果剪切并粘贴到文档字符串中
'''
import doctest

doctest.testmod()  # 自动验证嵌入测试

'''
unittest模块不想doctest模块那么容易使用，不过它可以在一个独立的文件里面提供一个更全面的测试集
'''
import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()
