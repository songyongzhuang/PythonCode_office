
# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : test_02_login_登录.py
# Author       : 大壮
# Create time  : 2019-10-10 20:33
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 导入测试框架
# 导入测试框架
import json
import os
import unittest
from libs.ddt import ddt, data
# 导入自己写的方法
from common.requests_handler_HTTPqingqiu import RequestsHandler  # HTTP请求
from common.excel_handler_caozuoExcel import ExcelHandler  # Excel 表格
from common.config_handler_peizhiwenjian import config  # 读取配置文件
from setting.constant import p_path  # 各种文件路径
from common.logger_handler_rizhicaozuo import logger  # 日志处理
from middler_ware.db_handler import MyDBHandler  # 数据库搭桥
from function.helper import mk_phone  # 随机数手机号码


@ddt  # ddt根据测试用例自动创建标题
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
        # 导入HTTP请求
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
        # 预期结果，实际结果
        self.assertEqual(test_info['expected'], res['msg'])  # 部分断言，判断msg里面的数据
