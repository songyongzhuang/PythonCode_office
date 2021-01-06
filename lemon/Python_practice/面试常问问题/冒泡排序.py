# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : 冒泡排序.py
# Author       : 大壮
# Create time  : 2019-11-14 19:53
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
arr = [1, 7, 4, 89, 34, 2]

for i in range(1, len(arr)):  # len(arr) 求出列表长度, 判断可以循环几次
    for j in range(0, len(arr) - i):  # 长度减循环次数, 每次循环可以判断一个最大值
        if arr[j] > arr[j + 1]:  # 列表切片 判断前后数据
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 数据赋值
print(arr)
