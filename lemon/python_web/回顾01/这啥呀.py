# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：这啥呀.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/04 14:23
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end=' ')
#     print()


# aa = [12, 46, 321, 5, 19, 36, 2, 3, 7, 94, 2945]
# for i in range(len(aa)):
#     for j in range(len(aa)-i-1):
#         if aa[j] > aa[j+1]:
#             aa[j], aa[j + 1] = aa[j+1], aa[j]
# print(aa)


# 在一个字符串中查找目标字符串 并输出 首字母下标
# def index_of_str(s1, s2):
#     lt = s1.split(s2, 1)
#     if len(lt) == 1:
#         return -1
#     return len(lt[0])
#
#
# print(index_of_str('12abc34de5f', 'c34'))


# pyCharm = 'aAb bCd vEf A A'
# print(pyCharm.find('A',2))


# a = [1,5,58,89,2,898]
# for i in range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j +1] = a[j+1], a[j]
# print(a)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end=' ')
#     print()
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///E:/WebWebpageTest/page.html")
driver.maximize_window()  # 最大化浏览器

# 点击出现非HTML弹出框
driver.find_element_by_id('alert').click()
time.sleep(1)

# 切换弹框 需要接收返回的对象
al = driver.switch_to.alert

# 弹框的四个操作
print(al.text)  # 获取弹出框的文本
# al.dismiss()  # 取消
al.accept()  # 确定
# al.send_keys()  # 弹出框输入
# 暂停看操作
time.sleep(1)

driver.quit()
"""

