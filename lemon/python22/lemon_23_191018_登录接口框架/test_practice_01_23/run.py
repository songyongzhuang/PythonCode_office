# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : run_practice_02.py
# Author       : Administrator
# Create time  : 2019-10-11 14:56
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！


# 导入HTMLTestRunnerNew
from HTMLTestRunnerNew import HTMLTestRunner  # 生成HTML文件调用模块
import os  # 使用os模块获取路径
import unittest  # python自带单元测试模块
from datetime import datetime  # 时间模块
from lemon_23_191018_登录接口框架.test_practice_01_23.setting_配置文件_4.constant import p_path

# 初始化 loader
loader = unittest.TestLoader()
# 自动发现测试用例方法
# loader.discover 返回的结果就是一个集合的对象
suite = loader.discover(p_path.CASE_PATH)  # 直接调用配置文件里面写好的路径

"""
# join 字符串拼接，首先使用文件夹路径，放在start_dir路径的上一层级
# report_dir = os.path.join(os.path.dirname(start_dir), '存放测试报告')

# 判断路径是否存在，不存在则为新增
# os.path.exists()   判断某个路径是否存在
if not os.path.exists(p_path.REPORT_PATH):
    os.mkdir(p_path.REPORT_PATH)  # os.mkdir()：创建目录
"""

# 生成HTML
# 测试报告文件, 放到一个文件夹里面，可以根据时间动态生成文件名字
# 使用datetime模块,now 现在时间，strftime把现在时间转换成字符串
time_str = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

file_name = os.path.join(p_path.REPORT_PATH, time_str + '测试报告.html')

# main
if __name__ == '__main__':
    with open(file_name, 'wb') as f:
        """ stream 文件流，可以传文件    verbosity 详细程度
        title=文件标题  description=文件的注释   tester=测试人员 """
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='Python自动化VIP第22期',
                                tester='我是测试人员',
                                description='我是文件注释')
        # 运行
        runner.run(suite)
