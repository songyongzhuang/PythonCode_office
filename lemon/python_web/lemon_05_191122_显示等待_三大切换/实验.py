# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : 实验.py
# Author       : 大壮
# Create time  : 2019-11-23 08:12
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()  # 启动谷歌浏览器
# 最大化浏览器
driver.maximize_window()
# 打开网址
driver.get('file:///E:/WebWebpage/page.html')
time.sleep(1)
# 输入内容
driver.find_element_by_xpath("//input[@id='user']").send_keys('输入的内容')
time.sleep(1)
# 点击打开新窗口  //a[@id='ZCA']
driver.find_element_by_xpath("//a[@id='ZCA']").click()  # 点击
# 获取所有的句柄
win = driver.window_handles
print(f"所有的窗口句柄：{win}")
# 当前的窗口句柄
cur_win = driver.current_window_handle
print(f'当前的窗口句柄：{cur_win}')
# 切换窗口句柄
driver.switch_to.window(win[-1])
time.sleep(1)
driver.find_element_by_xpath("//input[@id='userA']").send_keys('新跳转的窗口')
# 关闭当前窗口
driver.close()

# 切换回第一个窗口
driver.switch_to.window(win[0])
driver.find_element_by_xpath("//input[@id='password']").send_keys('123456789')
time.sleep(1)

# 找到iframe 切换
driver.switch_to.frame("myframe1")  # name
time.sleep(1)
driver.find_element_by_xpath("//input[@id='userA']").send_keys('切换到A里面')
time.sleep(1)
# 切出来，直接切换到默认的主页面
driver.switch_to.default_content()

# 切到上一个iframe
# driver.switch_to.parent_frame()

time.sleep(1)
# 切换出来输入数据
driver.find_element_by_xpath("//input[@id='tel']").send_keys('切出来输入主页面')
time.sleep(1)
driver.quit()  # 关闭浏览器
