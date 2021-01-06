# --*-- coding : utf-8 --*--
# Project      : python_web
# Current file : 滚动条操作.py
# Author       : 大壮
# Create time  : 2020-03-17 18:13
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"""
滚动的目的：将你要操作的元素，滚动到可视区域后，再操作
由js实现，
"""
# 键盘操作
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://cs.test.tebiemiao.cn/#/login")
driver.maximize_window()  # 最大化浏览器
# 输入用户名, 等待元素出现
user_loc = (By.XPATH, '//input[@name="username"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(user_loc))
driver.find_element_by_xpath('//input[@name="username"]').send_keys('11000000001')
# 输入密码
driver.find_element_by_xpath('//input[@name="password"]').send_keys('1234567')
# 点击登录
driver.find_element_by_xpath('//button[@type="button"]//span').click()
# 等待搜索结果出现
loc = (By.XPATH, '//span[text()="酒店管理"]')
# 找到要滚动的元素
ele = driver.find_element(*loc)

# 先滚动到可是区域后，
# 参数1、JavaScript脚本 参数2、传给JS脚本
# JS脚本中，用 arguments 来接收外部的参数
# js脚本中，用 scrollIntoView() 自动滚动到可视区域
# arguments 是列表，外部传递的列表， 只传递了一个值【0】
driver.execute_script('arguments[0].scrollIntoView();', ele)
# scrollIntoView() 默认与页面顶部对齐
# scrollIntoView(false) 页面底部对齐
# driver.execute_script('arguments[0].scrollIntoView();', ele)

# 再去点击
time.sleep(2)
driver.find_element(*loc).click()

driver.find_element_by_xpath('//span[text()="酒店查询"]').click()

"""
直接滚动到页面底部
driver.execute_script("window.scrollTO(0, document.body.scrollHeight)")
直接滚动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
"""
driver.quit()



