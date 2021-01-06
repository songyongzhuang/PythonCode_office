# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2019-12-01 10:13
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import unittest
from selenium import webdriver

from lemon_08_191129_自动化测试方案_PO模式.PageLocation.login_page import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")

    def test_login_success(self):
        self.login = LoginPage(self.driver)
        # 调用登陆页面的。请输入密码。
        self.login.login("18684720553", "")
        self.assertEqual('请输入密码', self.login.get_error_msg(LoginPage.mistake_hint))

    def test_login_success_02(self):
        # 调用登陆页面的。请输入手机号。
        s = LoginPage(self.driver)
        s.login("", "python")
        a = s.get_error_msg(LoginPage.mistake_hint)
        self.assertEqual('请输入手机号', a)

    def test_login_success_03(self):
        # 调用登陆页面的。帐号或密码错误。
        s = LoginPage(self.driver)
        s.login("18684720553", "python123456")
        a = s.get_error_msg(LoginPage.mistake_hint_account)
        self.assertEqual('帐号或密码错误!', a)
