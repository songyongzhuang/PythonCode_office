# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : run_003修改两次_TestLoader.py
# Author       : Administrator
# Create time  : 2019-09-20 16:40
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# 初始化一个对象 suite 测试套件（集合）
import unittest

from lemon_14_190918_测试框架_unittest import test_练习相加01
from lemon_14_190918_测试框架_unittest import test_练习相减02

# 第一步
# TestLoader 用来加载测试用例
# 可以根据模块加载、根据测试类加载、自己定义规则，让他们自动发现
loader = unittest.TestLoader()

# 第二步、根据测试类去加载测试用例
cases = loader.loadTestsFromModule(test_练习相加01)
cases1 = loader.loadTestsFromModule(test_练习相减02)

# 初始化测试套件, 往套件里面添加测试用例
suite = unittest.TestSuite()
suite.addTests(cases)
suite.addTests(cases1)


# 生成 , 测试报告文件
with open('demo_run_003.txt', 'w', encoding='utf-8') as f:
    # 初始化  runner stream 文件流，可以传文件  verbosity 详细程度
    runner = unittest.TextTestRunner(f, verbosity=0)

    # 运行
    runner.run(suite)
