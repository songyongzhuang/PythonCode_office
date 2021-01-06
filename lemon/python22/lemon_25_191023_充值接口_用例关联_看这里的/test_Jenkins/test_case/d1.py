# --*-- coding ：utf-8 --*--
# Project      ：test_Jenkins
# Current file ：d1.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/05 17:39
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# 导入测试框架
import json
import os
import unittest
import suds
from libs.ddt import ddt, data
# 导入自己写的方法
from common.requests_handler_HTTPqingqiu import RequestsHandler  # HTTP请求
from common.excel_handler_caozuoExcel import ExcelHandler  # Excel 表格
from common.config_handler_peizhiwenjian import config  # 读取配置文件
from setting.constant import p_path  # 各种文件路径
from common.logger_handler_rizhicaozuo import logger  # 日志处理
from middler_ware.db_handler import MyDBHandler  # 数据库搭桥
from function.helper import mk_phone, login, replace_label  # 随机数手机号码

# suds的client获取webService
from suds import client


@ddt
class TestInvest(unittest.TestCase):
    # 通过读取配置文件得到 cases.xlsx
    file_name = config.read('excel', 'file_name')
    # 拼接配置文件的路径和名称
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'sendMCode_sheet')
    # url 地址
    url = config.read('http', 'combat_url')
    # 读取 excel 数据
    test_data = ExcelHandler(file_path).read(sheet_name)

    @classmethod
    def setUpClass(cls):
        # HTTP请求
        cls.req = RequestsHandler()
        # 初始化日志操作
        cls.logger = logger

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*test_data)
    def test_invest(self, test_info):
        # 访问的url地址
        user_url = self.url
        client = suds.client.Client(user_url)
        data = eval(test_info['data'])
        res = client.service.sendMCode(data)

        self.assertEqual(test_info['expected'], res['retInfo'])
