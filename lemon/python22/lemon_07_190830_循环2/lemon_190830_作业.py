# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190830_作业.py
# Author       :
# Create time  : 2019-08-31 15:38
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# 一.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。


# 第一种


def int_data(a):
    if a == 1:
        return '周一'
    elif a == 2:
        return '周二'
    elif a == 3:
        return '周三'
    elif a == 4:
        return '周四'
    elif a == 5:
        return '周五'
    elif a == 6 or a == 7:
        return '周末'
    else:
        return '“输入有误，请重新输入！”'


while True:
    figure = int(input('请输入1-7七个数字, 分别代表周一到周日, 输入0，退出循环：'))
    if figure == 0:
        print("退出循环")
        break
    else:
        print(int_data(figure))


# 第二种
def data(b):
    # if b == 0:
    #     return '退出循环'
    # elif 0 < b < 6:
    #     return f'今天是周{b}'
    # elif b == 6 or b == 7:
    #     return '今天是周天'
    # else:
    #     return '“输入有误，请重新输入！”'
    if b == 0:
        return '退出循环'
    elif 0 < b <= 7:
        if b >= 6:
            return '周末'
        else:
            return f'周{b}'
    else:
        return '“输入有误，请重新输入！”'


while True:
    int_b = int(input('请输入1-7七个数字, 分别代表周一到周日, 输入0，退出循环：'))
    int_b2 = data(int_b)
    if int_b2 == '退出循环':
        print('退出循环')
        break
    else:
        print(int_b2)


# 二、列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# 第一种
list_01 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
print(set(list_01))  # 强制转换成集合


# 第二种
list_01 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
list_02 = []
for i in list_01:
    if i not in list_02:
        list_02.append(i)
print(list_02)


# 三、将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。
# 第一种
def exchange(a, b):
    a, b = b, a
    return a, b


data_a = input('请输入第一个变量：')
data_b = input('请输入第二个变量：')
data_c = exchange(a=data_a, b=data_b)
print(f'两个变量的交换结果为：{data_c}')


# 第二种
def exchange_01(a, b):
    count = a
    a = b
    b = count
    return a, b


data_a = input('请输入第一个变量：')
data_b = input('请输入第二个变量：')
data_c = exchange_01(a=data_a, b=data_b)
print(f'两个变量的交换结果为：{data_c}')

# 四、编写如下程序
# 尝试函数部分封装：
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5:过轻、18.5-25:正常、25-28:过重、28-32:过于肥胖、32:严重肥胖


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
