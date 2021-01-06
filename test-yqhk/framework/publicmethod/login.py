from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pageobject.login_page import LoginPage


def login(self):
    driver = self.driver
    # driver.maximize_window()
    LoginPage(self).username().click()
    LoginPage(self).username().send_keys("admin")
    LoginPage(self).password().send_keys("admin")
    LoginPage(self).button().click()


class CD(object):
    # 服务器访问 base_url
    base_url = 'https://oms.test.tebiemiao.cn'
    # 登录地址
    login_url = base_url + '/#/login'
    # 首页地址(登录成功的首页)
    home_url = base_url + '/#/goods/index'
