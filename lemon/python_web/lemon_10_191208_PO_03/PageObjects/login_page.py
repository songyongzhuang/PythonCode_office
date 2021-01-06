# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：login_page.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/03 20:26
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lemon_10_191208_PO_03.PageLocators.login_page_loc import LoginPageLoc as loc
from lemon_10_191208_PO_03.Common.basepage import BasePage


class LoginPage(BasePage):

    # 元素操作 # 登陆操作
    def login(self, username, passwd):
        # 登录页面_等待用户名输入框可见
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入用户名
        self.imput_text(loc.user_loc, username, '登录页面_用户名输入')
        # 输入密码
        self.imput_text(loc.passwd_loc, passwd, '登录页面_密码输入')
        # 点击登陆
        self.click_element(loc.login_button_loc, '登录页面_点击登录按钮')

    # 获取 提示信息
    def get_error_msg(self):
        return self.get_element_text(loc.form_error_loc, '登录页面_表单区域获取错误')

    # 获取页面中的错误提示信息 帐号或密码错误!提示框
    def get_error_msg_from_dialog(self):
        return self.get_element_text(loc.dialog_error_loc, '登录页面_页面中的错误提示信息')
