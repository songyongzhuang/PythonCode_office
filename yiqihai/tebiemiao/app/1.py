# --*-- coding : utf-8 --*--
# Project      : app
# Current file : 1.py
# Author       : human
# Create time  : 2020-11-16 18:41
# IDE          : PyCharm
# MAIL         : 邮箱地址
# TODO 成长很苦，进步很甜，加油！
from pynput.mouse import Controller,Button
import time
# 实例化对象

mouse = Controller()

# 读取鼠标指针在屏幕上的位置
while True:
    # 设置鼠标指针的位置
    mouse.position = (200, 200)
    mouse.press(Button.left)
    time.sleep(5)
    mouse.position = (600, 600)
    time.sleep(5)

# 相对于当前位置移动指针
#     mouse.move(100, -100)
# # 按下并释放鼠标左键
#
# mouse.press(Button.left)
#
# mouse.release(Button.left)
#
# # 双击鼠标左键
#
# mouse.click(Button.left, 2)
#
# # 向下滚动两下（滑动鼠标上的滚轮）
#
# mouse.scroll(0, 2)
