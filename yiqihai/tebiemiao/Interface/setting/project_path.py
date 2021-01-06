# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : project_path.py
# Author       : 大壮
# Create time  : 2020-01-26 15:38
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import os
from datas.dir_data import DirData


class ProjectPath(object):
    # 项目路径
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 记录日志、HTML 文件路径
    data_dir = os.path.join(base_dir, "outputs")
    # 测试报告
    htmlreport_dir = os.path.join(data_dir, r"reports")
    # 测试日志
    logs_dir = os.path.join(data_dir, r"logs")

    # 测试数据 (excel文件中、项目全局数据)
    test_data_dir = os.path.join(base_dir, 'datas')
    # 拼接测试数据excel路劲及名字
    data_excel = os.path.join(test_data_dir, DirData.fire_name)


if __name__ == '__main__':
    pp = ProjectPath()
    print('项目路径：', pp.base_dir)
    print('测试数据excel：', pp.test_data_dir)
    print('测试数据excel路劲及名字', pp.data_excel)
