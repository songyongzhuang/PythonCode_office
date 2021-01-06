#!/usr/bin/python3
"""
@File    : 按键操作.py
@Time    : 2019/11/25 21:23
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)
# driver.find_element_by_id("").send_keys(Keys.CONTROL,"c")


