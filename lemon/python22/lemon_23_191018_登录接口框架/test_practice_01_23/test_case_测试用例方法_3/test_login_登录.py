# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : test_01_register_注册.py
# Author       : 大壮
# Create time  : 2019-10-10 20:33
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 导入测试框架

import os
import unittest
from lemon_23_191018_登录接口框架.test_practice_01_23.libs.ddt import ddt, data
# 导入自己写的方法
from lemon_23_191018_登录接口框架.test_practice_01_23.common_内容不会变.requests_handler_HTTP请求 \
    import RequestsHandler
from lemon_23_191018_登录接口框架.test_practice_01_23.common_内容不会变.excel_handler_操作表格 \
    import ExcelHandler
from lemon_23_191018_登录接口框架.test_practice_01_23.common_内容不会变.config_handler_读取配置文件 \
    import config
from lemon_23_191018_登录接口框架.test_practice_01_23.setting_配置文件_4.constant \
    import p_path


@ddt
class TestLogin(unittest.TestCase):
    # 通过读取配置文件得到 cases.xlsx
    file_name = config.read('excel', 'file_name')
    # 拼接配置文件的路径和名称
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'login_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息
    headers = config.read('http', 'headers')
    # 读取 excel 数据
    test_data = ExcelHandler(file_path).read(sheet_name)

    # 测试类方法，每一个测试类之前运行一次
    @classmethod
    def setUpClass(cls):
        # HTTP请求
        cls.req = RequestsHandler()

    @data(*test_data)
    def test_login(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info[3],
                            self.url + test_info[4],
                            json=eval(test_info[5]),
                            headers=eval(self.headers))
        print(res)
        # 断言
        self.assertEqual(test_info[7], res['msg'])

