# -*- coding: utf-8 -*-
# @Time     : 2019/8/31 13:36
# @Author   : wolf_eye
# @Email    : 15840995236@163.com
# @File     : lemon8_homework_0830.py
# @student  : 狼眸

'''
Q1.编写如下程序
尝试函数部分分装：
a.用户输入1-7七个数字，分别代表周一到周日
b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
c.如果输入0，退出循环
d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
'''


def week_day(num):
    week_dict = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
    if num == '0':
        return True
    elif num in week_dict.keys():
        print(f'{week_dict[num]}')
    else:
        print('输入有误，请重新输入！')
        return False


while True:
    num = input('请输入您要查询1-7中的数字，若输入0退出查询：')
    result = week_day(num)
    if result == True:
        break
    else:
        pass


# Q2： 列表去重，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
def func1(list_repeat):
    '''''
    方法一：集合去重
    '''
    return list(set(list_repeat))


def func2(list_repeat):
    '''''
    方法二：使用字典键去重的方式
    '''
    return {}.fromkeys(list_repeat).keys()


def func3(list_repeat):
    '''''
    方法三：使用列表遍历的方式，将不重复的元素存到新列表中
    '''
    temp_list = []
    for element in list_repeat:
        if element not in temp_list:
            temp_list.append(element)
    return temp_list


def func4(list_repeat):
    '''
    方法四：for遍历列表中元素，对count()若大于1的元素进行删除，不改变列表元素顺序
    '''
    for x in list_repeat:
        while list_repeat.count(x) > 1:
            del list_repeat[list_repeat.index(x)]
    return list_repeat


import itertools


def func5(list_repeat):
    '''
    方法五：itertools.groupby，把迭代器中相邻的重复元素挑出来放在一起，返回连续键和组的迭代器，其中键有去重功能，类似字典
    '''
    list_result5 = []
    list_repeat.sort()
    it = itertools.groupby(list_repeat)
    for k, g in it:
        list_result5.append(k)
    return list_repeat


from functools import reduce


def func6(list_repeat):
    '''
    方法六：reduce函数，用传给 reduce 中的函数 func（有两个参数）先对列表中的第 1、2 个元素进行操作，
    得到的结果再与第三个数据用 func 函数运算
    '''
    list_result6 = []
    func = lambda x, y: x if y in x else x + [y]
    list_result6 = reduce(func, [[], ] + list_repeat)
    return list_result6


list_repeat = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(func1(list_repeat))
print(func2(list_repeat))
print(func3(list_repeat))
print(func4(list_repeat))
print(func5(list_repeat))
print(func6(list_repeat))


# Q3: 将两个变量的值进行交换（a = 100, b = 200）,交换之后，a = 200， b = 100， 使用函数
def change_func1(a, b):
    '''
    方法一：定义函数，直接交换变量位置返回，同a, b = b, a
    '''
    return b, a


def change_func2(a, b):
    '''
    方法二：通过元组解包方式对变量交换赋值，python独有方式，最简单常用方式
    '''
    a, b = b, a
    return a, b


def change_func3(a, b):
    '''
    方法三：引入第三个变量，作为中间值存储进行赋值
    '''
    temp = a
    a = b
    b = temp
    return a, b


def change_func4(a, b):
    '''
    方法四：二进制，异或运算，进行赋值处理，与方法五有相似之处
    '''
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def change_func5(a, b):
    '''
    方法五：不引进第三个变量，通过运算符，完成变量交换
    '''
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = 100
b = 200
a, b = change_func1(a, b)
print(f'第一种方法交换后的a,b值：{a}，{b}')
a, b = change_func2(a, b)
print(f'第二种方法交换后的a,b值：{a}，{b}')
a, b = change_func3(a, b)
print(f'第三种方法交换后的a,b值：{a}，{b}')
a, b = change_func4(a, b)
print(f'第四种方法交换后的a,b值：{a}，{b}')
a, b = change_func5(a, b)
print(f'第五种方法交换后的a,b值：{a}，{b}')

'''
Q4：输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
'''
import re


def legal_info(input_info):
    '''
    判断输入的升高体重是否合法
    '''
    pattern = re.compile(r'^[0-9]+\.?\d*$')
    func_compare = lambda x, y: re.match(x, y)
    if func_compare(pattern, input_info):
        list_info.append(input_info)
    else:
        print('您输入的内容无法识别，请重新输入')


def health_remind(high_info, weight_info):
    '''
    根据入参的身高体重给出检测结果
    '''
    bmi = float(weight_info) / float(high_info) ** 2
    if bmi < 18.5:
        print('您的体重过轻，请多吃肉')
    elif 18.5 <= bmi < 25:
        print('您的体重正常，请保持')
    elif 25 <= bmi < 28:
        print('您的体重过重，请多吃蔬菜')
    elif 28 <= bmi < 32:
        print('您的体重肥胖，请注意锻炼')
    else:
        print('您的体重严重肥胖，可别吃肉了，多锻炼吧')


while True:
    list_info = []
    decide = input('您要参加此次检测么？（参加请输入“Y”，不参加请输入“N”）：')
    if decide == 'Y':
        while len(list_info) < 1:
            high = input('请输入您的身高(m):')
            legal_info(high)
        while len(list_info) < 2:
            weight = input('请输入您的体重(kg):')
            legal_info(weight)
        health_remind(high, weight)
    elif decide == 'N':
        print('您已退出此次检测')
        break
    else:
        print('您输入的内容无法识别，请重新输入')
