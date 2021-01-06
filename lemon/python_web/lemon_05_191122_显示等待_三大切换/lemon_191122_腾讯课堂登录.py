# --*-- coding : utf-8 --*--
# Project      : python_wed
# Current file : lemon_191122_腾讯课堂登录.py
# Author       : ***
# Create time  : 2019-11-24 17:41
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
# 打开谷歌浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待
# 打开腾讯课堂首页
driver.get("https://lemon.ke.qq.com/")
# 最大化浏览器
driver.maximize_window()

# 加一个刷新，有时候 登录 显示不出来
driver.refresh()

# 定位登录
register = (By.ID, "js_login")
# 等待元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(register))
# 点击登录
driver.find_element(*register).click()

# 弹出了登陆框
loc = (By.XPATH, '//div[@class="login-tab mod-tab"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))


# -------------------  点qq登录 -------------------
# 定位 点qq登录
QQ_account = (By.XPATH, "//a[@class='js-btns-enter btns-enter btns-enter-qq']")
# 等待元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(QQ_account))
# 点击
driver.find_element(*QQ_account).click()

# 定位上方的QQ账号登录
QQ_account_01 = (By.XPATH, "//li[@data-index='0']//a[@class='tab-link']")
# 等待元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(QQ_account_01))
# 点击
driver.find_element(*QQ_account_01).click()

# -----------------------------------------------------------------------------
# 弹出了登陆框
loc = (By.XPATH, '//div[@class="login-tab mod-tab"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))

# 通过 name 属性, 切换到登录框的 iframe 中
driver.switch_to.frame("login_frame_qq")

time.sleep(1)  # 不知道为啥，不停一下找不到
# 定位 帐号密码登录
accoun = (By.ID, "switcher_plogin")
# 等待元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(accoun))
# 点击
driver.find_element(*accoun).click()

# 定位到账号输入框输入账号
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('2353139876')

# 定位到密码输入框输入密码
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('ssong656421952')

# 点击登录
driver.find_element_by_id('login_button').click()

time.sleep(3)

# 关闭浏览器
driver.quit()
