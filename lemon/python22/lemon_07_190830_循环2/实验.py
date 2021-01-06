# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 实验.py
# Author       : 大壮
# Create time  : 2019-08-31 17:59
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# list_02 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# # print(list_02.)
# print(list_02)
#
# a = 1.5
# print(type(a))

# nums = []
# for var in range(1, 4):
#     nums.append(int(input(f'请输入第{var}个数: ')))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1-i):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(f"最大数为{nums[len(nums)-1]}")

# #
# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}\t', end='')

# def exchange_01(a, b):
#     count = a
#     a = b
#     b = count
#     return a, b
#
#
# data_a = input('请输入第一个变量：')
# data_b = input('请输入第二个变量：')
# data_c = exchange_01(data_a, data_b)
# print(f'两个变量的交换结果为：{data_c}')

# def data(b):
#     # if b == 0:
#     #     return '退出循环'
#     # elif 0 < b < 6:
#     #     return f'今天是周{b}'
#     # elif b == 6 or b == 7:
#     #     return '今天是周天'
#     # else:
#     #     return '“输入有误，请重新输入！”'
# #     if b == 0:
# #         return '退出循环'
# #     elif 0 < b <= 7:
# #         if b >= 6:
# #             return '周末'
# #         else:
# #             return f'周{b}'
# #     else:
# #         return '“输入有误，请重新输入！”'
# #
# #
# # while True:
# #     int_b = int(input('请输入1-7七个数字, 分别代表周一到周日, 输入0，退出循环：'))
# #     int_b2 = data(int_b)
# #     if int_b2 == '退出循环':
# #         print('退出循环')
# #         break
# #     else:
# #         print(int_b2)


def bmi_01(stature, weight):
    bmi = weight / stature ** 2
    if bmi < 18.5:
        return '过轻'
    elif 18.5 < bmi <= 25:
        return '正常'
    elif 25 < bmi <= 28:
        return '过重'
    elif 28 < bmi <= 32:
        return '过于肥胖'
    else:
        return '严重肥胖'


while True:
    stature_m = float(input('请输入您的身高:米(m)：'))
    weight_kg = float(input('请输入您的体重:公斤(kg)：'))
    g3 = bmi_01(stature=stature_m, weight=weight_kg)
    if g3 == '正常':  # 直到用户输入正常值就退出
        print(g3)
        break
    else:
        print(g3)
