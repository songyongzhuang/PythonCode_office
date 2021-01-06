
# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : calc.py
# Author       : 大壮
# Create time  : 2019-10-10 20:07
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 1+2=3
# 1+'a' ==> 预期结果报错，None


def add(a, b):
    """ 加 , 当ab都不是数字的时候，返回 None
    不返回的话默认就是None """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # return None  # 不写默认也是返回None


def minus(a, b):
    """ 减 """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b


def multiply(a, b):
    """ 乘 """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b


def division(a, b):
    """ 除 """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
        return a / b
