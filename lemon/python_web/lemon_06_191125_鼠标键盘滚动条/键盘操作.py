# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：滚动条操作.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/26 17:12
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 键盘操作 导入第三方库
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")

driver.find_element_by_id('kw').send_keys('天龙八部荣耀版',Keys.ENTER)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')  # Ctrl + c

