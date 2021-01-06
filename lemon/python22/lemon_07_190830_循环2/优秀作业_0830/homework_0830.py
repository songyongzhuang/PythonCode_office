# 1.编写如下程序
# 尝试函数部分分装：
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

dict = {"1": "周一", "2": "周二", "3": "周三", "4": "周四", "5": "周五", "6": "周末", "7": "周末"}


def func_week(num):
    if num in dict.keys():
        return "{}".format(dict[num])
    elif num == "0":
        return "退出循环"
    else:
        return "输入有误，请重新输入"


while True:
    num = input("请输入1-7七个数字: ")
    if num.isdigit():
        print(func_week(num))
        if int(num) == 0:
            break
    else:
        print("输入不是有效数字，请检查后重新输入")

# 2.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素

list1 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
list2 = list1[:]  # 复制一个列表
for index_one in range(len(list2) - 1):  # 第一个列表索引值
    for index_two in range(index_one + 1, len(list2)):  # 第二个列表索引值
        if list2[index_one] == list2[index_two]:
            if list1.count(list2[index_two]) > 1:  # 如果list1中重复值的个数是大于1的，则可在列表中删除
                list1.remove(list2[index_two])
print(list1)


# 3.将两个变量的值进行交换（a = 100, b = 200）
# 交换之后，a = 200， b = 100， 使用函数。

def swap(a, b):
    a, b = b, a
    return a, b


print(swap(100, 200))


# 4.输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5：过轻      18.5-25：正常       25-28：过重       28-32：肥胖       高于32: 严重肥胖

def fun_bmi(height, weight):
    bmi = float(weight / height ** float(2))
    if bmi < 18.5:
        return "过轻"
    elif 18.5 <= bmi < 25:
        return "正常"
    elif 25 <= bmi < 28:
        return "肥胖"
    else:
        return "严重肥胖"


i = 0
while i < 5:  # 设置循环条件，循环5次程序结束
    height = float(input("请输入你的身高："))
    weight = float(input("请输入你的体重："))
    res = fun_bmi(height, weight)
    print(res)
    i += 1
