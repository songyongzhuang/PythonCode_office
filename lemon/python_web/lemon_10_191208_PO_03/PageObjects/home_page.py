# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：home_page.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/03 20:25
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from lemon_10_191208_PO_03.PageLocators.login_page_loc import LoginPageLoc as loc


class HomePage:

    def __init__(self, driver: WebDriver):  # 解决问题：点不出来方法的函数
        self.driver = driver  # 拥有所有 WebDriver 的方法

    def check_user_exist(self):
        """
        检测退出是否存在
        如果退出元素存在，返回True, 否则显示False
        布尔值, 只要是异常就返回False
        """''
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.exit_loc))
        except:
            return False
            # 只要是异常就返回False
        else:
            return True

    def click_first_bid(self):
        """
        点击首页的第一个标
        :return: 
        """''

