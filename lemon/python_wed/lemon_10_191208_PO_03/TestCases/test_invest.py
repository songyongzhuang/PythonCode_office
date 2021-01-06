# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：test_invest.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/04 9:18
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
"""
前置（准备条件）
1、登录网站
2、有可投资的标（没有就去创建标）
3、可投金额，大于你投资的金额
4、用户得有足够的金额去投资（功能：一次充值多点钱）

代码：接口（创建标、审核标）、接口（每次冲5000，或者，先查询有没有钱，没有就充值XXX)

步骤+断言（wed页面，期望结果除外）：
1、（前置）登录页面的登陆；
2、首页选标
3、表页面获取用户余额
4、标页面获取标的余额
5、标页面：投标动作
6、个人页面：获取用户余额
7、回退到标页面，再次获余额
"""''

import unittest
import time
import ddt
from selenium import webdriver

from lemon_10_191208_PO_03.PageObjects.login_page import LoginPage
from lemon_10_191208_PO_03.PageObjects.home_page import HomePage
# 调用的投标模块
from lemon_10_191208_PO_03.PageObjects.bid_page import BidPage
from lemon_10_191208_PO_03.TestDatas.Common_Datas import CD
from lemon_10_191208_PO_03.TestDatas.Login_Datas import LD


class TestInvest(unittest.TestCase):
    """
    投资用例
    """''

    def setUp(self) -> None:
        # 1、（前置）登录页面的登陆；
        self.driver = webdriver.Chrome()
        # 最大化浏览器
        self.driver.maximize_window()
        # 打开前程贷页面
        self.driver.get(CD.login_url)
        # 登录，输入账号密码
        LoginPage(self.driver).login(CD.user, CD.passwd)
        self.lp = LoginPage(self.driver)
        self.bp = BidPage(self.driver)

    def tearDown(self) -> None:
        # 后置条件，关闭浏览器
        # 关闭浏览器
        self.driver.quit()

    # 正常场景 - 投资成功
    def test_invest_success(self):

        # 调用登录后的 点击抢标
        self.bp.click_bid()
        # 断言= url地址，应当为：http://120.78.128.25:8765/loan/loan_detail/Id/17951.html
        time.sleep(1)
        self.assertEqual(self.driver.current_url, CD.bid_url)
