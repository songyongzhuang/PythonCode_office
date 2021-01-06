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
    import mk_phone  # 随机数手机号码


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
    # 读取 headers 信息 请求头
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
        # 操作数据库
        self.db = MyDBHandler()

    def tearDown(self):  # 每个用例执行之后运行，
        # 关闭游标和数据连接
        self.db.close()

    @data(*test_data)
    def test_register(self, test_info):  # test_info里面是测试文档里的数据
        # 测试数据中有 *exist_phone* 判断数据在数据库中
        if '*exist_phone*' in test_info['data']:  # 判断数据是否存在表格data里面
            # 去数据库中查找获取一条数据，用来测试手机号码已存在
            user = self.db.query('select * from member;')
            # 把在数据库中查询到的手机号，替换掉 '*exist_phone*'
            test_info['data'] = test_info['data'].replace('*exist_phone*', user['mobile_phone'])

        # 测试中有'#phone#'
        if '#phone#' in test_info['data']:
            # 正常的测试用例, 生成一个手机号码
            while True:  # 判断数据库中有没有随机生成的号码
                phone = mk_phone()  # 获取随机生成的手机号码
                # 查询数据库中是否有随机生成的手机号
                user = self.db.query('select * from member where mobile_phone=%s;',
                                     args=[phone, ])
                # 数据库中没有手机号码就跳出循环
                if not user:
                    break
            # 替换手机号码
            test_info['data'] = test_info['data'].replace('#phone#', phone)

        # 调用 requests 模块HTTP请求访问接口
        res = self.req.json(test_info['method'],  # 请求方式 POST
                            self.url + test_info['url'],  # url地址
                            # 测试数据  获取json的默认是字典格式，所以要进行转换
                            json=eval(test_info['data']),
                            # 读取 headers 信息 标题头 是字符串，需要转化成字典
                            headers=eval(self.headers))
        print(res)

        # 断言 判断
        try:  # 先断言判断是否通过，再把结果写入表格
            self.assertEqual(test_info['expected'], res['code'])  # 只断言code
            # self.assertEqual(json.loads(['expected'])['msg'], res['msg'])  # 模拟断言 msg

            # 记录日志信息
            self.logger.info('断言成功')
            # 写回 Excel        # TODO 拼接配置文件的路径和名称
            ExcelHandler.write(self.file_path,
                               # TODO 表格名称
                               self.sheet_name,
                               # TODO 当case_id是‘1’的时候他的行数是‘2’ 需要索引加一
                               test_info['case_id'] + 1,
                               # TODO 写入的表格数
                               self.result_index + 1,
                               # TODO 写入的断言结果
                               '断言成功')
        except AssertionError as e:
            # 写入断言失败
            # 写回 Excel
            ExcelHandler.write(self.file_path,
                               self.sheet_name,
                               test_info['case_id'] + 1,
                               self.result_index + 1,
                               '断言失败')
            # 记录日志信息
            self.logger.error('断言失败')
            raise e
