# -*- coding:utf-8 -*-
# @Time   : 2019/8/29 20:39
# @Author : caoyq
# @Email  : 1456039626@qq.com
# @File   : homework6.py

# 1.求三个整数中的最大值
# 提示：三个整数使用input提示用户输入

num = input('请输入第一个整数：')
num_01 = input('请输入第二个整数：')
num_02 = input('请输入第三个整数：')
if num.isdigit() and num_01.isdigit() and num_02.isdigit(): # 判断输入值是否为数字
    if int(num) > int(num_01) and int(num) >= int(num_02): # 两两之间判断大小
        print('最大值为：{}'.format(num))
    elif int(num) >= int(num_01) and int(num) < int(num_02):
        print('最大值为：{}'.format(num_02))
    elif int(num) >= int(num_02) and int(num) < int(num_01):
        print('最大值为：{}'.format(num_01))
    else:
        print('三个数相等，请重新输入')
else:
    print('请输入符合规范的整数')


# 2.分别使用for和while打印九九乘法表

# for
for i in range(1,10):      # i=1, i=2    i=3
    for j in range(1,i+1): # j=1  j=1,2  j=1,2,3  遍历取值后，依次相乘
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print('')
#
# while
i=0
while i < 10:
    j =1
    while j <= i:
        print('{}*{}={}'.format(j,i,i*j),end='\t')
        j += 1
    print()
    i+=1

# 3、你的微信好友当中有 5 个推销的，他们存在一个列表中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# black_list.clear()
# print(black_list)
for person in black_list[:]:  # 遍历列表中的每个元素
    black_list.pop()  # 依次删除最后一个元素
print(black_list)



# 4.使用循环实现排序算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]
for i in range(1,len(a)):
    for j in range(0,len(a)-i): # 经过依次比较后，下轮就减少一个数比较
        if a[j]>a[j+1]:  # 前个和后者比较，如果前者大于后者，交换位置，依次比较，直到最大数排在最后
           a[j],a[j+1]=a[j+1],a[j]
print(a)


# 5. 编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best
def login(name,pwd): # 定义一个登录函数，接受用户输入用户名和密码作为参数
    if name =='lemon' and pwd == 'best':  # 条件判断
        print('登录系统成功')
    else:
        print('用户名或密码错误')
name = input('请输入用户名:')
pwd = input('请输入密码:')
login(name,pwd)  # 函数调用








