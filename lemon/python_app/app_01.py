# --*-- coding : utf-8 --*--
# Project      : Python_app
# Current file : app_01.py
# Author       : 大壮
# Create time  : 2019-12-21 11:14
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',  # 操作系统
    'platformVersion': '5.1',  # 系统版本
    'deviceName': 'huawei',  # 设备名称
    'noReset': True,  # 应用不重置

    # app：独一无二的包名
    # apk包。
    'appPackage': 'com.lemon.lemonban',  # 包名
    'appActivity': 'com.lemon.lemonban.activity.MainActivity'

}

# 链接 appium
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 20)

# 我的柠檬 元素可见
loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_my")
wait.until(EC.visibility_of_element_located(loc))

# 点击我的柠檬
driver.find_element(*loc).click()

# classname
# driver.find_element_by_class_name("android.widget.FrameLayout")

# content -desc
driver.find_element_by_accessibility_id()




"""
1、python代码写好了
2、打开appium server ，与 appium 简历链接，发送你的命令
3、打开模拟器/真机，USB 调试，保证设置时可以被识别的
adb命令：检测已链接的设备-命令：adb devices
emulator-5554

1、usb连接了一个设备(android5.1)到电脑端，开启了USB调试模式
2、appium server  --(android/IOS)
3、python代码

任务：通过写一段python代码，在android设备上，打开 柠檬班app.

1、你告诉appium server，你要在XX设备上，打开XXapp
2、appium收到你的命令之后，检测一下是否有XX设备，检测一下设备上是否有XXapp
3、2)确认成功，就执行命令。

获取应用包名和入口activity：aapt命令
aapt目录：
安卓sdk的build-tools目录下
示例：adt-bundle-windows-x86_64-20140702\sdk\build-tools\android-4.4W
命令语法：
aapt dump badging apk应用名
示例：aapt dump badging D:\BaiduNetdiskDownload\Future-release-2018.apk
"""
