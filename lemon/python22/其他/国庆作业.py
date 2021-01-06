# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 国庆作业.py
# Author       : Administrator
# Create time  : 2019-09-29 14:33
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# 3.编写如下程序
# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）

#
# def dafd(deposit, expect):
#     A = 0  # 年
#     B = deposit  # 10000存的钱
#     while B < expect:
#         b = B * 0.0352
#         B += b
#         A += 1
#
#     return f'{A}年'
#
#
# print(dafd(1000, 2000))


# 21、简答题分值5
# 编写如下程序
# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出
# 提示：
# a、1!等于 1
# b、2!等于 1 * 2
# c、3!等于 1 * 2 * 3
# d、n!等于 1 * 2 * 3 * ... * n

def is_int(int_num):
    """ check whether int_num is integer! """

    if isinstance(int_num, str):  # 判断是否为字符串类型

        if int_num.isdigit():
            return True
        else:
            return False
    elif isinstance(int_num, int): # 判断是否为整数类型
        return True
    else:
        return False


def count_factorial(one_num):
    """ count one_num's fatorial """

    result = 1

    if one_num < 0:
        print("{}为负数，没有阶乘！".format(one_num))
        return None

    elif one_num in (0, 1):
        return 1

    else:
        for i in range(1, one_num + 1):
            result *= i

        return result


input_num = input("请输入一个正整数：")

if is_int(input_num):

    input_num = int(input_num)

    print("{}的阶乘为：{}".format(input_num, count_factorial(input_num)))

else:

    print("输入的{}有误，请输入一个正整数!".format(input_num))











