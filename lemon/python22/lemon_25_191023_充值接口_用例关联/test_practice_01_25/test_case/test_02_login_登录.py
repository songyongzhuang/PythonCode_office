
# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : test_02_login_登录.py
# Author       : 大壮
# Create time  : 2019-10-10 20:33
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 导入测试框架
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
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.function.helper \
    import mk_phone, login  # 随机数手机号码
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.middler_ware.db_handler \
    import MyDBHandler


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

    def setUp(self):  # 每个用例执行一次
        self.db = MyDBHandler()

    def tearDown(self):  # 每个之后运行，关闭游标和数据连接
        self.db.close()

    @data(*test_data)
    def test_register(self, test_info):

        # 测试数据中有 *exist_phone* 判断数据在数据库中
        if '#phone#' in test_info['data']:
            # 手机号码已存在，查找已存在的手机号
            user = self.db.query('select * from member;')
            # 替换手机号码
            test_info['data'] = test_info['data'].replace('#phone#', user['mobile_phone'])

        # 测试中有'*phone*'
        if '*phone*' in test_info['data']:
            # 正常的测试用例, 生成一个手机号码
            while True:  # 判断数据库中有没有随机生成的号码
                phone = mk_phone()
                user = self.db.query('select * from member where mobile_phone=%s;', args=[phone, ])
                if not user:
                    break
            # 替换手机号码
            test_info['data'] = test_info['data'].replace('*phone*', phone)

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
