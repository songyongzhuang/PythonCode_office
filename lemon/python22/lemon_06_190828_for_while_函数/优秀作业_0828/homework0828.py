#-*- coding:utf-8 -*-
#@Time: 2019/8/2912:37
#@Author:深圳+朱朱+python22
#@File:homework0828.py
#@Software: PyCharm


#Q1求三个整数中的最大值
number1 = int(input("请输入第一个整数: "))
number2 = int(input("请输入第二个整数: "))
number3 = int(input("请输入第三个整数: "))
max_number = 0
if number1 > number2:
    max_number = number1
    if number1 > number3:
        max_number = number1
    else:
        max_number = number3
else:
    max_number = number2
    if number2 > number3:
        max_number = number2
    else:
        max_number = number3
print("{},{},和{}中最大数为{}".format(number1,number2,number3,max_number))


#Q2：分别使用for和while打印九九乘法表
#for循环实现
for i in range(1, 10):  #控制行数
    for j in range(1, i+1): #控制列数
        print("{} * {} ={}".format(j, i, i*j), end="\t")  #设置print的end参数，使其不换行
    print("")

#while循环实现
i = 1
while i < 10:
    for j in range(1, i+1):
        print("{} * {} ={}".format(j, i, i*j), end="\t")
    print()
    i += 1


#Q3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机'], 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。

#使用pop方法
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in range(len(black_list)):
    to_del_item = black_list.pop()   #默认删除最后一个元素
    print("正在删除的人是：{}".format(to_del_item))
print("列表最终结果为{}".format(black_list))


#使用del方法
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in range(len(black_list)):  # 控制循环次数
    print(i)
    del black_list[0]   # 每次删除第一个元素
print("列表最终结果为{}".format(black_list))

#Q4：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a = [1,7,4,89,34,2]
n = len(a)
for x in range(n-1):
    for y in range(n-1-x):
        if a[y] > a[y+1]:
            a[y], a[y+1] = a[y+1], a[y]  # 交换位置
print("列表从小到大排序结果为：{}".format(a))


#Q5：从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。a.定义一个函数，接收用户输入的用户名和密码作为参数b.正确的账号，用户名为lemon，密码为best
#定义函数
def checkinfo(username, pwd): # username,pwd形参
    if username == "lemon":
        if pwd == "best":
            print("登陆系统成功")
        else:
            print("您输入的密码错误")
    else:
        print("您输入的用户名错误")

username = input("请输入您的用户名：")
pwd = input("请输入您的密码：")
#调用函数
checkinfo(username, pwd)  # username,pwd实参，函数定义传来几个参数，调用函数也需要传多少个参数