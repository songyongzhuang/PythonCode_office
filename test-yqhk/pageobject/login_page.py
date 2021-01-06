# coding=utf-8

from selenium.webdriver.common.by import By


class LoginPage(object):
    def __init__(self, dr):
        self.driver = dr.driver

    def username(self):
        return self.driver.find_element(By.NAME, "username")

    def password(self):
        return self.driver.find_element(By.NAME, "password")

    def button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".el-button")


class LoginPageLoc(object):
    # 用户名输入框
    username = (By.NAME, 'username')
    # 密码输入框
    password = (By.NAME, 'password')
    # 登陆按钮
    button = (By.CSS_SELECTOR, '.el-button')
