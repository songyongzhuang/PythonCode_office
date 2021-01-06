# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：asd.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/27 15:00
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.maximize_window()
ele = driver.find_element_by_id('kw')
ele.send_keys("京东商城", Keys.ENTER)
# win=driver.window_handles
# driver.switch_to.window(win[-1])

loc = (By.XPATH, '//a[contains(text(),"正品低价、品质保障")]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

win = driver.window_handles
driver.switch_to.window(win[-1])

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  //h3[text()='排行榜'] //*[@id="J_top"]/div[1]/a/h3
lo = (By.XPATH, "//h3[text()='排行榜']")
driver.execute_script("window.scrollBy(500,500)")

WebDriverWait(driver, 20).until(EC.visibility_of_element_located(lo))
ele = driver.find_element(*lo)

ele.click()
