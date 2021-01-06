# @Time : 2019/9/22 21:38 
# @Author : ZhangHaiQin
# @File : run.py 
# @Software: PyCharm
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime

# 构造测试集
suit = unittest.TestSuite()
# 初始化loader
loader = unittest.TestLoader()



start_dir = os.path.dirname(os.path.abspath(__file__))
suit1 = loader.discover(start_dir)

# 自动创建测试报告文件名
dir_str = datetime.now().strftime("%Y%m%d")
report_dir = os.path.join(start_dir, "report_"+dir_str)
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
file_str = datetime.now().strftime("%H-%M-%S")
file_name = os.path.join(report_dir, file_str + ".html")

# 运行测试用例，输出测试报告
with open(file_name, 'wb')as f:
    # 初始化runner
    runner = HTMLTestRunner(f,
                            verbosity=2,
                            title="20190922自动化测试用例",
                            description="Excel的操作",
                            tester="琴琴")
    # 使用run方法运行测试套间
    runner.run(suit1)
