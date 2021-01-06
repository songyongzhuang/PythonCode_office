# 1.求三个整数中的最大值 提示：三个整数使用input提示用户输入
while True:
    a = input("请输入第一个整数：")
    b = input("请输入第二个整数：")
    c = input("请输入第三个整数：")
    if a.isdigit() and b.isdigit() and c.isdigit():
        first_num = int(a)
        second_num = int(b)
        third_num = int(c)
        if first_num > second_num:
            max_num = first_num
        else:
            max_num = second_num
        if max_num < third_num:
            max_num = third_num
        print("三个整数中最大的值为{}".format(max_num))
        break
    else:
        print("输入的数字不符合规范，请重新输入")

# 2.分别使用for和while打印九九乘法表

# 方式1：使用for循环
for x in range(1, 10):
    for y in range(1, 10):
        if x > y:
            print("{} * {} = {}\t".format(y, x, x * y), end='')
        elif x == y:
            print("{} * {} = {}\n".format(y, x, x * y), end='')

# 方式2：使用while循环
x1 = 1
while x1 <= 9:
    y1 = 1
    while y1 <= x1:
        print("{} * {} = {}\t".format(y1, x1, y1 * x1), end='')
        y1 += 1
    print(end='\n')
    x1 += 1

"""
3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']当中
请把这 5 个人从 black_list 当中删除，最后 black_list 为空
"""
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in range(len(black_list)):
    for friend in black_list:
        black_list.remove(friend)
print(black_list)

# 4.使用循环实现排序算法 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面）
a = [1, 7, 4, 89, 34, 2]
for num in range(len(a) - 1):
    for num1 in range(num+1, len(a)):
        if a[num] > a[num1]:
            a[num], a[num1] = a[num1], a[num]
print(a)

"""
5.编写如下程序
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""

user = input("请输入用户名：")
pwd = input("请输入密码：")


def login(username, password):
    if username == 'lemon' and password == 'best':
        return "登录系统成功!"
    else:
        return "用户名或密码错误!"


print(login(user, pwd))
