# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：lemon_作业_191128.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/28 15:00
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains

# 启动谷歌浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 打开12306
driver.get("https://www.12306.cn/index/")

# ===========================================================================
# 出发地
"""
# 方法一
# 1、实例化 ActionChains 鼠标类
ac = ActionChains(driver)
# 2、添加鼠标动作，调用对应的鼠标动作函数
ele = driver.find_element_by_xpath("//input[@id='fromStationText']")
ac.move_to_element(ele).click(ele)
# 3、**执行鼠标操作perform()
ac.perform()

# 选择北京
loc = (By.XPATH, '//ul[@id="ul_list1"]//li[@data="BJP"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
"""

# 出发地输入
departure = '北京'
loc = (By.XPATH, '//input[@id="fromStationText"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys(f'{departure}')

loc = (By.XPATH, f'//div[@id="panel_cities"]//span[text()="{departure}"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# ===========================================================================
# 到达地
"""
# 方法一
ac = ActionChains(driver)
ele = driver.find_element_by_xpath("//input[@id='train_date']")
ac.move_to_element(ele).click(ele)
ac.perform()

# 选择 FGHIJ
loc = (By.XPATH, '//li[@id="nav_list3"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 选择济南
loc = (By.XPATH, "//div[@id='ul_list3']//ul[@class='popcitylist']//li[@data='JNK']")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
"""
# 到达地输入
arrive = '济南'
loc = (By.XPATH, '//input[@id="toStationText"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys(f'{arrive}')

loc = (By.XPATH, f'//div[@id="panel_cities"]//span[text()="{arrive}"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# ===========================================================================
# 选择出发日期
# 点击 日历 按钮
loc = (By.XPATH, '//i[@data-click="train_date"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 出发日期   12-12
loc = (By.XPATH, '//div[@style="left: 171px; top: 29px; cursor: pointer;"]//div[text()="12"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# ===========================================================================
# 点击 查询
loc = (By.XPATH, '//a[@id="search_one"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# ===========================================================================
# 获取句柄跳转新页面

# 获取所有窗口的句柄
wins = driver.window_handles
print("所有窗口句柄：", wins)
cur_win = driver.current_window_handle
print("当前的窗口句柄是：", cur_win)
# 切换到最新打开的窗口，存储的是一个列表，新打开的列表在最后，使用列表切片
driver.switch_to.window(wins[-1])
# 切换后进去, 关闭新窗口
driver.close()

# 关闭所有窗口
driver.quit()
