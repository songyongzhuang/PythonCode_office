# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：js_处理.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/28 10:39
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 启动谷歌浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 打开12306
driver.get("https://www.12306.cn/index/")
time.sleep(2)
# ===========================================================================
# 出发地
"""
BJP:北京, SHH:上海, TJP:天津, CQW:重庆, CSQ:长沙, CCT:长春
value="BJP"
"""
ele = driver.find_element_by_id('fromStationText')
region = '上海'
abbreviation = 'SHH'
js = f"""
var a = document.getElementById("fromStationText")
a.value = "{region}";
var b = document.getElementById("fromStation")
b.value = "{abbreviation}";
"""
driver.execute_script(js, ele)

# ===========================================================================
# 到达地
ele = driver.find_element_by_id('toStationText')
region = '长春'
abbreviation = 'CCT'
js = f"""
var a = document.getElementById("toStationText")
a.value = "{region}";
var b = document.getElementById("toStation")
b.value = "{abbreviation}";
"""
driver.execute_script(js, ele)

# ===========================================================================
# 修改时间
ele = driver.find_element_by_id('train_date')
cur_time = '2019-12-12'
js = f"""
var a = arguments[0]
a.readOnly = false;
a.value = "{cur_time}";
"""
driver.execute_script(js, ele)

# ===========================================================================
# 点击 查询
loc = (By.XPATH, '//a[@id="search_one"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 关闭所有窗口
driver.quit()
