#!/usr/bin/python3
"""
@File    : home_page.py
@Time    : 2019/11/29 21:38
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from lemon_11_191206.PageLocators.home_page_loc import HomePageLoc as loc


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_user_exist(self):
        """
         # 检测用户名元素是否存在。
        如果退出元素存在，则返回True。否则返回False
        :return: 布尔值
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
        else:
            return True

    def click_first_bid(self):
        """
        点击首页的第一个标
        :return:
        """
        pass
