# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : toast.py
# Author       : 大壮
# Create time  : 2019-12-29 13:42
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from inspect import Traceback
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    "automationName": "UiAutomator2",  # 自动化引擎,不设置的话,默认为appium.
    "platformName": "Android",  # 操作系统
    "platformVersion": "5.1",  # 系统版本号
    "deviceName": "vivo",  # 设备名称
    "noReset": False,  # 应用重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban",  # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 20)

# 点击我的柠檬
loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_my")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击头像
loc = (MobileBy.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_image")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击登录
loc = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 弹出toast
loc = (MobileBy.XPATH, '//*[contains(@text, "手机号码或密码不能为空")]')
try:  # presence_of_element_located 存在
    WebDriverWait(driver, 20, 0.1).until(EC.presence_of_element_located(loc))
except Traceback:
    print('没找到')
else:
    text = driver.find_element(*loc).text
    print(text)
