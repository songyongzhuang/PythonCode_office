# -*- coding:utf-8 -*-
# @Time :12:18
# @Author :Leon

# 1.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

def isworkday(day):
    workday = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
    if day in workday.keys():
        print(workday[day])
    else:
        print("输入有误，请重新输入!")

while True:
    day = input("请输入0-7，0表示退出：")
    if day == "0":
        print("退出输入")
        break
    isworkday(day)

# 2.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# 1 用新列表装载
a_new = []
for i in a:
    if i not in a_new:
        a_new.append(i)
print(a_new)
print("-------------------")

# 2 列表里对比去重
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            a[j] = 'del'
print(a)
for i in a[:]:
    if i == 'del':
        a.remove(i)
print(a)

# 3 用set方法去重
a = list(set(a))
print(a)


# 3.将两个变量的值进行交换（a = 100, b = 200）交换之后，a = 200， b = 100， 使用函数。
def change(a, b):
    a, b = b, a
    print(f'a = {a}, b = {b}')
change(100, 200)

# 4.编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
def bodybmi(weight, hight):
    bmi = weight/(hight ** 2)
    if bmi < 18.5:
        print("你的BMI指数过低，请加强饮食锻炼")
    elif 18.5 <= bmi < 23.9:
        print("恭喜你！你的BMI指数正常")
    elif 23.9 <= bmi < 27:
        print("你的BMI指数过高，请适当减肥")
    elif 27 <= bmi:
        print("你的BMI指数严重超标了！！！请注意日常饮食习惯")
    else:
        print("计算失败")

while True:
    hight = input("请输入你的身高（m ）：")
    weight = input("请输入你的体重（kg）：")
    if hight.replace('.', '').isdecimal() and weight.replace('.', '').isdecimal():
        weight = float(weight)
        hight = float(hight)
        bodybmi(weight, hight)
        break
    else:
        print("你输入的格式不正确，请重新输入！！！")
