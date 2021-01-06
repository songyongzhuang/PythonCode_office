#!/usr/bin/python3
"""
@File    : 滚动条.py
@Time    : 2019/11/25 21:31
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
"""
滚动的目的：将你要操作的元素，滚动到可视区域后，再操作。
由js实现。
很多的网页，是会自己滚的。
"""

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.maximize_window()

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)

# 等待搜索结果出现
loc = (By.XPATH,'//a[text()="-自动化测试-软件测试培训自学网"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
# 找到要滚动的元素
ele = driver.find_element(*loc)

# 先滚动到可视区域后，
# 参数1：javascript脚本  参数2。。。：传给js脚本的参数
# js脚本当中，用什么来接收外部的参数？arguments是个列表。
# js脚本当中，什么函数来滚动页面呢？scrollIntoView()
# scrollIntoView() 与页面顶部对齐。scrollIntoView(false) 与页面底部对齐。
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
# 再去点击
ele.click()

"""
直接滚动到页面底部：
 driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
直接滚动到页面顶部：
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

"""