# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : 滑屏操作.py
# Author       : 大壮
# Create time  : 2019-12-27 18:43
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 模拟触屏操作
from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

desired_caps = {
    # "automationName":"appium" # 自动化引擎,不设置的话,默认为appium.
    "platformName": "Android",  # 操作系统
    "platformVersion": "5.1",  # 系统版本号
    "deviceName": "vivo",  # 设备名称
    "noReset": True,  # 应用重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban",  # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 9)

time.sleep(1)
# 点击题库
loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_tiku")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待库类型的都可见选择有 S 的
loc = (MobileBy.ID, "com.lemon.lemonban:id/fragment_category_type")
# 等待元素可见
wait.until(EC.visibility_of_all_elements_located(loc))
time.sleep(2)
# 滑屏函数
# driver.swipe()
"""
swipe: 滑屏操作
"""
# 整个设置的大小
# 获取整个高和宽
device_size = driver.get_window_size()
# 从下向上滑动 swipe 两个一组，两个一组
driver.swipe(device_size['width']*0.5, device_size['height']*0.85,
             device_size['width']*0.5, device_size['height']*0.15)

time.sleep(2)
# 从上向下滑动 swipe 两个一组，两个一组
driver.swipe(device_size['width']*0.5, device_size['height']*0.15,
             device_size['width']*0.5, device_size['height']*0.85)

time.sleep(2)
# 从左到右 swipe 两个一组，两个一组
driver.swipe(device_size['width']*0.15, device_size['height']*0.5,
             device_size['width']*0.85, device_size['height']*0.5)

time.sleep(2)
# 从右到左 swipe 两个一组，两个一组
driver.swipe(device_size['width']*0.85, device_size['height']*0.5,
             device_size['width']*0.15, device_size['height']*0.5)
time.sleep(2)

