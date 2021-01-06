#!/usr/bin/python3
"""
@File    : 窗口操作.py
@Time    : 2019/11/22 20:39
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
# 0、先打开新的窗口
# 1、知道你要切的窗口叫什么？ --- 句柄。 获取当前会话浏览器打开的所有窗口句柄。
# driver.window_handles  -- 列表。按照窗口出现的顺序。
# 2、切换过去：driver.switch_to.window(window的句柄)
# 3、进入了一个新的页面：元素操作/查找 --只针对新的页面。

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
driver = webdriver.Chrome()  # 会话的起始标志。
driver.get("http://www.baidu.com")

# 搜索 柠檬班，点击柠檬班第一个结果。
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
# 要等待结果出现，搜索结果当中，选第一个
loc = (By.XPATH, '//a[text()="腾讯课堂 - 机构主页"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 导致新的窗口出现了。
# 等待有新的窗口出现，我再去切换窗口。
time.sleep(0.5)
# 获取所有窗口的句柄
wins = driver.window_handles
print("所有窗口句柄：", wins)
cur_win = driver.current_window_handle
print("当前的窗口句柄是：", cur_win)
# 切换到最新打开的窗口
driver.switch_to.window(wins[-1])
# 新的窗口
loc = (By.XPATH, '//ul[@id="js-tab"]//h2[contains(text(),"老师")]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# EC.new_window_is_opened


