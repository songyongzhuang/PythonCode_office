#!/usr/bin/python3
"""
@File    : test_invest.py
@Time    : 2019/12/2 21:30
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
"""
前置(准备条件)：
1、登陆网站 
2、有可投资的标(没有就会去创建标)
3、可投金额，大于你投资的金额
4、用户得有足够的余额去投资(功能：一次充它一个亿)

代码：接口(创建标、审核标)、接口(每次充5000，或者，先查询有没钱，没有就充XXXX)

步骤+断言(web页面，期望结果除外)：
1、(前置)登陆页面登陆;
2、首页选标；
3、标页面获取用户余额；
4、标页面获取 标的余额；
5、标页面：投标动作；
6、个人页面：获取用户余额
7、回退到标页面：再次获取标的余额
"""

import unittest
from selenium import webdriver

from lemon_09_191202_PO_02.PageObjects.login_page import LoginPage

from lemon_09_191202_PO_02.TestDatas import Common_Datas as CD


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 1、(前置)登陆页面登陆;
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        self.driver.get(CD.login_url)
        LoginPage(self.driver).login(CD.user, CD.passwd)

    def tearDown(self) -> None:
        self.driver.quit()

    # 正常场景 - 投资成功
    def test_invest_success(self):
        # 2、首页选标；
        # 3、标页面获取用户余额；
        # 4、标页面获取 标的余额；
        # 5、标页面：投标动作；
        # 6、个人页面：获取用户余额
        # 7、回退到标页面：再次获取标的余额
        pass
