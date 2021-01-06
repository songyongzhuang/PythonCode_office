# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : H5_混合应用.py
# Author       : 大壮
# Create time  : 2019-12-29 14:23
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import time
from inspect import Traceback
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    # "automationName":"appium" # 自动化引擎,不设置的话,默认为appium.
    "platformName": "Android",  # 操作系统
    "platformVersion": "5.1",  # 系统版本号
    "deviceName": "vivo",  # 设备名称
    "noReset": True,  # 应用不重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban",  # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",  # 入口页面: activity
    "chromedriverExecutable": r"D:\\python\\chromedrivers\\52_54\\chromedriver.exe"
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 20)

# 点击全程版
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全程班")')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待 webView 元素可见
loc = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
time.sleep(2)

# 获取当前所有的contests
cons = driver.contexts
print(cons)
# 获取当前的context
print(driver.current_context)
# 切换 进入了 HTML 页面
driver.switch_to.context(cons[-1])

# 点击 立即购买
loc1 = (MobileBy.XPATH, '//button[text()="立即购买"]')
wait.until(EC.visibility_of_element_located(loc1))
driver.find_element(*loc1).click()
