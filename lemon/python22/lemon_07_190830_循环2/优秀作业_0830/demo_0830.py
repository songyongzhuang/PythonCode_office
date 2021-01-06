#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/16 20:52
# email:936763477@qq.com
# author: '墨墨'
# copyright：personal

# 1. 编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

def week(num):
    if 0 < num <= 5:
        return dio[num]
    elif num == 6 or num == 7:
        return '周末'


dio = {1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周日'}
while True:
    num = int(input('请输入一个整数：'))
    if 0 < num <= 7:
        print(week(num))
    elif num == 0:
        break
    else:
        print('输入有误，请重新输入！')

print('********************分割线*********************')

# 2. 列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素

lis = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(set(lis))

print('********************分割线*********************')


# 3. 将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。

def exchange(a, b):
    t = a
    a = b
    b = t
    return a, b


a = 100
b = 200
print('a,b的新值分别为', exchange(a, b))

print('********************分割线*********************')


# 4.编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
def health(height, weight):
    BMI = weight / height ** 2
    if BMI < 18.5:
        return '过轻'
    elif 18.5 <= BMI < 25:
        return '正常'
    elif 25 <= BMI < 28:
        return '过重'
    elif 28 <= BMI < 32:
        return '肥胖'
    elif BMI >= 32:
        return '严重肥胖'


height = float(input('请输入身高（m）：'))
weight = float(input('请输入体重（kg）：'))
print(health(height, weight))
