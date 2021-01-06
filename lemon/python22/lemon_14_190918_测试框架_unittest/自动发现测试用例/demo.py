# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : demo.py
# Author       : Administrator
# Create time  : 2019-09-19 18:14
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# 导入HTMLTestRunnerNew
from HTMLTestRunnerNew import HTMLTestRunner  # 生成HTML文件调用模块
import os  # 使用os模块获取路径
import unittest  # python自带单元测试模块
from datetime import datetime  # 时间模块

# 初始化 loader
loader = unittest.TestLoader()
# 自动发现测试用例
# 获取路径的文件夹路径  os.path.dirname(os.path.abspath(__file__))
start_dir = os.path.dirname(os.path.abspath(__file__))
suite = loader.discover(start_dir)  # loader.discover 返回的结果就是一个集合的对象

# 生成HTML
# 测试报告文件, 放到一个文件夹里面，可以根据时间动态生成文件名字
# join 字符串拼接，首先使用文件夹路径
report_dir = os.path.join(start_dir, '我是文件夹')

# os.path.exists()   判断某个路径是否存在
if not os.path.exists(report_dir):
    os.mkdir(report_dir)  # os.mkdir()：创建目录

# 使用datetime模块,now 现在时间，strftime把现在时间转换成字符串
time_str = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


file_name = os.path.join(report_dir, time_str + '123456测试报告.html')
with open(file_name, 'wb') as f:
    """ stream 文件流，可以传文件    verbosity 详细程度
    title=文件标题  description=文件的注释   tester=测试人员 """
    runner = HTMLTestRunner(f,
                            verbosity=2,
                            title='Python自动化VIP第22期',
                            tester='我是测试人员',
                            description='我是文件注释')
    # 运行
    runner.run(suite)
