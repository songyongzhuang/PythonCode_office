# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : run.py
# Author       : Administrator
# Create time  : 2019-09-19 15:19
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# 初始化一个对象 suite 测试套件（集合）
import unittest

from lemon_14_190918_测试框架_unittest import test_练习相加01
from lemon_14_190918_测试框架_unittest import test_练习相减02
from lemon_14_190918_测试框架_unittest.test_练习相加01 import TestAdd
from lemon_14_190918_测试框架_unittest.test_练习相减02 import TestMinus


# 使用 TestLoader 注释下面的代码

cases = [TestAdd('test_add_success'),
         TestAdd('test_add_error'),
         TestMinus('test_add_success'),
         TestMinus('test_add_error')
         ]
# 1.初始化测试套件
suite = unittest.TestSuite(tests=cases)

'''
# 2.往套件里面添加测试用例
# addTests与addTest的区别, 第一个可以添加多个，第二个只能添加一个
# 需要一个一个去添加 TestAdd（） 里面的方法名，添加字符串
# 格式：类名称（’方法名称‘）

"""
cases = [TestAdd('test_add_success'),
         TestAdd('test_add_error'),
         TestMinus('test_add_success'),
         TestMinus('test_add_error')
         ]
suite.addTests(cases)
"""
'''


# TestLoader 用来加载测试用例
# 可以根据模块加载、根据测试类加载、自己定义规则，让他们自动发现
loader = unittest.TestLoader()

# 根据测试类去加载测试用例
cases = loader.loadTestsFromTestCase(TestAdd)
cases2 = loader.loadTestsFromTestCase(TestMinus)

cases3 = loader.loadTestsFromModule(test_练习相加01)
cases4 = loader.loadTestsFromModule(test_练习相减02)

# 初始化测试套件, 往套件里面添加测试用例
suite = unittest.TestSuite()
suite.addTests(cases3)
suite.addTests(cases4)


# 运行 , 测试报告文件, demo.txt
with open('demo.txt', 'w', encoding='utf-8') as f:
    # 初始化 runner
    # stream 文件流，可以传文件
    # verbosity 详细程度
    runner = unittest.TextTestRunner(f, verbosity=0)

    # 运行
    runner.run(suite)
