
# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : constant.py
# Author       : 大壮
# Create time  : 2019-10-10 21:21
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import os


class BasePath(object):
    pass


class ProjectPath(BasePath):
    # 获取路径 当前文件上一次就多写一个 os.path.dirname
    # 得到项目的名称
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 获取 用例数据 data 路径
    DATA_PATH = os.path.join(ROOT_PATH, 'data')

    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, 'setting')

    # 测试用例方法路径
    CASE_PATH = os.path.join(ROOT_PATH, 'test_case')

    # 存放测试报告路径
    REPORT_PATH = os.path.join(ROOT_PATH, 'report')

    # 判断路径是否存在，不存在则为新增
    # os.path.exists()   判断某个路径是否存在
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)  # os.mkdir()：创建目录


p_path = ProjectPath()
