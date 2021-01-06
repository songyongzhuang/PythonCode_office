# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2020-03-22 15:48
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import unittest
import ddt
import time
from selenium import webdriver
from tebiemiao_web.PageObjects.login_page import LoginPage
from tebiemiao_web.PageObjects.home_page import HomePage
# 公共数据层
from tebiemiao_web.TestDatas.common_datas import CommonData as CD
from tebiemiao_web.TestDatas import usecase_datas as UC


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CD.test_login_url)
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        """
        调用登录页面的，登录行为 - 正常登录
        :return:
        """
        # 调用登录操作输入账号密码
        self.lp.login(UC.success_data['user'], UC.success_data['password'])
        # 断言 - 首页右上角中定位表达式存在
        time.sleep(2)
        self.assertTrue(HomePage(self.driver).check_user_exist())
        # 断言2 - 登录成功后 url 比对
        self.assertEqual(self.driver.current_url, UC.success_data['check_url'])
'''
    @ddt.data(*UC.wrong_data_tooltip)
    def test_login_failed_tooltip(self, case):
        """
        测试 登录失败 提示框 (导致弹框出现的错误登录)
        :return:
        """
        self.lp.login(case['user'], case['password'])
        # 断言 - 登录页面 - 错误弹框提示信息 ：账号密码不正确
        self.assertEqual(case['check'], self.lp.get_error_user())

    @ddt.data(*UC.wrong_data_password)
    def test_login_failed_by_noPassword(self, case):
        """
        调用登录页面，没有密码 (导致 密码下方提示信息 的错误登录)
        :return:
        """
        self.lp.login(case['user'], case['password'])
        # 断言 - 登录页面 - 密码下方提示信息 ：密码不能小于6位
        self.assertEqual(case['check'], self.lp.get_error_password())
'''
