# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : test_login.py
# Author       : 大壮
# Create time  : 2019-12-01 10:13
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

import unittest
import time
import ddt
from selenium import webdriver

from lemon_10_191208_PO_03.PageObjects.login_page import LoginPage
from lemon_10_191208_PO_03.PageObjects.home_page import HomePage

from lemon_10_191208_PO_03.TestDatas.Common_Datas import CD
from lemon_10_191208_PO_03.TestDatas.Login_Datas import LD


@ddt.ddt
class TestLogin(unittest.TestCase):
    """
    登录用例
    """''

    # setUp 每一个测试类之前只运行一次
    def setUp(self) -> None:  # -> None 表示没有返回
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        self.driver.get(CD.login_url)
        self.lp = LoginPage(self.driver)

    # tearDown 每一个测试类之后运行一次
    def tearDown(self) -> None:
        # 关闭浏览器
        self.driver.quit()

    # 正常场景 成功用例 登录成功
    def test_login_success(self):
        # 调用登陆页面的。请输入密码。
        self.lp.login(LD.success_data['user'], LD.success_data['passwd'])
        # 断言 - 首页当中，应该存在 退出元素
        self.assertEqual(LD.success_data['check_quit_exist'], HomePage(self.driver).check_user_exist())
        # 断言2 = url地址，应当为：http://120.78.128.25:8765/Index/index
        time.sleep(1)
        self.assertEqual(self.driver.current_url, LD.success_data['check_url'])

    @ddt.data(*LD.wrong_datas)  # 需要数据列表或者字典
    def test_login_failed_by_wrongData(self, case):
        # 调用登录页面的，登陆行为  请输入密码
        self.lp.login(case['user'], case['passwd'])
        # 断言- 登录页面 - 应当提示信息： 请输入密码
        self.assertEqual(case['check'], self.lp.get_error_msg())

    # 帐号或密码错误!提示框
    def test_login_failed_by_wrong_passwd(self):
        # 调用登录页面的，登陆行为
        self.lp.login('18684720553', 'python11')
        # 断言- 登录页面 - 应当提示信息： 帐号或密码错误!
        self.assertEqual('帐号或密码错误!', self.lp.get_error_msg_from_dialog())
