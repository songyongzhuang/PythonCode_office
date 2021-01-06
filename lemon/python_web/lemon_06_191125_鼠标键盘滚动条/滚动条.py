# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：滚动条.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/26 17:23
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
"""
滚动的目的：讲你要操作的元素，滚动到可视区域后，再操作
由 js 实现， 会自动滚动到位置
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 键盘操作 导入第三方库
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://www.baidu.com/")

driver.find_element_by_id('kw').send_keys('百度',Keys.ENTER)

# //a[text()='官方吧_']
# //h3[@class='t']//a[text()='地图']

# 找到要滚动的元素
loc = (By.XPATH, "//h3[@class='t']//a[text()='地图']")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)

# 先滚动到可视区域后
# 参数一、 javacript 脚本， 参数二、传给 js 脚本的参数
# js 脚本用 arguments 接受外部的参数
# arguments 是列表，外部传递的列表， 只传递了一个值【0】
# js 脚本中 用 scrollIntoView() 自动滚动到可视区域
driver.execute_script("arguments[0].scrollIntoView(false)", ele)
# scrollIntoView() 默认与页面顶部对齐
# scrollIntoView(false) 页面底部对齐

# 再去点击
time.sleep(2)
driver.find_element(*loc).click()

"""
直接滚动到页面底部
driver.execute_script("window.scrollTO(0, document.body.scrollHeight)")
直接滚动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
"""










