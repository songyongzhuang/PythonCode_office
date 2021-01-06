# -*- coding: utf-8 -*-
# @Time     : 2019/8/25 12:52
# @Author   : wolf_eye
# @Email    : 15840995236@163.com
# @File     : homework_0823.py
# @student  : 狼眸

# Q1: 删除如下列表中的"矮穷丑"，写出能想到的所有方法
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# # 方法一：remove()
# info.remove('矮穷丑')
# print(info)
#
# # 方法二：pop()
# info.pop(info.index('矮穷丑'))
# print(info)
#
# # 方法三：del
# del info[info.index('矮穷丑')]
# print(info)
#
# # 方法四：列表切片，去掉"矮穷丑"，再将列表重新拼接
# num = info.index('矮穷丑')
# info_left = info[:num]
# info_right = info[num+1:]
# info_left.append(info_right)
# info = info_left
# print(info)

# 方法五：创建for循环，过滤要删除的元素，生成新的列表重新赋值给原列表
del_str = ['矮穷丑']
new_info = []
for element in info:
    if element not in del_str:
        new_info.append(element)
info = new_info
print(info)


# Q2: 5道小题
# 添加个人信息
info_dict = {}


def info(*args):
    for element in args:
        info_dict[element] = input(f'请输入您的{element}: ')
    print('您当前的个人信息为：', info_dict)


# 删除个人信息
def del_info(*args):
    for element in args:
        del_element = info_dict.pop(element)
        print(f'您的"{element}：{del_element}"信息已删除')
    print('您当前的个人信息为：', info_dict)


# 修改个人信息
def update_info(*args):
    for element in args:
        info_dict[element] = input(f'请输入您要更新的{element}信息：')
    print('您当前的个人信息为：', info_dict)
    while True:
        update_element = input('请输入您要修改的信息（如无需修改请输入“N”）：')
        if update_element == 'N':
            break
        elif update_element not in info_dict.keys():
            print('您要修改的信息不在当前资料中，请重新输入')
        else:
            info_dict[update_element] = input(f'请输入您要更新的{update_element}信息：')
            print('您当前的个人信息为：', info_dict)


# a.某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
info('姓名', '性别', '年龄')

# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
info('身高', '联系方式')

# c, 平台为了保护你的隐私，需要你删除你的联系方式；
del_info('联系方式')

# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
info('花名')
update_info('身高')

# e, 你进一步添加自己的兴趣，至少需要 3 项。一经确定，不可单独修改各个兴趣点。
# 一经确定，不可单独修改各个兴趣点，由题干确定兴趣存储在元组中
print('请至少输入三个兴趣，若三个兴趣输入完成，可选择继续输入兴趣或输入“N”退出：')
number = 1
interest_tuple = ()
while True:
    interest = (input(f'请输入您第{number}个兴趣：'),)
    number += 1
    if number > 4 and interest[0] == 'N':
        break
    else:
        interest_tuple += interest
print('您的兴趣为：', interest_tuple)
info_dict['兴趣'] = interest_tuple
print('您当前的个人信息为：', info_dict)

# Q3： 现在有一个列表 li2=[1，2，3，4，5]
li2 = [1, 2, 3, 4, 5]
# 第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
# 在元素1的索引位置，插入元素0
li2.insert(li2.index(1), 0)
# 在元素4的索引位置，插入元素66
li2.insert(li2.index(4), 66)
# 在列表的末尾添加元素11, 22, 33
li3 = [11, 22, 33]
# li2 += li3
li2.extend(li3)
print('元素添加完成的列表li2为', li2)

# 第二步：对li2进行排序处理
li2.sort(reverse=True)
print('li2降序输出：', li2)
li2.sort()
print('li2.sort()默认升序输出：', li2)

# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# remove根据元素值进行删除，删除列表中第一个找到的元素，不会返回该元素值，只支持单个元素删除
li2.remove(0)
print('删除元素0：', li2)
# pop根据索引位置删除元素，并返回该元素值，只支持单个元素删除
li2.pop(0)
print('删除索引位置0的元素：', li2)
# del根据索引位置删除元素,可支持批量删除
del li2[0]
print('删除索引位置0的元素：', li2)
del li2[:2]
print('批量删除索引位置0-1的元素：', li2)
# 清空列表,结果为空列表
li2.clear()
print('clear清空列表：', li2)
# del可以删除整个列表，删除会清空列表的内存
try:
    del li2
    print(li2)
except Exception as err:
    print('del列表会清空列表的内存')
    raise err
