# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_06_invest_投资.py
# Author       : 大壮
# Create time  : 2019-10-26 16:19
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
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
from function.helper import mk_phone, login, replace_label  # 随机数手机号码


@ddt
class TestInvest(unittest.TestCase):
    # 读取配置文件
    file_name = config.read('excel', 'file_name')
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'invest_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息 获取 请求头

    headers = eval(config.read('http', 'headers'))
    # 读取 excel 数据
    test_data = ExcelHandler(file_path).read(sheet_name)

    # 写入，写入
    excel_headers = ExcelHandler(file_path).headers(sheet_name)
    # TODO 写入断言结果的表格
    result_index = excel_headers.index('result')

    @classmethod
    def setUpClass(cls):
        cls.req = RequestsHandler()
        # 登录， 测试账号来登录
        cls.user_info = login()
        cls.headers['Authorization'] = 'Bearer ' + cls.user_info['token']

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每个测试用例执行前运行
        self.db = MyDBHandler()

    def tearDown(self):  # 每个测试用例之后运行
        self.db.close()

    @data(*test_data)
    def test_invest(self, test_info):
        # 1 登录，拿到 token_id, 作为接下来的接口请求头信息
        # 2，创建标
        # 3， 审核标
        # 4， 投资
        # 余额是否相等
        test_info['data'] = replace_label(test_info['data'])
        print(test_info['data'])

        user_info = self.db.query('SELECT * FROM member WHERE id=%s;', args=[self.user_info['member_id']])
        before_money = user_info['leave_amount']

        res = self.req.json(test_info['method'],
                            self.url + test_info['url'],
                            json=json.loads((test_info['data'])),
                            headers=self.headers)
        # 替换 member_id
        print(res)
        self.assertEqual(test_info['expected'], res['code'])
        if res['code'] == 0 and test_info['url'] == '/member/invest':
            user_info_after = self.db.query('SELECT * FROM member WHERE id=%s;', args=[self.user_info['member_id']])
            after_money = user_info_after['leave_amount']
            self.assertEqual(before_money - json.loads(test_info['data'])['amount'],
                             after_money)
        # 如果是添加投资用例，我才能把 res.token. 保存配置文件。
