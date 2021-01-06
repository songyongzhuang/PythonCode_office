#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @time     :2019/8/31 21:34
# @author   :天儿
# @file     :Homework_tianer_0830.py
# @software :win10 python3.7.2
#
# 1.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

# # 函数

def which_week1(a):
    """方式一：在函数中使用了字典，
    输入一周7天的任意数字，判断分别对应的周几"""
    a_week = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
    if a in a_week.keys():
        return a_week[a]


def which_week2(a):
    """方式2,使用列表，这种方式明显没有第一种好用，这种方式需要校验输入的类型
    输入一周7天的任意数字，判断分别对应的周几"""
    try:
        a_week = ['周一', '周二', '周三', '周四', '周五', '周末', '周末']
        if 0 < int(a) < 8:
            return a_week[int(a) - 1]
    except ValueError:
        return False


#
# # 循环
while True:  # 方式一：在while True 中用break 跳出循环
    info_num = input("请输入1-7中的任意数字：")
    if info_num == '0':
        print('退出！')
        break
    else:
        if which_week1(info_num):
            print(which_week1(info_num))
        else:
            print("输入有误，请重新输入！")
#
#
info_num = input("请输入1-7中的任意数字：")
while info_num != '0':  # 方式二：在while后 加入循环条件，若不符合循环条件，则跳出
    if which_week2(info_num):
        print(which_week2(info_num))
        info_num = input("请输入1-7中的任意数字：")  # 由于第一次赋值没有在循环中，所以在循环内需要再次赋值
    else:
        info_num = input("输入有误，请重新输入:")  # 由于第一次赋值没有在循环中，所以在循环内需要再次赋值
else:
    print('退出！')

# 2.列表去重
original_list = [2, 4, 2, 4, 4, 5, 5, 5, 4, 4, 2, 2, 3, 4, 3, 4, 4, 4, 2, 2, 2, 2, 4, 2, 4]
# [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]

# 方法一：使用集合的去重功能 （去重后顺序与原来不一致）
current_list = list(set(original_list))
print(current_list)

current_list.sort(key=original_list.index)  # 去重后后按照原有的索引排序
print(current_list)

# 方法二：for 遍历列表，若列表中该元素的个数大于1，则删除该元素  （若元素重复，先删除前面的）
for i in original_list[:]:
    if original_list.count(i) > 1:
        original_list.remove(i)
print(original_list)

# 方法三：for 遍历列表，若列表中该元素的个数大于1，若这个元素有n个，那么就重复删除该元素n-1次 （若元素重复，先删除前面的）
for i in original_list[:]:
    if original_list.count(i) > 1:
        for j in range(original_list.count(i) - 1):  # 这一步是重复删除大于一个的元素
            original_list.remove(i)
print(original_list)

# 方法四：for 遍历复制的列表，取前面的值依次与其后面比较，若相同则删除原列表后面的值  （若元素重复，先删除前面的）
for i in original_list[:-1]:  # 不取最后一个，是因为如果i是最后一个值，那么j就取不到值了，多进行了一次无意义的比较
    for j in original_list[original_list.index(i) + 1:]:  # j只取i后面的元素
        if i == j:
            original_list.remove(j)
print(original_list)

# 方法五：for 遍历表中的元素，把元素一个一个放入新的列表，若重复则不放  (去重后顺序与原来一致)
# 取自百度（感觉这种方式好理解也好用，还不改变去重后的顺序）
current_list = []
for i in original_list:  # 不取最后一个，是因为如果i是最后一个值，那么j就取不到值了，多进行了一次无意义的比较
    if i not in current_list:
        current_list.append(i)
print(current_list)

# 方法六：fromkeys（seq）用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
# 由于创建字典时，key不可重复，所以fromkeys（seq）有去重作用  (去重后顺序与原来一致)
# 取自百度
dict_null = {}  # 空字典
dict_create = dict_null.fromkeys(original_list)  # 空字典使用列表为key创建一个字典
current_list = list(dict_create.keys())  # 取出字典的key,转换成列表
print(current_list)


# 3.将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。

def change(a, b):  # 最基本的根据第三方元素来换
    c = 0
    c = a
    a = b
    b = c
    return a, b


def change1(a, b):  # 元素互换位置的简便方式
    a, b = b, a
    return a, b


def change2(a, b):  # 根据函数中位置参数的性质来return出相反值
    return b, a


x = {1: 'a', 2: 'b', 3: 'c'}
y = 'ewqeqwe'
(x, y) = change(x, y)  # 返回出来的是一个元组
print('x ={0},y={1}'.format(x, y))  # 打印时使用元组解包


# 4.编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖

# 第一种：(只把计算BIM值封装了；使用if判断比较输出BMI对应的健康状况；有校验输入输出退出等)
def bmi_1(height, weight):
    """得到身高，体重，返回BMI
    若无法计算得到，则返回False
    """
    try:
        bim_value = float(weight) / float(height) ** 2
        return bim_value
    except ValueError:
        return False


while True:
    info_height = (input('请输入您的身高(m)（输入均为空则退出）：'))
    info_weight = (input('请输入您的体重(kg)（输入均为空则退出）：'))
    if not info_height and not info_weight:
        print('退出！')
        break
    elif not bmi_1(info_height, info_weight):
        print('输入不合法或少输入任意一项')
    else:
        bim_value = bmi_1(info_height, info_weight)
        if bim_value < 18.5:
            print('您体重过轻')
        elif bim_value <= 25:
            print('您体重正常')
        elif bim_value <= 28:
            print('您有点重')
        elif bim_value <= 32:
            print('您属于肥胖')
        else:
            print('您属于严重胖')


# 第二种：( 把BIM和对应健康表均封装了；使用字典和for循环查找对应BMI的健康数据；不再重复加其他输入输出校验和循环了)
def bmi_2(height, weight):
    """得到身高，体重，计算出BMI，对比列表后，直接返回健康数据(不加异常捕捉了)"""
    bmi_dict = {18.8: '过轻', 25: '正常', 28: '过重', 32: '肥胖', float('inf'): '过于肥胖'}
    # float('inf')表示无穷大
    bim_value = float(weight) / float(height) ** 2
    for i in bmi_dict.keys():
        if i > bim_value:
            return bim_value, bmi_dict[i]


info_height = input('请输入您的身高(m)：')
info_weight = input('请输入您的体重(kg)：')
(bim_value, health_condition) = (bmi_2(info_height, info_weight))
print('您的BMI是{0:.2f}，您当前指标为“{1}.”'.format(bim_value, health_condition))
