# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 自动发现测试用例(重点).py
# Author       : Administrator
# Create time  : 2019-09-20 17:11
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import os
import unittest

# TODO 自动发现测试用例  loader.discover 返回的结果就是一个集合
# TODO suitel = unittest.TestSuite()

# 初始化 loader  测试加载器（TestLoader）
loader = unittest.TestLoader()

# 自动发现测试用例, 自动发现文件夹，以test开头的项目(一个py文件就是一个项目)、
# 第一个传递的需要一个文件夹路径，
start_dir = os.path.dirname(os.path.abspath(__file__))
suite = loader.discover(start_dir)  # 返回一个集合，直接使用集合当做参数

# 生成 , 测试报告文件
with open('自动发现测试用例.txt', 'w', encoding='utf-8') as f:
    # 初始化 runner
    runner = unittest.TextTestRunner(f, verbosity=2)
    # 运行
    runner.run(suite)
