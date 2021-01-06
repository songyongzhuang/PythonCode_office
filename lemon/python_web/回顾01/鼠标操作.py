# --*-- coding : utf-8 --*--
# Project      : python_web
# Current file : 鼠标操作.py
# Author       : 大壮
# Create time  : 2020-03-16 17:41
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 鼠标
from selenium.webdriver.common.action_chains import ActionChains
# 下拉操作
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.get("file:///E:/WebWebpageTest/page.html")

# 悬浮的元素 //button[text()="注册用户"]
# 1、实例化 ActionChains 类
ac = ActionChains(driver)
# 2、添加鼠标动作：调用对应的鼠标动作函数
ele = driver.find_element_by_xpath('//select[@id="select"]')
ac.click(ele)  # 点击
# 3、执行鼠标动作：perform()
ac.perform()

# 下拉列表：1、触发下拉列表出现，2、等地你要操作的元素可见，3、选择你要操作的元素
loc = (By.XPATH, '//select[@id="select"]//option[@value="sh"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

driver.quit()
