import os
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from datetime import datetime
# 初始化loader


loader = unittest.TestLoader()
# 自动发现测试用例
start_dir = os.path.dirname(os.path.abspath(__file__))
suite1 = loader.discover(start_dir)


report_dir = os.path.join(start_dir,"report")
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

file_name = os.path.join(report_dir,time_str+".html")

with open(file_name,"wb") as f:
    # 初始化runner
    runner = HTMLTestRunner(f,
                            verbosity=2,
                            title = "excel封装作业的测试报告",
                            description="测试结果如下所示",
                            tester="芊茗")
    # 运行
    runner.run(suite1)