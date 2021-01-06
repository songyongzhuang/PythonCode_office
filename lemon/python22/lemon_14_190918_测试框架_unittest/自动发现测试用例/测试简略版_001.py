# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 测试简略版_001.py
# Author       : Administrator
# Create time  : 2019-09-20 16:23
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# 导入HTMLTestRunnerNew
from HTMLTestRunnerNew import HTMLTestRunner  # 生成HTML文件调用模块
import os  # 使用os模块获取路径
import unittest  # python自带单元测试模块

# 初始化 loader  测试加载器（TestLoader）
loader = unittest.TestLoader()
start_dir = os.path.dirname(os.path.abspath(__file__))
suite = loader.discover(start_dir)  # 找到文件路径运行

with open('测试报告_001.html', 'wb') as f:
    """ stream 文件流，可以传文件    verbosity 详细程度
    title=文件标题  description=文件的注释   tester=测试人员 """
    runner = HTMLTestRunner(f,
                            verbosity=2,
                            title='Python自动化VIP第22期',
                            tester='我是测试人员',
                            description='我是文件注释')
    # 运行
    runner.run(suite)
