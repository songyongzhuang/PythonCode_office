# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : main.py
# Author       : 大壮
# Create time  : 2020-12-21 17:04
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest


pytest.main(['-s', '-v',  # 搜索当前目录下，所有的测试用例i
             '--reruns', '2', '--reruns-delay', '5',  # 失败重运行两次，重运行间隔五秒
             '--alluredir=outputs/reports'])  # 生成测试报告


# TODO 生成报错 allure serve outputs\reports

# pytest.main(['-m', 'smoke', '-s', '-v'])  # 搜索当前目录下, 目录运行打标记的

# ['-s', '-v'] 运行当前文件夹包括子文件所有的用例
# -s是会运行print的内容，-v是会把用例的名称啥的详细信息打印出来
