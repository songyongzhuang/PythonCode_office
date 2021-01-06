# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : export_file_loc.py
# Author       : 大壮
# Create time  : 2020-03-26 15:36
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 定位
from selenium.webdriver.common.by import By


class ExportFileLoc(object):
    # 导出excel表格 - 元素定位

    # ------------ 酒店列表 - 在售商品导出excel ------------
    # 定位右侧一级菜单 - 酒店管理
    hotel_management_loc = (By.XPATH, '//span[text()="酒店管理"]')
    # 定位右侧二级菜单 - 酒店查询 '//li[@class="el-menu-item is-active"]//span'
    hotel_query_loc = (By.XPATH, '//span[@style="padding-left: 10px;" and text()="酒店查询"]')
    # 酒店列表 - 在售商品导出excel
    hotel_list_excel_loc = (By.XPATH, '//span[contains(text(),"在售商品导出excel")]')

    # ------------ 酒店列表 - 商品列表 - 在售商品导出excel ------------
    # 酒店列表 - 查看
    '//div[contains(text(),"test大大夶𡘙酒店")]/ancestor::tr//span[contains(text(),"查看")]'

    # ------------ 订单管理 - 销售明细导出excel ------------
    # 定位右侧一级菜单 - 订单管理
    order_management_loc = (By.XPATH, '//span[text()="订单管理"]')
    # 定位右侧二级菜单 - 订单列表
    order_list_loc = (By.XPATH, '//li//span[text()="订单列表"]')
    # 订单列表 - 搜索按钮
    search_loc = (By.XPATH, '//span[contains(text(),"搜索")]')
    # 销售明细导出excel
    sales_detail_loc = (By.XPATH, '//span[contains(text(),"销售明细导出excel")]')
    # 提示导出弹框 - 确定
    sales_detail_confirm_loc = (By.XPATH, '//div[@class="el-message-box"]//span[contains(text(),"确定")]')

    # ------------ 订单管理 - 订单明细导出excel ------------
    # 订单明细导出excel
    order_detail_loc = (By.XPATH, '//span[contains(text(),"订单明细导出excel")]')
    # 提示导出弹框 - 确定
    order_detail_confirm_loc = (By.XPATH, '//div[@class="el-message-box"]//span[contains(text(),"确定")]')
