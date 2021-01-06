# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 练习练习.py
# Author       : Administrator
# Create time  : 2019-09-20 13:23
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

import unittest
from lemon_14_190918_测试框架_unittest.test_练习相加01 import TestAdd
from lemon_14_190918_测试框架_unittest.test_练习相减02 import TestMinus

# 1.初始化测试套件
suite = unittest.TestSuite()
# 2.往套件里面添加测试用例
# addTests与addTest的区别, 第一个可以添加多个，第二个只能添加一个
# 需要一个一个去添加 TestAdd（） 里面的方法名，添加字符串
# 格式：类名称（’方法名称‘）
cases = [TestAdd('test_add_success'),
         TestAdd('test_add_error'),
         TestMinus('test_add_success'),
         TestMinus('test_add_error')
         ]
suite.addTests(cases)
# 运行 , 测试报告文件, demo.txt
with open('demo111.txt', 'w', encoding='utf-8') as f:
    # 初始化 runner
    runner = unittest.TextTestRunner(f)
    # 运行
    runner.run(suite)
