# --*-- coding : utf-8 --*--
# Project      : Interface_test
# Current file : dir_path.py
# Author       : 大壮
# Create time  : 2020-07-12 11:21
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import os


class DirPath(object):
    # 框架顶层目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试数据层
    datas_dir = os.path.join(base_dir, r'datas')
    # 测试运行数据文件
    data_dir = os.path.join(base_dir, r'outputs')
    # 测试日志
    logs_dir = os.path.join(data_dir, r'logs')
