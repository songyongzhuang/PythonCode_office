#!/usr/bin/python3
"""
@File    : alert切换.py
@Time    : 2019/11/22 21:40
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

# 非 html元素
# Alert类
# 操作元素，导致非html弹出框出现
# 2、切换到它
# 3、将它关掉。

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
driver = webdriver.Chrome()   # 会话的起始标志。
driver.get(r"D:\Pychram-Workspace\py22-Web-Study\web_1122\xj_demo.html")

# 做一动作，非html弹出框出现
driver.find_element_by_id("press").click()
time.sleep(1)

# 切换
al = driver.switch_to.alert
# 关掉这个弹出框
al.dismiss()  # 取消
# al.accept()  # 确定
print(al.text)  # 获取弹出框的文本

#####
"""
1、显性等待：WebdriverWait等待\expected_condition条件
        WebdriverWait(driver,20).until(EC.条件)
   辅助等待：sleep

2、3大切换 
   windows切换
   iframe切换
   alert切换
   1）动作：导致窗口，iframe，alert出现。
   2）找到你要切换的它：窗口(先得到所有句柄，再切换到窗口句柄)、
                      iframe(name、下标、webelement对象)
                      alert
   3) 切换：driver.switch_to.window/frame/alert
   4) 关闭alert
"""

