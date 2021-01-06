import pytest
import time
import json
from selenium import webdriver
from framework.publicmethod import login
from pageobject.menusBar_page import MenusPage
from selenium.webdriver.common.by import By


class TestOrder(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://oms.test.tebiemiao.cn/")
        login.login(self)
        # print("\nsetup_class")

    def teardown_class(self):
        self.driver.quit()
        # print("\nteardown_class")

    def setup_method(self):
        MenusPage(self).header_order().click()
        print("\nsetup_method")

    # def teardown_method(self):
    #     print("\nteardown_method")

    # 检查订单-订单交易-订单查询-实物商品 的页面元素
    def test_01(self):
        # MenusPage(self).content_order_ddjy().click()
        MenusPage(self).content_order_ddjy_ddcx().click()
        print("\ntest_ss1")
        time.sleep(10)

    # def test_ss2(self):
    #     print("\ntest_ss2")
