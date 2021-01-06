# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习练习.py
# Author       : 大壮
# Create time  : 2019-09-14 20:31
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

"""
class MyError(Exception):
    print('456123')


try:
    1/0
except(IndexError, ZeroDivisionError, ) as e:
    print('异常')
finally:
    print('无论异常处理有没有执行，finally都会运行')
"""


class SingleDog:
    def __init__(self, name):
        self.name = name


# SingleDog('睡觉')  # 类的使用
# print(SingleDog)  # init初始化对象时候默认会执行

import random
print(random.randint(1, 3))
