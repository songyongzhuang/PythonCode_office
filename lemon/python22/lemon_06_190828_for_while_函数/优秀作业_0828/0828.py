#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:li_ma
# datetime:2019/8/29 16:56
# file: 0828.py


# 1.求三个整数中的最大值
# 提示：三个整数使用input提示用户输入
# 定义conpare_num函数 输入比较的数字个数 不输入默认为3次
def compare_num(count=3):
    """
    :param count:  输入比较的数字个数 不输入默认为3次
    :return:
    """
    list_max_num = []  # 定义列表存储输入的数
    print('请输入{}个整数，输出最大的数'.format(count))
    for i in range(1, count + 1):  # 输入几个数 循环几次
        while True:  # 提示用户输入，如果输入符合规则跳出循环进入下个输入 否则一直提示输入
            str_iput = input('请输入第{}个数： '.format(i))
            if str_iput.isdigit():  # 如果是整数
                int_iput = int(str_iput)  # 转换为int类型
                list_max_num.append(int_iput)  # 添加到list_max_num列表中
                break
            else:
                print('输入的不是整数，请重新输入第{}个数'.format(i))
    print('输入的{}里面最大的数是{}'.format(list_max_num, max(list_max_num)))  # man（列表）返回列表最大值


# 调用定义好的compare_num方法
compare_num()

# 2.分别使用for和while打印九九乘法表
# 提示：输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
# 1 * 1 = 1
# 1 * 2 = 2    2 * 2 = 4
# 1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
# 1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
# 1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
# 1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
# 1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
# 1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
# 1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
# 1.for循环实现
for i in range(1, 10):  # 外层循环定义打印打印行数
    for j in range(1, i + 1):  # 第二层循环定义打印打印列数
        print('{} * {} = {}'.format(j, i, i * j), end='\t')  # 循环打印从1 到i的乘法 输出不回车
    print()  # 打印一行后回车

# while 循环实现
i = 1  # 定义被乘数初始值i为1
while i <= 9:  # 被乘数最大值
    j = 1  # 二层循环进来后乘数默认值为1
    while j <= i:  # 乘数小于等于被乘数进入该层循环
        print('{} * {} = {}'.format(j, i, i * j), end='\t')  # 乘数j从1开始 直到输出至于被乘数i一致后终止循环
        j += 1  # 每次循环乘数+1
    print()  # 第二层循环结束后打印回车
    i += 1  # 第二层循环结束后，被乘数+1

# 3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
#  当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。

# 方法1 循环
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
while len(black_list) > 0:
    black_list.remove(black_list[0])
print(black_list)

# 方法二 clear方法
black_list.clear()
print(black_list)


# 4.使用循环实现排序算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
def ascending_order(order_list):
    '''
    :param order_list:
    :param list:  传入list 将list升序排列
    '''
    length_list = len(order_list)
    for i in range(length_list):  # 第一层循环 列表长度有多少就需要循环比较多少次 把最大的数往后排
        break_flag = False  # 结束循环标志位，如果第二层循环未走进，跳出循环，无需再比较，优化性能
        # 第二层循环 前次循环已经把较大的数排在后面，所以用列表长度减去上次循环的次数，列表后面的数已经最大 不用再次循环比较
        for j in range(length_list - i - 1):
            if order_list[j] > order_list[j + 1]:
                order_list[j], order_list[j + 1] = order_list[j + 1], order_list[j]  # 不需要借助第三方变量 直接交换两个元素的值
                break_flag = True  # 标志位置位True 说明排序未完成 继续循环
        print('第{}次循环，列表为{}'.format(i, order_list))
        if not break_flag:  # 如果第二层循环代码没走，说明已经顺序已经排好，无需继续比较大小 直接跳出循环
            break


a = [1, 7, 4, 89, 34, 2]
ascending_order(a)  # 调用ascending_order函数 将列表a传进去
print(a)


# 5. .编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best
def login(user_name, user_pwd):  # 定义login函数 根据传入的用户名密码 判断传入的是否正确 并返回True或False
    """
    :param user_name:  用户名
    :param user_pwd:   密码
    :return:
    """
    account_info = {'user_name': 'lemon', 'user_pwd': 'best'}  # 定义用户名密码存储字典
    if (account_info['user_name'] == user_name) and (account_info['user_pwd'] == user_pwd):
        return True  # 如果用户名密码正确，返回True
    else:
        return False  # 如果用户名密码不正确，返回False


limit_count = 3  # 输入限制次数
for i in range(1, limit_count + 1):  # 循环3次
    user_name = input('请输入用户名： ')
    user_pwd = input('请输入密码： ')
    if login(user_name, user_pwd):  # 调用login方法 如果用户名密码都输入正确 跳出循环
        print('登录系统成功!')
        break
    else:
        if limit_count - i > 0:  # 最后1次录入错误不需要打印还可录入次数
            print('用户名或密码错误,请重新输入，还可输入{}次'.format(limit_count - i))
    if i == 3:
        print('用户名或密码错误,输入超过限制，程序退出')
