
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: 小简
# Time: 2018/11/28 17:04

import os

# 框架项目顶层目录
# base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据
testdatas_dir = os.path.join(base_dir, "TestDatas")
# 运行层
testcases_dir = os.path.join(base_dir, "TestCases")
# 测试报告
htmlreport_dir = os.path.join(base_dir, "Outputs/reports")
# 测试日志
logs_dir = os.path.join(base_dir, "Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")
# 文件截图
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")

print(screenshot_dir)
