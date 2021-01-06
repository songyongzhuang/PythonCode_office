# -*- coding：utf-8 -*-
# 时间 ：2019-08-31 22:10
# 作者：小白

'''
a.用户输入1-7七个数字，分别代表周一到周日

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”

思路：1。定义函数来实现输入数字到周几的转换
     2。用while实现多次输入，当输入不为0时，执行循环体。为0时，退出程序
     3。用if做输入结果是否的判断
'''


# 定义digit_to_week函数来进行数字到周几的转换
def digit_to_week(number):
    digit = {"1": "周一", "2": "周二", "3": "周三", "4": "周四", "5": "周五", "6": "周末", "7": "周末"}  # 用字典将数字和周几进行一一对应
    if number in digit.keys():  # 判断number是否在字典的key值里，在的话，输出对应的value值，得到周几
        week = digit[number]
    return week  # 返回week


input_number = input("请输入数字1-7（输入0退出）：")  # 用户输入

while input_number != "0":  # while循环，当输入不为0时，执行循环体，当输入为0时，跳出循环。实现退出程序
    if input_number not in ['1', '2', '3', '4', '5', '6', '7']:  # 判断输入值不为1-7，则让用户重新输入
        input_number = input("输入有误，请重新输入数字1-7（输入0退出系统）:")
    else:
        output_week = digit_to_week(input_number)  # 当用户输入为1-7时，调用函数
        print("输入数字对应的是：{}".format(output_week))  # 打印
        input_number = input("请输入数字1-7（输入0退出）：")  # 用户输入新的值
print("退出系统")  # 当用户输入为0时，打印退出系统。
