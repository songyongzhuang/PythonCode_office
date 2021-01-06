# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：b1.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/11/14 11:23
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import time

from selenium import webdriver

# 打开谷歌浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 访问百度首页
driver.get("https://www.ketangpai.com/")
# 等待五秒，最好不要使用这个方式，太差劲

time.sleep(2)  # 等待1秒


# 点登录
driver.find_element_by_xpath("//a[@class='login']").click()
time.sleep(2)  # 等待1秒
# 输入账号   send_keys
driver.find_element_by_xpath("//input[@type='text']").clear()
driver.find_element_by_xpath("//input[@type='text']").send_keys('17662460324')

time.sleep(2)  # 等待1秒
# 输入密码  send_keys
driver.find_element_by_xpath("//input[@type='password']").clear()
driver.find_element_by_xpath("//input[@type='password']").send_keys('song656421952')

# 点击登录
driver.find_element_by_xpath("//a[@class='btn-btn']").click()

time.sleep(2)  # 等待1秒

# 用户头像
# driver.find_element_by_xpath("//img[@class='avatar']").click()
# time.sleep(2)  # 等待1秒

# 退出账户
driver.find_element_by_xpath("//strong//a[@title='Python全栈第22期']").click()
time.sleep(3)

# 关闭浏览器
driver.quit()


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end=' ')
#     print()
#
# a = [2, 66, 4,78, 1, 3, 5]
# for i in range(1, len(a)):
#     for j in range(0, len(a)-i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)
#
# # [1, 2, 3, 4, 5, 66, 78]
