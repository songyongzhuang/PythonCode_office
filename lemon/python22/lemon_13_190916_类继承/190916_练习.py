# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 190916_练习.py
# Author       : Administrator
# Create time  : 2019-09-19 10:29
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！


class A:
    def a(self):
        print('这是大写A')


class B:
    def b(self):
        print('这是大写B')


class C:
    def c(self):
        print('这是大写C')


class D(A, B, C):
    def d(self):
        print('这是大写D')


d = D()
d.a()
d.b()
d.c()
d.d()
