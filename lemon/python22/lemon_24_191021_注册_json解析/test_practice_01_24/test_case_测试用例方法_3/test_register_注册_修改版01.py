# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : test_01_register_注册.py
# Author       : 大壮
# Create time  : 2019-10-10 20:33
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 导入测试框架
import json
import os
import unittest
from lemon_24_191021_注册_json解析.test_practice_01_24.libs.ddt import ddt, data
# 导入自己写的方法
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.requests_handler_HTTP请求 import RequestsHandler
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.excel_handler_修改版 \
    import ExcelHandler  # TODO ===========================================================
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.config_handler_读取配置文件 \
    import config
from lemon_24_191021_注册_json解析.test_practice_01_24.setting_配置文件_4.constant \
    import p_path


@ddt
class TestRegister(unittest.TestCase):
    # 通过读取配置文件得到 cases.xlsx
    file_name = config.read('excel', 'file_name')
    # 拼接配置文件的路径和名称
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'register_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息
    headers = config.read('http', 'headers')

    # 读取 excel 数据
    xls = ExcelHandler(file_path, sheet_name)
    test_data = xls.read()
    # 写入，写入
    excel_headers = xls.headers()
    # TODO 写入断言结果的表格
    result_index = excel_headers.index('result')
    # 测试类方法，每一个测试类之前运行一次
    @classmethod
    def setUpClass(cls):
        # HTTP请求
        cls.req = RequestsHandler()

    @data(*test_data)
    def test_register(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info['method'],  # 请求方式
                            self.url + test_info['url'],  # url地址
                            # 测试数据  获取json的默认是字典格式，所以要进行转换
                            json=eval(test_info['data']),
                            # 读取 headers 信息 标题头 是字符串，需要转化成字典
                            headers=eval(self.headers))
        print(res)
        # 断言 字符串当中应该是双引号，不能用单引号
        # 把字符串转化为json合适
        try:  # 先断言，把结果写入表格
            self.assertEqual(json.loads(test_info['expected']), res)
            # 写回 Excel
            self.xls.write(test_info['case_id'] + 1,
                           self.result_index + 1,
                           'data')
        except AssertionError as e:
            # 写入断言失败
            # 写回 Excel
            self.xls.write(test_info['case_id'] + 1,
                           self.result_index + 1,
                           'data')
            raise e
