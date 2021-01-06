# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_add_数据相加.py
# Author       : Administrator
# Create time  : 2019-09-19 18:20
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import unittest


def add(a, *args):  # add 加起来,
    """ 相加 """''
    b = 0
    for i in args:
        b += i
    return b + a


class TestAdd(unittest.TestCase):

    # 测试用例的设计
    # 前置条件
    def setUp(self):
        """前置条件
        测试用例方法之前自动运行 setUp 里面的程序"""
        self.data = [
            {'a': 0, 'b': (3, 4), 'expected': 7},
            {'a': 0, 'b': (1, 1, 12), 'expected': 14}
        ]
        print('用例执行前置条件')

    # 后置条件
    def tearDown(self):
        """后置条件
        测试用例方法之后自动运行 tearDown 里面的程序"""
        print('用例执行后置条件')

    def test_add_success(self):
        """ 判断表达式是否为真 """''
        self.assertTrue(self.data[0]['expected'] == add(self.data[0]['a'], *self.data[0]['b']))

    def test_add_error(self):
        """如果确定两个对象不相等，则失败。"""''
        self.assertEqual(self.data[1]['expected'], (add(self.data[1]['a'], *self.data[1]['b'])))


if __name__ == '__main__':
    unittest.main()
