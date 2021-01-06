# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : dir_path.py
# Author       : 大壮
# Create time  : 2020/12/19 16:04
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import os


class DirPath(object):
    # 框架项目顶层目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试数据
    testdatas_dir = os.path.join(base_dir, r"test_datas")
    # 运行层
    testcases_dir = os.path.join(base_dir, r"test_cases")
    # 测试运行数据文件
    data_dir = os.path.join(base_dir, "outputs")
    # 测试报告
    htmlreport_dir = os.path.join(data_dir, r"reports")
    # 测试日志
    logs_dir = os.path.join(data_dir, r"logs")
    # 文件截图
    screenshot_dir = os.path.join(data_dir, r"screenshots")
    print('框架项目顶层路径', base_dir)
    print('测试报告路径', htmlreport_dir)
    print('测试日志路径', logs_dir)
    print('文件截图路径', screenshot_dir)
