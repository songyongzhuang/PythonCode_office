# -*- coding:utf-8 -*-
# datetime:2019/08/16
# email:84351228@qq.com
# author:Rachel



# 1.求三个整数中的最大值(提示：三个整数使用input提示用户输入)
number = []
i = 1

while len(number) < 3:
    try:
        number.append(int(input(f"请输入第{i}个数：")))
        if i == 1:
            number_max = number_min = number[i-1]
        else:
            if number_max < number[i-1]:
                number_min = number_max
                number_max = number[i-1]
        i += 1
    except Exception as e:
        print(f"你输入的第{i}个数无效，请重新输入数值类型字符！\n")
print(f"你输入的数是：{number}, 最大的数是：{number_max}，最小的数是：{number_min}")






# 2.分别使用for和while打印九九乘法表

# 2.1 for循环打印
for i in range(1, 10):
    for j in range(1, i+1):
        product = j * i
        print(f"{j}*{i}={product}  ", end='')
    print("\n")


# 2.2 while循环打印
i = 1
while i < 10:
    j = 1
    while j <= i:
        product = j * i
        print(f"{j}*{i}={product}  ", end='')
        j += 1
    i += 1
    print("\n")







""" 3.你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空  """
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']


# 3.1 for循环删除
def del_list(del_list):
    for i in range(len(del_list)):
        del_name = del_list.pop(0)             # 每删除列表一个元素后列表剩余元素向前移动一个位置，则每次循环只要删除第一个位置的元素即可清空列表
        print(f"微信名为({del_name})的好友已被删除！\n")
    return i+1


print(f"共{del_list(black_list)}个好友被删除！")


# 3.2 while循环删除
def del_list2(del_list1):
    i = 0
    len_list = len(del_list1)                   # 每删除一个列表元素后列表长度发生改变，需在循环外将列表原始长度取出
    while i < len_list:
        del_number = del_list1[0]
        del_list1.remove(del_list1[0])
        print(f"微信名为({del_number})的好友已被删除！\n")
        i += 1
    return i


print(f"共{del_list2(black_list)}个好友被删除！")






# 4.使用循环实现排序算法(提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法)
a = [1, 7, 4, 89, 34, 2]
b = []

# 4.1 循环找到列表中的最小值追加到列表b中后进行删除，直到把a列表剩余元素的最小值全部追加到b列表进行升序排序
def list_sort(list_a):
    for i in range(len(list_a)):
        find_index = a.index(min(list_a))
        b.append(a[find_index])
        a.pop(find_index)
    return b

print(f"a列表降序排序后为：{list_sort(a)}")



# 4.2
i = 0
b = []
len_list = len(a)
while i < len_list:
    find_index = a.index(min(a))
    b.append(a[find_index])
    a.pop(find_index)
    i += 1

print(f"a列表降序排序后为：{b}")








""" 
5.编写如下程序:从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best   

"""


# 1.

def user_login(user):
    while True:
        if user[0] != users["username"]:
            print("用户名错误，登录失败！")
            break
        else:
            if user[0] == users["username"]:
                if user[1] != users["password"]:
                    print("密码错误，登录失败！")
                    break
                else:
                    print("恭喜您登录成功！")
                    break


users = {"username": "lemon", "password": "best"}
i = 0
usinput = []
while i < 2:
    msg = ["请输入用户名：", "请输入密码:"]
    usinput.append(input(f"{msg[i]}\n"))
    i += 1
user_login(usinput)




# 2.此方法存在问题（当账号锁定后无法break跳出循环会继续执行循环体内的语句），暂未想到解决方法

users = {"username": "lemon", "password": "best"}
lock = 0



def user_input():
    i = 0
    usinput = []
    while i < 2:
        msg = ["请输入用户名：", "请输入密码:"]
        usinput.append(input(f"{msg[i]}\n"))
        i += 1
    user_login(usinput)



def user_login(user):
    global lock
    while True:
        if user[0] != users["username"]:
            print("用户名错误，请重新输入！")
            user.clear()
            user_input()
        else:
            if user[0] == users["username"]:
                if user[1] != users["password"]:
                    user.clear()
                    lock += 1
                    if lock < 5:
                        print(f"密码错误，请重新输入！还有{5 - lock}次机会")
                        user_input()
                    else:
                        print("您的账号已被锁定，请联系管理员！")
                        break
                        lock = 0      # 账号锁定清除密码输错记录
                else:
                    print("恭喜您登录成功！")
                    lock = 0     # 登录成功后清除密码输错记录
                    break


user_input()

















