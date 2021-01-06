# -*- coding:utf-8 -*-

# 4、使用循环实现排序算法：
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法

print("*" * 20 + "方法一" + "*" * 20)
# 定义列表
a = [1, 7, 4, 89, 34, 2]
# 获取列表长度
b = len(a)

for i in range(b):
    # 设最小元素下标
    min_num = i
    for j in range(i+1, b):
        if a[j] < a[min_num]:
            # 找到最小元素下标
            min_num = j
    # 每2个元素交换位置，小的在前，大的在后
    a[min_num], a[i] = a[i], a[min_num]
print(a)

print("*" * 20 + "方法二" + "*" * 20)
# 定义列表
list_test = [1, 7, 4, 89, 34, 2]
# 获取列表长度
nums = len(list_test)
# 定义空列表
mid_list = []

for j in range(nums):
    # 将列表中最小的数赋值给number_min
    number_min = min(list_test)
    # 将列表中最小的数删除
    list_test.remove(number_min)
    # 将最小的数添加到空列表中
    mid_list.append(number_min)
# 复制列表
list_test = mid_list[:]
print(list_test)