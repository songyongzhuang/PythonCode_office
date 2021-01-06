# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : 登录lemonban.py
# Author       : 大壮
# Create time  : 2019-12-25 08:59
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
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

# 输入手机号
loc = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("17662460324")

# 输入密码
loc = (MobileBy.ID, "com.lemon.lemonban:id/et_password")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("460324")

# 点击登录
loc = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 断言
loc = (MobileBy.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_title")
# 等待元素可见, 获取文本
wait.until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc).text
try:
    if ele != '一八.十.四':
        print('退出app')
        driver.close_app()
except:
    print('异常')

# 点击右上角设置
loc = (MobileBy.CLASS_NAME, "android.widget.ImageButton")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击退出登录
loc = (MobileBy.ID, "com.lemon.lemonban:id/logout_button")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击确定按钮
loc = (MobileBy.ID, "com.lemon.lemonban:id/tv_sure")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 关闭app
driver.close_app()
