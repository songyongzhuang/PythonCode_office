# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : login_page_loc.py
# Author       : 大壮
# Create time  : 2020-03-24 18:12
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 登录页面 - 元素定位
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="username"]')
    # 密码输入框
    password_loc = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//button[@type="button"]//span')
    # 用户名 - 账号错误-弹框
    from_error_User = (By.XPATH, '//p[@class="el-message__content"]')
    # 密码 - 下方错误提示-非弹框
    from_error_Password = (By.XPATH, '//div[@class="el-form-item__error"]')
    # 登录后的右上角登录名  运营管理
    right_up_loc = (By.XPATH, '//span[text()="运营管"]')
