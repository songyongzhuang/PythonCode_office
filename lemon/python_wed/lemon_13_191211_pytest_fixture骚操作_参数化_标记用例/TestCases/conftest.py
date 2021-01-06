# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : conftests.py
# Author       : 大壮
# Create time  : 2019-12-15 15:12
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import pytest
from selenium import webdriver
from lemon_13_191211_pytest_fixture骚操作_参数化_标记用例.TestDatas \
    import Common_Datas as CD
from lemon_13_191211_pytest_fixture骚操作_参数化_标记用例.PageObjects.login_page \
    import LoginPage


@pytest.fixture()
def init():
    # 前置
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 最大化浏览器
    driver.maximize_window()
    # 打开URL地址
    driver.get(CD.login_url)
    # 初始 LoginPage 方便调用
    lp = LoginPage(driver)
    # 分隔前值和后置
    yield driver
    # 后置
    # 关闭浏览器
    driver.quit()


# 访问网站并且登录成功
# 继承 init_driver 前置后置
# 继承 ：可以继承高级别，但是不能继承底级别
@pytest.fixture
def login_web(init):
    # 初始化 LoginPage 登录用户名和密码
    LoginPage(init).login(CD.user, CD.passwd)
    yield init  # 返回 driver

# autouse=True 打开，默认是关闭，
@pytest.fixture(scope='session', autouse=True)
def session_gl():
    print('===== 测试会话开始 =====')
    yield True
    print('===== 测试会话结束 =====')


# 模块级别 .py
@pytest.fixture(scope='module')
def module_gl():
    print('===== 模块级别：测试用例开始 =====')
    yield True
    print('===== 模块级别：测试用例结束 =====')

"""
init的前置 --class
login_web的前置
=== 执行用例 ===
login_web的后置
init的后置

@pytest.fixture()
# function 默认是测试用例(函数)级别
# 测试类(class)级别
# module 模块级别(.py)
# package 包
# session 测试用例会话
def init_driver():
    # 前置
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 最大化浏览器
    driver.maximize_window()
    # 打开URL地址
    driver.get(CD.login_url)
    # 初始 LoginPage 方便调用
    lp = LoginPage(driver)
    # 分隔前值和后置
    yield {'driver': driver, 'lp': lp}
    # 后置
    # 关闭浏览器
    driver.quit()

# 访问网站并且登录成功  TODO  没改之前
def login_web():
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 最大化浏览器
    driver.maximize_window()
    # 打开URL地址
    driver.get(CD.login_url)
    # 初始化 LoginPage 登录用户名和密码
    LoginPage(driver).login(CD.user, CD.passwd)
    yield driver  # 返回 driver
    # 关闭浏览器
    driver.quit()
"""
