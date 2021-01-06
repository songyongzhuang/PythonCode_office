#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/9 20:46
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os
import unittest

from ddt import ddt, data
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.老师上课写代码.common.config_handler \
    import ConfigHandler, config
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.老师上课写代码.common.excel_handler \
    import ExcelHandler
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.老师上课写代码.func.calc \
    import add
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.老师上课写代码.setting.constant \
    import p_path

# 默认值就是叫 cases.xlsx
# 配置文件 文件夹 + 配置文件里面 cases.xlsx
# 通过读取配置文件得到 cases.xlsx
file_name = config.read('excel', 'file_name')
file_path = os.path.join(p_path.DATA_PATH, file_name)

# 获取 sheetname
sheet_name = config.read('excel', 'add_sheet')

# 读取 excel 数据
test_data = ExcelHandler(file_path).read(sheet_name)


@ddt
class TestAdd(unittest.TestCase):

    @data(*test_data)
    def test_add(self, test_info):
        a = test_info[2]
        actual = add(*eval(test_info[1]))
        # test_info[2] (字符串，数字)
        # actual, (数字，None)
        try:
            self.assertEqual(eval(str(test_info[2])),  actual)
        except AssertionError:
            # logging.info
            raise AssertionError
        # self.assertEqual(str(test_info[2]),  str(actual))
        # 断言失败 抛出异常：AssertionError
