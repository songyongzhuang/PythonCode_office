# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : conftest.py
# Author       : 大壮
# Create time  : 2020-12-21 13:14
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 调用pytest
import pytest
# 调用 浏览器
from selenium import webdriver
# 调用公共数据
from test_datas.common_datas import CommonData as CD
# 调用 元素操作
from page_objects.login_page import LoginPage


# 装饰器 代表init是 前置&后置。
@pytest.fixture
def init():
    # 前置
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 最大化浏览器
    driver.maximize_window()
    # 打开url地址
    driver.get(CD.base_url)
    # 初始化 LoginPage 方便调用
    lp = LoginPage(driver)
    # 分隔前置和后置  用例调用的时候 fixture 的函数名称作为用例的参数，接收他的返回值:driver
    yield driver
    # 后置
    # 关闭浏览器
    driver.quit()
