# --*-- coding : utf-8 --*--
# Project      : test-yqhk-Project
# Current file : dir_path.py
# Author       : 菜鸟一号
# Create time  : 2020-12-10 09:51
# IDE          : PyCharm
# MAIL         : 邮箱地址
# TODO 成长很苦，进步很甜，加油！
import os


class DirPath(object):
    # 框架项目顶层目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 生成的截图文件夹
    screenshot_dir = os.path.join(base_dir, r"screenshots")
    # 公共类，常用类
    framework_dir = os.path.join(base_dir, 'framework')
    # 日志
    logs_dir = os.path.join(framework_dir, 'logs')
    # print(logs_dir)
    print(os.path.exists(logs_dir))
    if os.path.exists(logs_dir) is False:
        os.mkdir(logs_dir)
