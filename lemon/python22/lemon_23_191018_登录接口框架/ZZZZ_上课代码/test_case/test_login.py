#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/9 20:46
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os
import unittest

from lemon_23_191018_登录接口框架.ZZZZ_上课代码.libs.ddt import ddt, data
from lemon_23_191018_登录接口框架.ZZZZ_上课代码.common.config_handler import config
from lemon_23_191018_登录接口框架.ZZZZ_上课代码.common.excel_handler import ExcelHandler
from lemon_23_191018_登录接口框架.ZZZZ_上课代码.common.requests_handler import RequestsHandler
from lemon_23_191018_登录接口框架.ZZZZ_上课代码.setting.constant import p_path


@ddt
class TestLogin(unittest.TestCase):
    # 读取配置文件
    file_name = config.read('excel', 'file_name')
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'login_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息
    headers = config.read('http', 'headers')

    test_data = ExcelHandler(file_path).read(sheet_name)

    @classmethod
    def setUpClass(cls):
        cls.req = RequestsHandler()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_login(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info[3],
                            self.url + test_info[4],
                            json=eval(test_info[5]),
                            headers=eval(self.headers))
        print(res)
        self.assertEqual(test_info[7], res['msg'])
