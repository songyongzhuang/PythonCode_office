# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_练习相减02.py
# Author       : Administrator
# Create time  : 2019-09-19 10:22
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import unittest


def minus(a, b):  # add 加起来
    """ 相减 """''
    return a - b


x = 3
y = 5
expected = -2


class TestMinus(unittest.TestCase):

    # 测试类方法，每一个测试类只运行一次
    @classmethod
    def setUpClass(cls):
        print('每一个测试类之前只运行一次')

    @classmethod
    def tearDownClass(cls):
        print('每一个测试类之后只运行一次')

    # 测试用例的设计
    # 前置条件
    def setUp(self):
        """前置条件
        测试用例方法之前自动运行 setUp 里面的程序"""
        print('每个测试用例执行前置条件')

    # 后置条件
    def tearDown(self):
        """后置条件
        测试用例方法之后自动运行 tearDown 里面的程序"""
        print('每个测试用例执行后置条件')

    def test_add_success(self):
        """ 判断表达式是否为真 """''
        self.assertTrue(expected == minus(x, y))

    def test_add_error(self):
        """如果确定两个对象不相等，则失败。"""''
        try:
            self.assertEqual(-2, minus(x, y))
        except SyntaxError:
            pass


if __name__ == '__main__':
    unittest.main()
