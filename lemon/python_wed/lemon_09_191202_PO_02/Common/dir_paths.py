# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : dir_paths.py
# Author       : 大壮
# Create time  : 2019-12-07 15:53
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
""" 路径配置 """
import os


class ProjectPath(object):
    # 获取路径 当前文件上一次就多写一个 os.path.dirname
    # 得到项目的名称
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, r'setting')

    # 存放截图
    SCREENSHOT_PATH = os.path.join(ROOT_PATH, r'Outputs')

    # 存放测试报告路径
    REPORT_PATH = os.path.join(SCREENSHOT_PATH, r'report')

    # 判断路径是否存在，不存在则为新增
    # os.path.exists()   判断某个路径是否存在
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)  # os.mkdir()：创建目录


print(ProjectPath.ROOT_PATH)


