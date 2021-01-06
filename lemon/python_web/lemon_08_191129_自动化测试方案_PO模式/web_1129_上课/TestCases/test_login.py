#!/usr/bin/python3
"""
@File    : test_login.py
@Time    : 2019/11/29 21:53
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
import unittest
from selenium import webdriver

from lemon_08_191129_自动化测试方案_PO模式.web_1129_上课.PageObjects.login_page \
    import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")

    def test_login_success(self):
        # 调用登陆页面的。登陆行为。
        LoginPage(self.driver).login("18684720553", "python")
        # 断言
