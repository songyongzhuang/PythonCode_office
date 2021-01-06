#!/usr/bin/python3
"""
@File    : login_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.TAG_NAME, "button")
    # 错误提示框
    form_error_loc = (By.XPATH, '//div[@class="form-error-info"]')

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
        self.driver.find_element(*self.login_button_loc).click()

    # 获取提示信息
    def get_error_msg(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.form_error_loc))
        return self.driver.find_element(*self.form_error_loc).text
