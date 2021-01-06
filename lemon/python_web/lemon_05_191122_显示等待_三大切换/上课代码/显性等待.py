#!/usr/bin/python3
"""
@File    : 显性等待.py
@Time    : 2019/11/22 19:46
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
# 强制等待：sleep - 辅助功能。
# 隐性等待：智能等待。DOM页面，给它一个上限，上限范围之内，什么时候元素存在/命令执行完成了，什么时候就不再等待了。
#          一次会话在当中，在启动会话(webdrvier.Chrome())到结束会话(driver.quit())之间，只需要调用一次。
# 显性等待(明明白白的条件)：智能等待。上限时间范围之内，等待 XXX 条件成立，就结束等待。
#   1）时间上限。2）条件  3)等待（时间上限，轮询的周期）
# 等待：WebdriverWait类    条件：expected_condition

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
driver = webdriver.Chrome()  # 会话的起始标志。
driver.implicitly_wait(30)  # 隐式等待
driver.get("http://www.baidu.com")

driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# 弹出了登陆框 - 页面的变化 默认0.5秒
# WebDriverWait(driver,等待上限,轮询周期).until(条件)
loc = (By.ID, "TANGRAM__PSP_10__footerULoginBtn")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
# EC.visibility_of_element_located(loc)
# 元素可见   visibility_of_element_located EC.visibility_of_element_located(loc)
# 元素们可见    EC.visibility_of_all_elements_located
time.sleep(1)
driver.find_element(*loc).click()


