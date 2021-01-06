# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : export_file_page.py
# Author       : 大壮
# Create time  : 2020-03-26 15:26
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
# 调用 基础定位(各种定位元素的方法)
from tebiemiao_web.Common.base_page import BasePage
# 导出表格定位
from tebiemiao_web.PageLocators.export_file_loc import ExportFileLoc as EFL


# 继承 BasePage 可以直接使用它的所有方法，
class ExportFilePage(BasePage):
    """
    下载平台后台excel表格
    """

    def hotel_list_excel(self):
        """
        下载 酒店管理列表 - excel表格
        :return:
        """
        # 滚动到 - 酒店管理 并点击
        self.guendongtiaocaozuo_jianyiban(EFL.hotel_management_loc, '滚动右侧一级菜单酒店管理')
        # 点击右侧二级菜单 - 酒店查询
        self.click_element(EFL.hotel_query_loc, '点击右侧二级菜单_酒店查询')
        # 点击导出商品excel按钮
        self.click_element(EFL.hotel_list_excel_loc, '点击_在售商品导出excel')
        # 导出表格 - 路径以及表格名称
        time.sleep(4)
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        self.export_file(f'E:\WebWebpageTest\酒店商品销售明细表_{now}.xls')

    def sales_detail_excel(self):
        """
        订单列表 - 销售明细导出excel
        :return:
        """
        # 滚动到 - 定位右侧一级菜单 - 订单管理 点击
        self.guendongtiaocaozuo_jianyiban(EFL.order_management_loc, '滚动右侧一级菜单酒店管理')
        # 点击右侧二级菜单 - 订单列表
        self.click_element(EFL.order_list_loc, '点击右侧二级菜单_酒店查询')
        # 点击搜索按钮 (他有时候提示无数据 - 加一步搜索操作)
        self.click_element(EFL.search_loc, '点击_搜索按钮')
        time.sleep(2)
        # 点击导出商品excel按钮
        self.click_element(EFL.sales_detail_loc, '点击_销售明细导出excel')
        # 点击导出确定按钮
        self.click_element(EFL.sales_detail_confirm_loc, '点击_导出弹框的确定按钮')
        time.sleep(8)
        # 导出表格 - 路径以及表格名称
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        self.export_file(f'E:\WebWebpageTest\酒店商品销售明细表({now}).xls')

    def order_detail_excel(self):
        """
        订单管理 - 订单明细导出excel
        :return:
        """
        # 滚动到 - 定位右侧一级菜单 - 订单管理 点击
        self.guendongtiaocaozuo_jianyiban(EFL.order_management_loc, '滚动右侧一级菜单酒店管理')
        # 点击右侧二级菜单 - 订单列表
        self.click_element(EFL.order_list_loc, '点击右侧二级菜单_酒店查询')
        time.sleep(2)
        # 点击导出商品excel按钮
        self.click_element(EFL.order_detail_loc, '点击_订单明细导出excel')
        # 点击导出确定按钮
        self.click_element(EFL.sales_detail_confirm_loc, '点击_导出弹框的确定按钮')
        time.sleep(11)
        # 导出表格 - 路径以及表格名称        now = time.strftime('%Y-%m-%d %H-%M-%S')
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        self.export_file(f'E:\WebWebpageTest\酒店成交订单明细表({now}).xls')
