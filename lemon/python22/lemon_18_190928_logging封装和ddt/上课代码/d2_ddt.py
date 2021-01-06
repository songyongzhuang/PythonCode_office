#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/28 21:30
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# ddt 是和 unittest 搭配起来使用的
# 怎么把测试用例方法合并，判断的依据是测试步骤，代码一样，(测试数据不同)
# 当我们输入一组数据的时候，测试框架生成独立的多个测试用例的方法
# 数据驱动。 ddt 实现了数据驱动思想。
# ddt != 数据驱动
# 安装 ddt

import unittest
from ddt import ddt, data

def add(param, param1):
    return param + param1



test_data = [
    ((3,4), 8, 1),
    ((3,5), 8, 2),
]

# 测试类上面带一个ddt 的帽子
@ddt
class TestAdd(unittest.TestCase):

    # 测试方法上带ddt 的数据帽子
    @data(*test_data)
    # @ddt.data(((3,4), 8, 1), ((3,5), 8, 2), ((3,6), 9, 3))
    # 每次运行都会从 test_data 中取出一组数据，动态生成一个独立的测试用例方法
    def test_add_1(self, test_info):
        print(test_info)
        self.assertEqual(add(3,4), 7)

    # @ddt.data(*test)
    def test_add_2(self, test_info):
        print(test_info)
        self.assertEqual(add(3,5), 8)

    # def ...

# ddt, 导入
# @data(*test_data), @ddt没有括号
# def test_add_1(self, data_info): #尽量不要用data

