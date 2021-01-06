import time
import unittest
from selenium import webdriver
from framework.publicmethod import login
from pageobject.login_page_loc import LoginPage
# 定义的日志
from framework import logger


class TestLogin(unittest.TestCase):
    """
    登录用例
    """

    # setUp 每一个测试类之前只运行一次
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        # 打开分享油客
        self.driver.get(login.CD.login_url)
        self.lp = LoginPage(self.driver)

    # tearDown 每一个测试类之后运行一次
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_login(self):
        # 调用登录页面的，登陆行为，输入账号密码
        self.lp.login('admin', 'admin')
        # TODO 明天该
        # 断言 url地址，应当为：https://oms.test.tebiemiao.cn/#/goods/index
        time.sleep(2)
        self.assertEqual(self.driver.current_url, login.CD.home_url)
