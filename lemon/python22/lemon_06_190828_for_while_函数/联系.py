# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习练习.py
# Author       : 大壮
# Create time  : 2019-08-29 20:49
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


arr = [9, 7, 4, 89, 34, 2]
length = len(arr)  # 查看列表的长度
for i in range(length):  # 判断最外圈的循环次数 控制跑多少次
    for j in range(length - 1):  # 每循环一次可以判断出一个最大值，两两比较需要长度减去 1, 循环一次i递增，减去i
        if arr[j] > arr[j+1]:  # 判断当前索引值的值是否大于后面的值  如：9 > 7
            tmp = arr[j]       # 创建一个变量用来储存当前索引的值(现在索引的值是大于后面索引的值) 如：变量a = 9
            arr[j] = arr[j+1]  # 判断后把后面的值交给前面的值 如：赋值前 9 = 7  赋值后就是 7 = 7
            arr[j+1] = tmp     # 把大的值在交给后面的索引值 如：赋值前 7 = 9 赋值后就是 9 = 9

print(f'排序后的循序为：{arr}')

