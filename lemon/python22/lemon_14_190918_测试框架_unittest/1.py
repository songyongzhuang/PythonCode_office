# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 1.py
# Author       : 大壮
# Create time  : 2019-09-19 21:42
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


def add(*args):
    s = 0
    for e in args:
        s += e
    return s


h = add(1, 2, 3)
print(h)
