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
from ddt import ddt, data
# 导入自己写的方法

from lemon_19_191009_接口框架设计综合使用_国庆作业总结.test_practice_01.common_内容不会变.excel_handler_操作表格 \
    import ExcelHandler
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.test_practice_01.common_内容不会变.config_handler_读取配置文件 \
    import config
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.test_practice_01.common_内容不会变.logger_handler_日志操作logging \
    import logger
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.test_practice_01.setting_配置文件_4.constant \
    import p_path
from lemon_19_191009_接口框架设计综合使用_国庆作业总结.test_practice_01.function_功能_1.calc \
    import add

# 使用Excel读取数据 ,
# 设置一个默认值配置文件名，使用配置文件设置默认
# 配置文件 文件夹+配置文件里面的 cases.xlsx

# 通过读取配置文件得到 cases.xlsx
file_name = config.read('excel', 'file_name')
file_path = os.path.join(p_path.DATA_PATH, file_name)


# 获取 sheetname
sheet_name = config.read('excel', 'add_sheet')

# 读取 excel 数据
test_data = ExcelHandler(file_path).read(sheet_name)


@ddt
class TestAbb(unittest.TestCase):
    """ 加 """

    @data(*test_data)
    def test_add(self, test_info):
        a = test_info[2]
        actual = add(*eval(test_info[1]))
        # test_info[2] (字符串，数字)
        # actual, (数字，None)
        try:
            self.assertEqual(eval(str(test_info[2])), actual)
            logger.info('测试通过')
        except AssertionError as a:
            # logging.info
            logger.error('断言失败')
            # 断言失败要手动抛出异常
            raise a
        self.assertEqual(str(test_info[2]),  str(actual))
        # 断言失败 抛出异常：AssertionError
