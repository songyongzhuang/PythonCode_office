# --*-- coding : utf-8 --*--
# Project      : PythonApp
# Current file : 列表滑动.py
# Author       : 大壮
# Create time  : 2019-12-29 12:32
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
"""
1、进入到页面的时候， 要确认一下，你要找的元素是否存在
2、如果不存在，滑动一下页面，新的页面内容当中，再次确认，你要找的元素是否存在
3、重复2，一直到找到元素为止.drier.find_element / page_source 是否能找到你的文本
        一直到无法滑动为止.滑动当前的page_source == 滑动后的page_source
"""
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
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 20)

# 点击 题库 --
loc = (MobileBy.ID, "com.lemon.lemonban:id/navigation_tiku")
# 等待元素可见
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

"""
while 条件，内部要有一个退出循环的出口
每一次循环，每一个滑动之后，都需要在内部判断元素是否找得到
循环的条件是：滑前和滑后的页面不相等
"""
# 要查找的元素
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("接口测试")')

old = None
# 获取页面的源代码
new = driver.page_source

while old != new:
    # 判断元素是否找得到
    try:
        # 等待 题库 类型都可见
        tiku_type_loc = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
        # 元素可见
        wait.until(EC.visibility_of_all_elements_located(tiku_type_loc))
        time.sleep(1)
        ele = driver.find_element(*loc)
    except Exception:  # 当前页面没找到元素，需要滑动到写一步，滑动之后，
        # 获取整个高和宽
        device_size = driver.get_window_size()
        # 从下向上滑动 swipe 两个一组，两个一组
        driver.swipe(device_size['width'] * 0.5, device_size['height'] * 0.85,
                     device_size['width'] * 0.5, device_size['height'] * 0.25)
        # 更新两个值
        old = new
        new = driver.page_source
    else:
        print('找到了，')
        break










