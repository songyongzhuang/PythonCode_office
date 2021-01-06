# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2020-01-26 16:01
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from ddt import ddt, data
import pytest
import os
import logging
# 读取excel
from common.excel_openpyxl import ExcelHandle
# 记录日志  相当重要的那，要不不记录日志
from common import logger
# HTTP请求
from common.requests_handler import RequestsHandler
# 项目路径
from setting.project_path import ProjectPath
# 配置路径及excel文件相关数据
from datas.dir_data import DirData


# 测试类方法，每一个测试类之前运行一次
# 前置后置  默认测试用例级别
@pytest.fixture
def init():
    # 导入HTTP请求
    req = RequestsHandler()
    # yield 返回值，
    yield req


@pytest.mark.usefixtures('init')
class TestLogin(object):
    # Excel表格路径及名称
    file_path = ProjectPath.data_excel
    logging.info('Excel表格路径及名称', file_path)
    # url 地址
    url = DirData.test_url
    logging.info('url 地址', url)
    # 读取 excel 数据
    test_data = ExcelHandle().read_all(file_path, DirData.login_sheet)
    logging.info('excel数据', test_data)

    @pytest.mark.parametrize('case', test_data)
    def test_register(self, case, init):
        # 调用 requests 模块访问接口
        res = init.json(case['method'],  # 请求方式
                        self.url + case['url'],  # url地址
                        # 测试数据  获取json的默认是字典格式，所以要进行转换
                        json=eval(case['data']))
        print(res)
        # 预期结果，实际结果
        assert (case['expected'] == res['message'])  # 部分断言，判断msg里面的数据
