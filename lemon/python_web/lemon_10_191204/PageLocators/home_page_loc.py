#!/usr/bin/python3
"""
@File    : home_page.py
@Time    : 2019/12/4 19:47
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium.webdriver.common.by import By


class HomePageLoc:
    # 退出元素定位
    exit_loc = (By.XPATH, '//a[text()="退出"]')
