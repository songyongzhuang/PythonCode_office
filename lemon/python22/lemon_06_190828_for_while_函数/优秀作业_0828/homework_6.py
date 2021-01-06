# _*_ coding: UTF-8 _*_
# @Time     :2019-08-29 09:18
# @Author   :清莲
# @FileName :homework_6.py
# @Software :PyCharm
# 题一：求出三个整数中的最大值
list = []
i = 0
print("输入三个整数，最后返回你最大的数字～")
while i != 3:
    try:
        num = int(input())
        list.append(num)
        i += 1
    except:
        print("请输入整型数字")
print("最大的数字是", max(list))

# 题二：打印九九乘法表
print("\n九九乘法表：")
i = 1
while i != 10:
    j = 1
    while j <= i:
        print("{0} * {1} = {2}".format(j, i, i * j), end='\t')
        j += 1
    print()
    i += 1

# 删除列表中元素
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
black_list.clear()

"""第二种方法
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
del black_list
black_list = []
"""

"""第三种方法：我猜实际希望操作为通过循环一个一个删除
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in range(black_list.__len__()):
    black_list.pop()
"""


# 题四：使用循环实现排序
# 经典排序算法：冒泡、选择、插排、归并、希尔、快排、堆排，我就写三个最基础的吧


def bubbleSort(arr):  # 冒泡
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSort(arr):  # 选择
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


def insertionSort(arr):  # 插排
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr


a = [1, 7, 4, 89, 34, 2]
print("\n排序后的a：", bubbleSort(a))


# 题五：定义函数判断是否登录成功
def setUp(user, password):
    if user == 'lemon' and password == 'best':
        print("登录系统成功")
    else:
        print("用户名或密码错误")


user = input("\n用户名：")
password = input("密码：")
setUp(user, password)
