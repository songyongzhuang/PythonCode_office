
# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : test_03_recharge_充值.py
# Author       : 大壮
# Create time  : 2019-10-24 21:18
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import json
import os
import unittest
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.libs.ddt import ddt, data
# 导入自己写的方法
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.requests_handler_HTTPqingqiu \
    import RequestsHandler  # HTTP请求
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.excel_handler_caozuoExcel \
    import ExcelHandler  # Excel 表格
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.config_handler_peizhiwenjian \
    import config  # 读取配置文件
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.setting.constant \
    import p_path  # 各种文件路径
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.logger_handler_rizhicaozuo \
    import logger  # 日志处理
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.middler_ware.db_handler \
    import MyDBHandler  # 数据库搭桥
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.function.helper \
    import mk_phone, login  # 随机数手机号码


@ddt
class TestRecharge(unittest.TestCase):
    # 通过读取配置文件得到 cases.xlsx
    file_name = config.read('excel', 'file_name')
    # 拼接配置文件的路径和名称
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    # Excel 表格名称
    sheet_name = config.read('excel', 'tixian_sheet')
    # url 地址
    url = config.read('http', 'base_url')
    # 读取 headers 信息 获取 请求头
    # TODO  cls.headers['Authorization'] = 'Bearer ' + cls.user_info['token']
    #  TypeError: 'str' object does not support item assignment
    headers = eval(config.read('http', 'headers'))
    # 读取 excel 数据
    test_data = ExcelHandler(file_path).read(sheet_name)

    # 写入，写入
    excel_headers = ExcelHandler(file_path).headers(sheet_name)
    # TODO 写入断言结果的表格
    result_index = excel_headers.index('result')

    # 测试类方法，每一个测试类之前运行一次
    @classmethod
    def setUpClass(cls):
        # HTTP请求
        cls.req = RequestsHandler()
        # 登录 提前准备好的测试账号来登录
        # 1、先登录获取token 用户id member_id
        cls.user_info = login()
        # 2、组装、Authorization 请求头是v2必传需要拼接是由：Bearer + '空格' + token
        cls.headers['Authorization'] = 'Bearer ' + cls.user_info['token']

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每个用例执行一次
        self.db = MyDBHandler()

    def tearDown(self):  # 每个之后运行，关闭游标和数据连接
        self.db.close()

    @data(*test_data)
    def test_recharge(self, test_info):  # test_info里面是测试文档里的数据

        if '#member_id#' in test_info['data']:  # TypeError: 参数二必须是 str 类型，不能是 int 类型
            test_info['data'] = test_info['data'].replace('#member_id#', str(self.user_info['member_id']))

        if '*wrong_member_id*' in test_info['data']:  # 只要用户id不是他自己就可以了，后面加一
            test_info['data'] = test_info['data'].replace('*wrong_member_id*', str(self.user_info['member_id'] + 1))

        # 3、发送请求  之前需要把表格里的用户member_id进行替换，表格里是“member”占位
        # 5、查询数据库，对比余额，
        # 提现之前金额
        user_info = self.db.query('select * from member where id = %s;', args=[self.user_info['member_id']])
        amount = user_info['leave_amount']  # 查询数据库获取用户金额

        res = self.req.json(test_info['method'],  # 请求方式
                            self.url + test_info['url'],  # url地址
                            # 测试数据  获取json的默认是字典格式，所以要进行转换
                            json=eval(test_info['data']),
                            # 读取 headers 信息 标题头 是字符串，需要转化成字典
                            headers=self.headers)

        # 4、替换member_id
        self.assertEqual(test_info['expected'], res['code'])

        # 4.1、再次查询数据库，对比两个数据库查到的结果相减 == 投资金额
        # 投资之后金额
        user_info_after = self.db.query('select * from member where id = %s;', args=[self.user_info['member_id']])
        amount_after = user_info_after['leave_amount']  # 查询数据库获取用户金额

        # 5、查询数据库，对比余额，
        if res['code'] == 0:
            print(amount, amount_after)
            self.assertEqual(float(amount - amount_after), json.loads(test_info['data'])['amount'])
