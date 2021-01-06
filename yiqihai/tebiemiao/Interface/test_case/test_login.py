# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2020-01-26 16:01
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from ddt import ddt, data
import unittest
import os
import logging
# 读取excel
from common.excel_openpyxl import ExcelHandle
# 记录日志  相当重要的那，要不不记录日志
from common import logger
# HTTP请求
from common.requests_handler import RequestsHandler
# 项目路径
from setting.project_path import ProjectPath
# 配置路径及excel文件相关数据
from datas.dir_data import DirData


@ddt
class TestLogin(unittest.TestCase):
    # Excel表格路径及名称
    file_path = ProjectPath.data_excel
    logging.info('Excel表格路径及名称', file_path)
    # url 地址
    url = DirData.test_url
    logging.info('url 地址', url)
    # 读取 excel 数据
    test_data = ExcelHandle().read_all(file_path, DirData.login_sheet)
    logging.info('excel数据', test_data)

    # 测试类方法，每一个测试类之前运行一次
    @classmethod
    def setUpClass(cls):
        # 导入HTTP请求
        cls.req = RequestsHandler()

    @data(*test_data)
    def test_register(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info['method'],  # 请求方式
                            self.url + test_info['url'],  # url地址
                            # 测试数据  获取json的默认是字典格式，所以要进行转换
                            json=eval(test_info['data']))
        print(res)
        # 预期结果，实际结果
        self.assertEqual(test_info['expected'], res['message'])  # 部分断言，判断msg里面的数据
