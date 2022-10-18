# 　扫描模块并根据程序中内嵌的文档字符串执行测试。
# 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致
def average(values):
    """
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


# import doctest
# doctest.testmod()

# unittest模块 测试集
import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])


# unittest.main()
