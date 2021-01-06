#!/usr/bin/python3
"""
@File    : iframe切换.py
@Time    : 2019/11/22 21:18
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
# 只想操作，你想操作的元素。
# 如果你要操作的元素，在iframe当中，那么必要切换到iframe.
# iframe - 新的html
# 0、你的元素是否在iframe当中？
# 1、找到这个iframe
# 2、切换到iframe
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
driver = webdriver.Chrome()  # 会话的起始标志。

# 找到iframe
# 1、iframe元素的name属性   # login_frame_qq
# 2、iframe元素的下标    # 2  从0开始
# 3、iframe对应的WebElement对象(driver.find_element_by_XXX)

# 切换
driver.switch_to.frame("login_frame_qq")  #name
driver.switch_to.frame(2)  # 下标
driver.switch_to.frame(driver.find_element_by_name('login_frame_qq'))  # webElement对象

# 切换完成之后，就直接是新的html页面里定位。

# 切出来，直接切换到默认的主页面
driver.switch_to.default_content()

# 切到上一个iframe
driver.switch_to.parent_frame()



