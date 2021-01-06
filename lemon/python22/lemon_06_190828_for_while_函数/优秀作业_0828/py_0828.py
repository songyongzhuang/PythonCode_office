# _*_ coding: utf-8 _*_ 
# @Time :2019/8/29 16:11
# @Author :beibei
# @Email :253238234@qq.com
# @File :py_0828.py
# @Software:PyCharm

#1.求三个整数中的最大值
#方法一：
def three_num():
    one = int(input("输入第一个数："))
    two = int(input("输入第二个数："))
    three = int(input("输入第三个数："))
    result = one
    if two>result:
        result = two
    if three>result:
        result = three
    return result
print("三个整数中最大值：{}".format(three_num()))
#方法二：
max_num=[]
for num in range(3):
    n=int(input("请输入数字：".format(num+1)))
    max_num.append(n)
print("三个整数中最大值是:{}".format(max(max_num)))


#2.分别使用for和while打印九九乘法表
#for循环
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s'%(j,i,i*j),end=' ')
    print("\t")
#while循环
j=1
while j<=9:
    i = 1
    while i<=j:
        print('%s*%s=%s' % (i, j, i * j), end="\t")
        i+=1
    print(' ')
    j+=1

#3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
black_list=['卖茶叶','卖面膜','卖保险','卖花生','卖手机']
while black_list:
    black_list.clear()
    print(black_list)


#4.使用循环实现排序算法 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]
for n in range(len(a)):
    for m in range(len(a)-1):
        if a[m]>a[n]:
            a[m],a[n]=a[n],a[m]
print(a)

#5. .编写如下程序
#从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
#a.定义一个函数，接收用户输入的用户名和密码作为参数
#b.正确的账号，用户名为lemon，密码为best
#方法一
d={"name":"lemon","pwd":"best"}
name = input("请输入用户名：")
pwd = input("请输入密码：")
if name == d["name"] and pwd == d["pwd"]:
    print("登录系统成功")
else:
    print("用户名或密码错误")
#方法二
def a():
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name == d["name"] and pwd == d["pwd"]:
        return ("登录系统成功")
    else:
        return ("用户名或密码错误")
d={"name":"lemon","pwd":"best"}
print(a())