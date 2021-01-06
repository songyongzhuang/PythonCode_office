#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/8/30 11:23
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


"""
1.求三个整数中的最大值

提示：三个整数使用input提示用户输入
"""

# 解题思路
"""
1，接受用户输入信息：
2，第一个数字和第二个数字比较，得到最大值 old_max
3， 第三个数字和最大值比较，得到新的最大值。new_max
4, 第四个和最大，
5， 5 ， 最大值
=
"""

# def run():


# max_num = a
# for num in [a, b, c]:
#     if max_num < num:
#         max_num = num
#
#     # else: 可以省略
#     #     pass
# print(max_num)


# a = int(input("第一个整数："))
# b = int(input("第二个整数："))
# c = int(input("第三个整数："))
# 异常处理：错误按照我们的思路去运行。
# 第一步：先解决问题。
# if a > b :
#     max_num = a
# else:
#     max_num = b
#
# if max_num > c:
#     max_num_new = max_num
# else:
#     max_num_new = c
# print(max_num_new)


# 很多很多数，：重复的运行过程。比较操作
# max_num = a
# for num in [a, b, c]:
#     if max_num < num:
#         max_num = num
#     # else: 可以省略
#     #     pass
# print(max_num)


# def maxize(a, b, c):
#     max_num = a
#     for num in [a, b, c]:
#         if max_num < num:
#             max_num = num
#     return max_num
#
#
# maxize(3, 6, 8)
# # input


# 不要着急写代码，用笔先把思路写清楚。
# 1, 先比较第一个和第二个，得到最大值；再和第三个相比较
# 输入得到 3 个数
# a = int(input("第一个整数："))
# b = int(input("第二个整数："))
# c = int(input("第三个整数："))
# 50


# 方法一：if
# if a > b:
#     max_num = a
# else:
#     max_num = b
#
# if c > max_num:
#     max_num = c
#
# print(max_num)


# # 方法二：每一个元素都要比较
# # 每次都是和前面的最大值比较：和语言是没有关系的。
# # 没有任何数据比较，max_num = a
# max_num = a
# for num in [a, b, c]:
#     if num > max_num:
#         max_num = num
# print(max_num)

# # 方法三：while
# max_num = a
# nums = [a, b, c]
# index = 0
# while index < len(nums):
#     if nums[index] > max_num:
#         max_num = nums[index]
#     index += 1
# print(max_num)

# 函数
# def maxize(nums):
#     max_num = nums[0]
#     for num in nums:
#         if num > max_num:
#             max_num = num
#     return max_num
# maxize([a, b, c])

"""
2.分别使用for和while打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
1 * 1 = 1
1 * 2 = 2    2 * 2 = 4
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72   9 * 9 = 81
"""

# 思路 for,
# for first in range(1, 10):
#     print() # 换行。
#     for two in range(1, 10):
#         if two  <= first:
#             print("{} * {} = {}".format(two, first, two * first), end='\t')


# for num in range(1, 10):
#     for rest_num in range(1, 10):
#         if rest_num <= num:
#             print('{} * {} = {}'.format(rest_num, num, rest_num * num), end="\t")
#     print()

# num = 1
# while num <= 9:
#     start = 1
#     while start <= num:
#         print('{} * {} = {}'.format(start, num, start * num), end="\t")
#         start += 1
#     print()
#     num += 1


"""
3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=

['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']

 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
"""
# black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']

# 知识：clear()
#
# black_list.clear()
# print(black_list)

# 每一个都删除，重复的过程。每个元素都要执行删除动作
# for i in black_list:
#     # ['卖面膜', '卖花生', '卖手机']
#     black_list.remove(i)
#     # index + = 2
# print(black_list)


# for i in black_list:
#     # ['卖面膜', '卖花生', '卖手机']
#     black_list.pop()
#     # index + = 2
# print(black_list)
# 一看到运行结果和自己所想的不一样，千万不要慌。
# 你的思路已经对的，细节没有把握好。

# 你的代码水平决定：你自己采坑的数量。自己从里面爬出来多少次。
# 坑。

# 原来的列表变化
# copy
# new_list = black_list[:]
# for i in new_list:
#     black_list.remove(i)
#     # index + 1
# print(black_list)

# 题目，很多很多。
# 不要在列表  for 循环的时候去进行列表的删除， 添加操作
# 维护新的备份。


# 错误形式
# for person in black_list:
#     black_list.remove(person)
# print(black_list)

# for person in black_list[:]:
#     black_list.remove(person)
# print(black_list)

"""
4.使用循环实现排序算法， 非常喜欢出面试题。

提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
"""


# 思路： 冒泡， 选择，
# 小学一年：1 列，

# 第一个：先确定第一个人。。。。 再确定第二个人。


# # 每次选出最小的
a = [1, 7, 4, 89, 34, 2]
# for i in a:

for index_one in range(len(a)-1):
    # 1
    # print(index_one)
    # 最小的的是
    min_index = index_one
    for index_two in range(index_one+1, len(a)):
        if a[index_two] < a[min_index]:
            a[min_index], a[index_two] = a[index_two], a[min_index] # 互换位置
        # print('min', min_index)
print(a)


#
# a = [1, 7, 4, 89, 34, 2]
# for index_one in range(len(a) - 1):
#     for index_two in range(len(a) - index_one - 1):
#         if a[index_two] > a[index_two + 1]:
#             a[index_two], a[index_two + 1] = a[index_two + 1], a[index_two]
# print(a)

# 冒泡，选择

"""
5. .编写如下程序

从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。

a.定义一个函数，接收用户输入的用户名和密码作为参数

b.正确的账号，用户名为lemon，密码为best
"""

# username = input('请输入账号名：')
# pwd = input("请输入密码")
#
#
# def validate(username, pwd):
#     if username == 'lemon' and pwd == 'best':
#         return True
#     else:
#         return False
#
#
# if validate(username, pwd):
#     print("陈工")
# else:
#     print('错误')
