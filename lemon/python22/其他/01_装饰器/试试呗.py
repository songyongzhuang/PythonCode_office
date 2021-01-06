"""
Project      : python22
Current file : 试试呗.py
Creator      : Administrator
Create time  : 2019-08-22 14:00
IDE          : PyCharm
"""



username = '糗事芒果树屋5'

# 步长为正数：从左往右
# 步长为负数：从右往左


print(username[0:-1])  # 糗事芒果

print(username[1:4:2])  # 事果

print(username[1:5:2])  # 事果

print(username[1:-1:1])  # 事芒果屋 -1就是最后一个不包含，

# print(username[1:-1:0])  # 步长不能为零，默认为一

print(username[::-1])  # 步长为负一，则是倒序

print(username[1::2])  # 取偶数位2/4/6
print(username[::2])  # 取奇数位1/3/5
print(username[::-2])  # 倒序取奇数位1/3/5
print(username[-2::-2])  # 倒序取偶数位2/4/6
# 指令不明，编程语言最忌讳
# print(username[4:0:1])  # 错误也不报错 先看四比零大，只能从右往左取值，再看步长是1从左往右取值，他就不知道往哪里取值了

print(username[1:4:-1])  # 也是什么都不打印
print(username[1:4:1])  # 事芒果

print(username[1:4000:1])  # 超出范围，尽我所能，一直取值
# print(username[1000])  # 索引超出范围，就报错

# 步长：默认是1，如果是正数，那么方向是从左到右
# [4:0:-1]  比较前面的部分和步长，如果他们方向冲突就不打印任何数据
# 看方向：整数：从左向右，负数：从右向左
# 先比较开始值和结束值，

print(username[0:8:-2])

