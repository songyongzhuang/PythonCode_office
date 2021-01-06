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
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.requests_handler_HTTP请求 \
    import RequestsHandler
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.excel_handler_操作表格 \
    import ExcelHandler
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.config_handler_读取配置文件 \
    import config
from lemon_24_191021_注册_json解析.test_practice_01_24.setting_配置文件_4.constant \
    import p_path
from lemon_24_191021_注册_json解析.test_practice_01_24.common_内容不会变.logger_handler_日志操作logging \
    import logger
from lemon_24_191021_注册_json解析.test_practice_01_24.middler_ware_搭建桥梁.db_handler \
    import MyDBHandler
from lemon_24_191021_注册_json解析.test_practice_01_24.function_功能_1.helper \
    import mk_phone


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
        # 初始化日志操作
        cls.logger = logger

    def setUp(self):  # 每个用例执行一次
        self.db = MyDBHandler()

    def tearDown(self):  # 每个之后运行，关闭游标和数据连接
        self.db.close()

    @data(*test_data)
    def test_register(self, test_info):
        # 测试数据中有 *exist_phone* 判断数据在数据库中
        if '*exist_phone*' in test_info['data']:
            # 手机号码已存在，查找已存在的手机号
            user = self.db.query('select * from member;')
            test_info['data'] = test_info['data'].replace('*exist_phone*', user['mobile_phone'])

        # 测试中有'#phone#'
        if '#phone#' in test_info['data']:
            # 正常的测试用例, 生成一个手机号码
            while True:  # 判断数据库中有没有随机生成的号码
                phone = mk_phone()
                user = self.db.query('select * from member where mobile_phone=%s;',
                                     args=[phone, ])
                if not user:
                    break
            # 替换手机号码
            test_info['data'] = test_info['data'].replace('#phone#', phone)

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
            # 记录日志信息
            self.logger.info('断言成功')
            # 写回 Excel        # TODO 拼接配置文件的路径和名称
            ExcelHandler.write(self.file_path,
                               # TODO 表格名称
                               self.sheet_name,
                               # TODO 当case_id是‘1’的时候他的行数是‘2’ 需要索引加一
                               test_info['case_id'] + 1,
                               # TODO 写入的表格数
                               self.result_index +1,
                               # TODO 写入的断言结果
                               'data')
        except AssertionError as e:
            # 写入断言失败
            # 写回 Excel
            ExcelHandler.write(self.file_path,
                               self.sheet_name,
                               test_info['case_id'] + 1,
                               self.result_index + 1,
                               'datadatadata')
            # 记录日志信息
            self.logger.error('断言失败')
            raise e
