# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 作业模拟操作的地方.py
# Author       : 大壮
# Create time  : 2019-08-24 09:49
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# A = []
# for i in range(3):
#     temp = input('请输入要添加的学生姓名:')
#     A.append(temp)
#     for tempName in A:
#         pass
# print(tuple(A))


# a = {'姓名': '哈哈', '性别': '男', '年龄': '18', '身高': '1880', '联系方式': '159', '花名': '小花'}
#
# while True:
#     key = input('猜猜看有没有键')
#     if key in a.keys():
#         print("有这个键")
#         break
#     elif key == 1:
#         print('')
#     else:
#         print("没有这个键从新输入")

# if int(number) >= 3:
#     for i in range(int(number)):  # range() 循环三次
#         temp = input('请输入要添加的兴趣:')
#         new_like.append(temp)  # 列表操作：append末尾追加
# else:
#     print("输入数据有误请重新输入")
#
#     print(new_like)
# number = (input("请输入需要填写兴趣的项数："))
# new_like = []  # 先新建一个空列表

# while True:
#     number = (input("请输入需要填写兴趣的项数："))
#     if number.isdigit() is True:
#         print('---------')
#         break
#     else:
#         print('输入错误，请输入正整数\n')

# 一、.删除如下列表中的"矮穷丑"，写出能想到的所有方法
# info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 1、根据值删除, 使用remove方法.
# info.remove("矮穷丑")  # 直接输入删除的"矮穷丑".
# print(info)

# 2、根据索引删除, 使用pop方法, 根据索引删除元素.
# print('删除的是：', info.pop(info.index("矮穷丑")))  # 1.使用index()求出索引, 2.根据索引删除并打印元素.
# print(info)

# 3、del 通过索引删除
# del info[info.index("矮穷丑")]  # 根据索引删除
# print(info)

# print(li2.values())  # 返回的是：值
# dict_values(['二狗子', '不详', '未知'])


# li2 = {'姓名': '二狗子',
#        '性别': '不详',
#        '年龄': '未知'}
# li2.update({"Stature": 175, "Tel": 13520183747})
# print(li2)


personal = {'姓名': '二狗子', '性别': '男', '年龄': 'age'}
print(personal.get('没有的key', '没有找到'))  # 没有找到返回默认值
print(personal.get('姓名'))  # 找到返回值：二狗子


