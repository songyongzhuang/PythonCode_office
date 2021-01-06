#!/usr/bin/python3
"""
@File    : 鼠标操作.py
@Time    : 2019/11/25 20:29
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")

# //*[@id="u1"]//a[@name="tj_settingicon"]
# driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]').click()

# 1、实例化ActionChains类。
ac = ActionChains(driver)
# 2、添加鼠标动作: 调用对应的鼠标动作函数。
ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')
ac.move_to_element(ele).click(ele)
# 3、执行鼠标动作：perform()
ac.perform()

# 下拉列表：1、触发下拉列表出现；2、等待你要操作的某项元素可见；3、选择你要操作的元素。
# //a[text()="高级搜索"]
loc = (By.XPATH,'//a[text()="高级搜索"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


# select/option类型的下拉列表，有专门的Select类来处理。
from selenium.webdriver.support.select import Select
# 1、初始化：参数是一个select元素对象。
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
select_ele = driver.find_element_by_xpath('//select[@name="ft"]')
s = Select(select_ele)
# 选择下拉列表当中的值：1）value属性 ；2）下标，从0开始；3）文本
s.select_by_value("ppt")  # value
time.sleep(2)
s.select_by_index(3) # 下标
time.sleep(2)
s.select_by_visible_text("所有格式") # 文本




