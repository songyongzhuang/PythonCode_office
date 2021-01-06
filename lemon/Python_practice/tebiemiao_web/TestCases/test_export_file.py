# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : test_export_file.py
# Author       : 大壮
# Create time  : 2020-03-26 14:51
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pytest
# 记录日志/打印日志到控制台/创建日志文件
from tebiemiao_web.Common import logger
# 调用公共数据
from tebiemiao_web.TestDatas.common_datas import CommonData as CD
# 调用 元素操作
from tebiemiao_web.PageObjects.login_page import LoginPage
#
from tebiemiao_web.PageObjects.export_file_page import ExportFilePage

# 前置后置  默认测试用例级别
@pytest.fixture
def init_driver(init):  # 继承同级目录 conf_test 里面的init
    # 登录 - 调用登录首页操作 - 输入用户名/密码
    LoginPage(init).login(CD.user, CD.password)
    # 初始化 LoginPage 方便调用
    slp = ExportFilePage(init)
    # yield 返回值, 修改成字典格式
    yield {'driver': init, 'slp': slp}
    # 后置不用写，直接使用继承 init 的后置


@pytest.mark.usefixtures('init_driver')
class TestSendLetter(object):
    """
    导出excel表格
    """

    def test_hotel_list_excel(self, init_driver):
        """
        酒店列表 - 在售商品导出excel
        :param init_driver:
        :return:
        """
        init_driver['slp'].hotel_list_excel()

    def test_sales_detail_excel(self, init_driver):
        """
        订单管理 - 销售明细导出excel
        :param init_driver:
        :return:
        """
        init_driver['slp'].sales_detail_excel()

    def test_order_detail_excel(self, init_driver):
        """
        订单管理 - 订单明细导出excel
        :param init_driver:
        :return:
        """
        init_driver['slp'].order_detail_excel()
