#-*- coding:utf-8 -*-
# datetime:2019/8/28
# author: 佳媛


# 1.求三个整数中的最大值
# 提示：三个整数使用input提示用户输入
try:
    a = int(input("请输入第一个整数："))
    b = int(input("请输入第二个整数："))
    c = int(input("请输入第三个整数："))
# 方法一 使用列表排序
    #将输入的三个整数放入列表
    int_list = [a,b,c]
    #通过sort进行排序
    int_list.sort()
    #排序后列表最后一个则为最大值
    max_value = int_list[len(int_list) - 1 ]
    print("最大数值为{}".format(max_value))
	
# 方法二 用if语句判断
    if a > b:
        max_value = a
    else:
        max_value = b
    if c > max_value:
        max_value = c
    print("最大数值为{}".format(max_value))
except:
    print("请输入整数哦")

# 2.分别使用for和while打印九九乘法表
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
#
# 1 * 1 = 1
# 1 * 2 = 2    2 * 2 = 4
# 1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
# 1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
# 1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
# 1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
# 1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
# 1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
# 1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81

#for循环实现九九乘法表
#变量用于计数，每循环一次增加一次
a = 2
for i in range(1,10):
    for b in range(1,a):
        print("{} * {} = {}".format(b,i,b * i),end="\t")
    print() #每次跳出小循环都换行
    a += 1
	
#while循环实现九九乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("{} * {} = {}".format(j,i,j*i),end="\t")
        j += 1
    print()
    i += 1

# 3、你的微信好友当中有 5 个推销的，他们存在一个列表
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
#  当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
# 1、直接将列表清除
black_list.clear()
# 2. 你用for循环进行遍历删除
for i in black_list:
    black_list.pop(i)
print(black_list)

# 4.使用循环实现排序算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]
# #求出a列表的长度
 n = len(a)
# 从左到右，数组中相邻的两个元素进行比较，将较大的放到后面。
for i in range(n-1):
    for y in range(n - 1 - i):
        if a[y] > a[y + 1]:
            a[y], a[y + 1] = a[y + 1], a[y]
    print(a)

# 5. .编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best

def login (name , pwd ):
    if name == "lemon" and pwd == "best":
        print("登录成功")
    else:
        print("用户名或密码错误")

name = input("请输入用户名：")
pwd = input("请输入密码：")
login(name,pwd)