# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : login_page.py
# Author       : 大壮
# Create time  : 2020-03-22 15:23
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！  登录页面
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 定位表达式
from tebiemiao_web.PageLocators.login_page_loc import LoginPageLoc as LOC

# 导入封装的页面基本操作
from tebiemiao_web.Common.base_page import BasePage


# 继承封装的页面基本操作
class LoginPage(BasePage):

    # 元素操作
    # 登录操作
    def login(self, user, password):
        self.input_text(LOC.user_loc, user, '平台后台登录页面_用户名输入框')
        self.input_text(LOC.password_loc, password, '平台后台登录页面_密码输入框')
        self.click_element(LOC.login_button_loc, '平台后台登录页面_点击登录按钮')

    # 获取登录 - 错误弹框 - 提示信息
    def get_error_user(self):
        return self.get_element_text(LOC.from_error_User, '登录页面_获取弹框提示')

    # 获取登录 - 错误 《密码不能小于6位》 - 提示信息
    def get_error_password(self):
        return self.get_element_text(LOC.from_error_Password, '登录页面_密码区域错误提示')
