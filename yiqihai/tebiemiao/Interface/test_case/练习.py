# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : 练习.py
# Author       : 大壮
# Create time  : 2020-02-12 08:58
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end=' ')
#     print()

a = [1, 4, 68, 764, 321, 3, 76, 97, 79, 9, 61, 231, 37, 89, 46, 132]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
