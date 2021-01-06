# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : 小程序自动化.py
# Author       : 大壮
# Create time  : 2020-01-01 11:04
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as MB

# 引入appium包
from appium import webdriver
import time
import os

"""
1\识别
2、开启调试：
针对微信版本在7.0+，微信有对H5开关做了调整，需要在聊天窗口输入如下：
http://debugmm.qq.com/?forcex5=true
http://debugx5.qq.com

3、appium代码当中：
   #支持X5内核应用自动化配置  desired_caps["recreateChromeDriverSessions"] = True
   # desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand0"}  # 小程序在哪个进程 

按微信小程序调试入口，进入到小程序页面。 发现 - 搜一搜 - 搜索 柠檬班软件测试

4、进入小程序之后，获取当前所有的上下文，切换进最后一个webview
   chromedriver版本要与腾讯x5版本匹配，而不是原生的webview

5、获取小程序当中所有的窗口。
   遍历所有窗口，并切入窗口的html中，查找有代表性的元素。
   driver.find_element
   driver.page_source.find("") != -1:
      break
"""

# 启动 appium 时，需要指定chromedriver.exe的目录。使用appium默认目录下的会报错。
# 在切换到小程序webview时，会去匹配chrome内核的39的驱动。在切换完成之后，在打印所有的窗口时，会使用x5内核的版本。
# 所以指定一个非默认目录下面的chromedriver.exe(X5内核对应的版本)，此问题就不会出现 。
# 在 appium server上设置chromedriver的路径：D:\\python\\chromedrivers\\52_54\\chromedriver.exe
# chromedriverExecutableDir
desired_caps = {}
# 支持X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"] = True
# android 4.4以下的版本通过Selendroid来切换到webview
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.0"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps["chromedriverExecutable"] = "D:\\python\\chromedrivers\\52_54\\chromedriver.exe"
desired_caps["noReset"] = True

# ChromeOptions使用来定制启动选项，因为在appium中切换context识别webview的时候,
# 把com.tencent.mm:toolsmp的webview识别成com.tencent.mm的webview.
# 所以为了避免这个问题，加上androidProcess: com.tencent.mm:toolsm
# options = wb.ChromeOptions()
# options.add_experimental_option("androidProcess","com.tencent.mm:toolsmp")
# 安卓进程
desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:appbrand0"}
# desired_caps["browserName"] = ""
