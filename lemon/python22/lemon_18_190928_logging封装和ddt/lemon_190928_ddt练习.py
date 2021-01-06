# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : lemon_190928_ddt练习.py
# Author       : Administrator
# Create time  : 2019-09-30 09:40
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# 1.ddt是和unittest搭配起来使用的
# 2.怎么把测试用例方法合并，判断的依据是测试步骤，代码一样，(测试数据不同)
# 3.当我们输入一组数据的时候，测试框架生成独立的多个测试用例方法
# 4.数据驱动。根据数据有多少个数据，就生成多少个测试用例，
# 5.ddt实现了数据驱动思想

import unittest
import ddt


def add(param, param1):
    return param + param1


test_data = [
    ((3, 4), 7, 1),
    ((3, 5), 8, 2),
    ((3, 6), 9, 3)
]

# 测试类上面带了一个ddt的帽子 固定用法
@ddt.ddt
class TestAdd(unittest.TestCase):

    # 测试方法上带ddt的数据帽子 *号表示解包，每一组数据都是一个参数
    @ddt.data(*test_data)
    # 每次运行都会从test_data中取出一组数据，动态生成一个独立的测试用例方法
    def test_add(self, test_info):  # 只有一个参数不要使用data
        self.assertEqual(test_info[1], add(*test_info[0]))

# ddt, 导入方法
# @data(*test_data), @ddt没有括号
# def test_add_1(self, data), 只有一个参数
