"""
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
from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    # "automationName":"appium" # 自动化引擎,不设置的话,默认为appium.
    "platformName": "Android",  # 操作系统
    "platformVersion": "5.1",  # 系统版本号
    "deviceName": "huawei",  # 设备名称
    "noReset": True,  # 应用不重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban",  # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 20)

"""
1、python代码写好了
2、打开appium server，与appium建立连接，发送你的命令。
3、打开模拟器/真机-usb调试。保证，设备是可以被识别到的。
   adb命令： 检测已连接的设备-命令：adb devices
"""

# page_src = driver.page_source  # 获取页面源码。

loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_my")
wait.until(EC.visibility_of_element_located(loc))
# 单一属性：id，class，content-desc
driver.find_element(*loc).click()
# class
# driver.find_element_by_class_name("android.widget.FrameLayout")
# content -desc  Android
# driver.find_element_by_accessibility_id("")


# 组合定位：android_uiautmator, xpath
"""
android_uiautomator： 直接使用安卓自带自动化测试框架uiAutomator的元素定位方式。
元素定位方式：java语言的类！类名：UiSelector  类下的函数都是元素定位方式。

java当中的字符串：必须是双引号！！！
java当中的类的实例化：new UiSelector()

公式：new UiSelector().函数名称(定位表达式)

示例：
new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my").className("android.widget.FrameLayout")
new UiSelector().text("全程班")

操作：click(),send_keys(),get_attribute(),text

"""
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")')
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")')
