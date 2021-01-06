# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_minus_数据相减.py
# Author       : Administrator
# Create time  : 2019-09-19 18:21
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import unittest


def minus(a, b):  # add 加起来
    """ 相减"""''
    return a - b


x = 5
y = 3
expected = 2


class TestMinus(unittest.TestCase):

    def test_add_success(self):
        """ 判断表达式是否为真 """''
        self.assertTrue(expected == minus(x, y))

    def test_add_error(self):
        """如果确定两个对象不相等，则失败。"""''
        self.assertEqual(expected, minus(x, y))


if __name__ == '__main__':
    unittest.main()
