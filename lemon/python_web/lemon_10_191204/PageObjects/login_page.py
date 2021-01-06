#!/usr/bin/python3
"""
@File    : login_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lemon_10_191204.PageLocators.login_page_loc import LoginPageLoc as loc


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # 元素操作 # 登陆操作
    def login(self, username, passwd):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入用户名
        self.driver.find_element(*loc.user_loc).send_keys(username)
        # 输入密码
        self.driver.find_element(*loc.passwd_loc).send_keys(passwd)
        # 点击登陆
        self.driver.find_element(*loc.login_button_loc).click()

    # 获取提示信息
    def get_error_msg(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.form_error_loc))
        return self.driver.find_element(*loc.form_error_loc).text

    # 获取页面中的错误提示信息
    def get_error_msg_from_dialog(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(loc.dialog_error_loc))
        return self.driver.find_element(*loc.dialog_error_loc).text
