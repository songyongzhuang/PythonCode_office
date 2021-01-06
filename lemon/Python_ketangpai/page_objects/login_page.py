# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : login_page.py
# Author       : 大壮
# Create time  : 2020-12-21 12:21
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
# 调用 首页操作的定位表达式
from page_locators.login_page_loc import LoginPageLoc as lpl
# 调用 基础定位(各种定位元素的方法)
from common2.base_page import BasePage


# 继承 BasePage 可以直接使用它的所有方法，
class LoginPage(BasePage):
    """
    账号登录元素操作
    """
    def login(self, register, account):
        """
        登录操作
        :param register: 传入账号
        :param account: 传入密码
        :return:
        """
        self.click_element(lpl.register_button, '首页页面_点击登陆按钮')
        time.sleep(0.5)
        self.input_text(lpl.account_input, register, '账号登录页面_账号输入框')
        self.input_text(lpl.password_input, account, '账号登录页面_密码输入框')
        self.click_element(lpl.enter_button, '账号登录页面_点击登陆按钮')

    # TODO (出现问题不显示了)获取 错误 提示信息
    def get_error_hint(self):
        return self.get_element_text(lpl.error_loc, "账号登录页面_表单区域错误提示")
