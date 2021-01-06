#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Datetime: 2019/8/28 22:37
@Author: 波哥
@Email: 1209879943@qq.com
@File : Boge_homework_0828.py
@Software: PyCharm
"""

"""
1、求三个整数中的最大值
提示：三个整数使用input提示用户输入
"""
# 方法一，sort函数
nums = []
for i in range(1, 4):
    nums.append(int(input(f'请输入第{i}个数: ')))
nums.sort()
print(f"最大数为{nums[2]}")

# 方法二，max函数
nums = []
for i in range(1, 4):
    nums.append(int(input(f'请输入第{i}个数: ')))
num_max = max(nums)
print(f"最大数为{num_max}")


# 方法三,函数


def cmp_num(a, b, c):
    """判断最大值"""
    if a.replace('-', '', 1).isdigit() \
            and b.replace('-', '', 1).isdigit() \
            and c.replace('-', '', 1).isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        if a <= b and c <= b:
            return b
        elif c <= a and b <= a:
            return a
        elif a <= c and b <= c:
            return c
    else:
        return "输入数据有误"


while True:
    num_one = input("请输入第一个数：")
    num_two = input("请输入第二个数：")
    num_three = input("请输入第三个数：")
    ret = cmp_num(num_one, num_two, num_three)
    if isinstance(ret, int):
        print(f"最大数为{ret}")
        break
    else:
        print("输入数据不合法，请重新输入")

# 方法四，排序
nums = []
for var in range(1, 4):
    nums.append(int(input(f'请输入第{var}个数: ')))
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(f"最大数为{nums[len(nums) - 1]}")

# 方法五，try except
while True:
    num_one = input("请输入第一个数：")
    num_two = input("请输入第二个数：")
    num_three = input("请输入第三个数：")
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        num_three = int(num_three)
        if num_one >= num_two and num_one >= num_three:
            print(f"最大数为{num_one}")
        elif num_two >= num_one and num_two >= num_three:
            print(f"最大数为{num_two}")
        elif num_three >= num_one and num_three >= num_two:
            print(f"最大数为{num_three}")
        break
    except ValueError as e:
        print(f"错误信息为{str(e)}")
        print(f"数据不合法，请重新输入！")

"""
2、分别使用for和while打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
1 * 1 = 1	
1 * 2 = 2    2 * 2 = 4	
1 * 3 = 3    2 * 3 = 6     3 * 3 = 9	
1 * 4 = 4    2 * 4 = 8     3 * 4 = 12    4 * 4 = 16	
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25	
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36	
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49	
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64	
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
"""
# for循环
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d\t" % (j, i, j * i), end='')
    print(end='\n')

# while循环
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d * %d = %d\t" % (j, i, j * i), end='')
        j += 1
    print(end='\n')
    i += 1

"""
3、你的微信好友当中有 5 个推销的，他们存在一个列表 
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空
"""
# 方法一,切片复制
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in black_list[:]:
    black_list.remove(i)
print(black_list)

# 方法二，浅拷贝
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in black_list.copy():
    black_list.remove(i)
print(black_list)

# 方法三,深拷贝
import copy

black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in copy.deepcopy(black_list):
    black_list.remove(i)
print(black_list)

"""
4、使用循环实现排序算法
提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），
不能使用sort、sorted等内置函数或方法
"""


def sort_fun(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li[len(li) - 1]


a = [1, 7, 4, 89, 34, 2]
result = sort_fun(a)
print(result)

"""
5、编写如下程序
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""


def log_on_fun(uname, pwd):
    """判断用户名密码是否正确，从而给予不同的返回值"""
    if uname == 'lemon' and pwd == 'best':
        return "登录系统成功!"
    else:
        return "用户名或密码错误,请重新输入!"


# 增加一个次数统计，限制用户尝试次数
count = 4
while True:
    user_name = input("请输入用户名：")
    passwd = input("请输入密码：")
    ret = log_on_fun(user_name, passwd)
    if ret == '登录系统成功!':
        print(ret)
        break
    else:
        if count > 0:
            print("用户名或密码错误，你还有{}次机会！".format(count))
        count -= 1
        if count == -1:
            # 第五次输入不成功，给予用户提示，并跳出循环
            print("账户被锁定，请联系管理员！")
            break
