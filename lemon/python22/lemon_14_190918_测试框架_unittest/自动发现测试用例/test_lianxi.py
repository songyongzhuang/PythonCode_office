# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : test_lianxi.py
# Author       : 大壮
# Create time  : 2019-09-19 21:39
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import unittest


def add(*args):
    s = 0
    for e in args:
        s += e
    return s


class TestAdd(unittest.TestCase):

    def setUp(self):
        """前置条件
        测试用例方法之前自动运行 setUp 里面的程序"""
        self.data = [
            {'a': (3, 4), 'expected': 7}]

        print('用例执行前置条件')

    def test_add_success(self):
        """ 判断表达式是否为真 """''
        self.assertTrue(self.data[0]['expected'] == add(*self.data[0]['a']))


if __name__ == '__main__':
    unittest.main()
