# --*-- coding : utf-8 --*--
# Project      : python_web
# Current file : 下拉列表.py
# Author       : 大壮
# Create time  : 2020-03-16 18:50
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 下拉操作
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.get("file:///E:/WebWebpageTest/page.html")

# 等待元素出现
loc = (By.XPATH, '//select[@id="select"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))

# 下拉列表：1、触发下拉列表出现，2、等地你要操作的元素可见，3、选择你要操作的元素
# 1、初始化：参数必须是一个select元素对象
select_ele = driver.find_element_by_xpath('//select[@id="select"]')
s = Select(select_ele)

# 2、选择下拉列表中的值：1、value属性，2、下标，从零开始，3、文本定位
# 通过value属性
s.select_by_value('sh')
time.sleep(2)
# 通过下标
s.select_by_index(2)
time.sleep(2)
# 通过文本
s.select_by_visible_text('重庆')
time.sleep(2)

driver.quit()
