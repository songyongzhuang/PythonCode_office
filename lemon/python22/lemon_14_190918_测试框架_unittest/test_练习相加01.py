# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_练习相加01.py
# Author       : Administrator
# Create time  : 2019-09-19 10:21
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import unittest


def add(a, b):  # add 加起来
    """ 相加 """''
    return a + b

# 在前置条件中添加了测试数据这是先注释


x = 3
y = 5
expected = 8


class TestAdd(unittest.TestCase):

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
        # self.data = [
        #     {'a': 3, 'b': 4, 'expected': 7},
        #     {'a': 5, 'b': 9, 'expected': 14}
        # ]
        print('用例执行前置条件')

    # 后置条件
    def tearDown(self):
        """后置条件
        测试用例方法之后自动运行 tearDown 里面的程序"""
        print('用例执行后置条件')

    def test_add_success(self):
        """ 判断表达式是否为真 """''
        self.assertTrue(expected == add(x, y))  # 在前置条件中添加了测试数据这是先注释
        # self.assertTrue(self.data[0]['expected'] == add(self.data[0]['a'], self.data[0]['b']))

    def test_add_error(self):
        """如果确定两个对象不相等，则失败。"""''
        self.assertEqual(7, add(x, y))  # 在前置条件中添加了测试数据这是先注释
        # self.assertEqual(self.data[1]['expected'], add(self.data[1]['a'], self.data[1]['b']))


# class TestAddTwo(unittest.TestCase):
#
#     def test_add_success_2(self):
#         """ 判断表达式是否为真 """''
#         self.assertTrue(expected == add(x, y))
#
#     def test_add_error_2(self):
#         """如果确定两个对象不相等，则失败。"""''
#         self.assertEqual(7, add(x, y))


if __name__ == '__main__':

    unittest.main()
