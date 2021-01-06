# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : home_page.py
# Author       : 大壮
# Create time  : 2020-03-22 15:24
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 定位表达式
from tebiemiao_web.PageLocators.login_page_loc import LoginPageLoc as LOC

# 导入封装的页面基本操作
from tebiemiao_web.Common.base_page import BasePage


class HomePage(BasePage):

    def check_user_exist(self):
        """
        如果//span[@class="user_name"] 元素存在，则返回True 否则返回 False
        :return:
        """
        return self.check_element_visible(LOC.right_up_loc, '登录操作_登录后检测右上角定位是否存在')
