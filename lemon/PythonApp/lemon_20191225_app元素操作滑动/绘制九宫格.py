# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : 绘制九宫格.py
# Author       : 大壮
# Create time  : 2019-12-27 16:09
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

"""
可使用的帐号： 18684720553/python      13760246701/python
"""
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
    "noReset": False,  # 应用重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.xxzb.fenwoo",  # 包名
    "appActivity": "com.xxzb.fenwoo.activity.MainActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 9)

# 点击我
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 输入手机号
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/et_phone")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("18684720553")
# 点击下一步
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_next_step")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 输入密码
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/et_pwd")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("python")
# 点击确定
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_next_step")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击马上设置
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_confirm")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击创建手势密码
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/btn_gesturepwd_guide")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击 确定 创建手势密码
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

"""
初始化
"""
# 获取整个高和宽
device_size = driver.get_window_size()

ta = TouchAction(driver)
ta.press()  # press ：按住

# 得到元素本身的起点坐标，它的高和宽
ele = driver.find_element(MobileBy.ID, 'com.xxzb.fenwoo:id/gesturepwd_create_lockview')
loc = ele.location  # 起点 元素在可呈现画布中的位置  X  Y
# 元素的大小
size = ele.size  # size : height 高度 width 宽度

step = size['width']/6  # 九宫格可以平均分成六小份

# 定位第一个点，x/y轴各走全部的六分之一
p1 = (loc['x']+step, loc['y']+step)
p2 = (p1[0] + 2*step, p1[1])
p3 = (p2[0] + 2*step, p2[1])
p4 = (p3[0] - 2*step, p3[1] + 2*step)
p5 = (p4[0] - 2*step, p4[1] + 2*step)
p6 = (p5[0] + 2*step, p5[1])
p7 = (p6[0] + 2*step, p6[1])

ta.press(x=p1[0], y=p1[1]).wait(200).\
    move_to(x=p2[0], y=p2[1]).wait(200).\
    move_to(x=p3[0], y=p3[1]).wait(200).\
    move_to(x=p4[0], y=p4[1]).wait(200).\
    move_to(x=p5[0], y=p5[1]).wait(200).\
    move_to(x=p6[0], y=p6[1]).wait(200).\
    move_to(x=p7[0], y=p7[1]).wait(200).\
    release().\
    perform()  # release：释放、perform：执行操作、move_to：滑动、wait：等待


time.sleep(3)
# 点击创建手势重试按钮
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxzb.fenwoo:id/reset_btn")')
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 关闭app
driver.close_app()
