# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：鼠标操作.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/26 14:46
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# 鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")

# 1、实例化 ActionChains 鼠标类
ac = ActionChains(driver)
# 2、添加鼠标动作，调用对应的鼠标动作函数
ele = driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")
ac.move_to_element(ele).click(ele)
# 3、**执行鼠标操作perform()
ac.perform()

# 点击下拉列表
loc = (By.XPATH, "//a[text()='高级搜索']")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 专门处理 select/option 的下拉框
from selenium.webdriver.support.select import Select

# 初始化：参数必须是 select 元素对象
time.sleep(1)
select_ele = driver.find_element_by_xpath("//select[@name='ft']")
s = Select(select_ele)

s.select_by_value('ppt')  # value
s.select_by_index(3)  # 索引
s.select_by_visible_text('所有格式')  # 文本
