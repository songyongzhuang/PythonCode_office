# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：login_page_loc.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/04 10:09
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

from selenium.webdriver.common.by import By

"""
存放定位表达式
"""


class LoginPageLoc(object):
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button_loc = (By.TAG_NAME, "button")
    # 账号密码下方错误提示框
    form_error_loc = (By.XPATH, '//div[@class="form-error-info"]')
    # 帐号或密码错误!提示框
    dialog_error_loc = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 退出元素定位
    exit_loc = (By.XPATH, '//a[text()="退出"]')

    """ 投资 """
    a = ' 双12剁手'
    invest_loc = (By.XPATH, f'//span[text()="{a}"]//ancestor::div[@class="b-unit"]//a[text()="抢投标"]')
