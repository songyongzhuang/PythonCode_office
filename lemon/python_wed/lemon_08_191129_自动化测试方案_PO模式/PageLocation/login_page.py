# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : login_page.py
# Author       : 大壮
# Create time  : 2019-12-01 09:57
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # 账号输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    register_button = (By.XPATH, '//button[@type="button"]')
    # 错误提示框
    mistake_hint = (By.XPATH, '//div[@class="form-error-info"]')
    # 帐号或密码错误!提示框
    mistake_hint_account = (By.XPATH, '//div[@class="layui-layer-content"]')

    def __init__(self, driver):
        self.driver = driver

    # 元素操作 # 登陆操作
    def login(self, username, passwd):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.user_loc))
        # 输入用户名
        self.driver.find_element(*self.user_loc).send_keys(username)
        # 输入密码
        self.driver.find_element(*self.passwd_loc).send_keys(passwd)
        # 点击登陆
        self.driver.find_element(*self.register_button).click()

    # 获取提示信息
    def get_error_msg(self, hint):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(hint))
        return self.driver.find_element(*hint).text


