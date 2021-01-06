# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : main_pytest.py
# Author       : 大壮
# Create time  : 2019-12-15 17:21
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest

pytest.main(['-s', '-v'])  # 搜索当前目录下，所有的测试用例i

# pytest.main(['-m', 'smoke', '-s', '-v'])  # 搜索当前目录下, 目录运行打标记的
# ['-s', '-v'] 运行当前文件夹包括子文件所有的用例
# -s是会运行print的内容，-v是会把用例的名称啥的详细信息打印出来

