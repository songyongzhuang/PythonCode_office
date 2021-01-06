# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : login_page_loc.py
# Author       : 大壮
# Create time  : 2020-12-21 12:02
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

from selenium.webdriver.common.by import By


class LoginPageLoc(object):
    """
     首页操作 定位表达式
    """
    # 首页的登录按钮
    register_button = (By.XPATH, '//a[text()="登录"]')
    # 账号登录：账号输入框
    account_input = (By.XPATH, '//input[@name="account"]')
    # 账号登录：密码输入框
    password_input = (By.XPATH, '//input[@name="pass"]')
    # 账号登录：登录按钮
    enter_button = (By.XPATH, '//div[@class="padding-cont pt-login"]//a[text()="登录"]')
    # 账号登录：错误提示(不输入账号、密码)
    error_loc = (By.XPATH, '//p[@class="error-tips"]')
