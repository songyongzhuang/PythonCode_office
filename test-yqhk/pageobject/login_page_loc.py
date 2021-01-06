# --*-- coding : utf-8 --*--
# Project      : test-yqhk-Project
# Current file : login_page_loc.py
# Author       : 菜鸟一号
# Create time  : 2020-12-07 18:15
# IDE          : PyCharm
# MAIL         : 邮箱地址
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.login_page import LoginPageLoc
from framework.base_page import BasePage


class LoginPage(BasePage):

    # 元素操作 # 登陆操作
    def login(self, username, passwd):
        # 登录页面_等待用户名输入框可见
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLoc.username))
        # 输入用户名
        self.input_text(LoginPageLoc.username, username, '登录页面_用户名输入')
        # 输入密码
        self.input_text(LoginPageLoc.password, passwd, '登录页面_密码输入')
        # 点击登陆
        self.click_element(LoginPageLoc.button, '登录页面_点击登录按钮')
