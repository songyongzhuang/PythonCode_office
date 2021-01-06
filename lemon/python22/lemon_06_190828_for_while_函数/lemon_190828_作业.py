# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190828_作业.py
# Author       : 大壮
# Create time  : 2019-08-28 22:41
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
print('*' * 30, '第一题', '*' * 30)


# 1、求三个整数中的最大值：
# 提示：三个整数使用input提示用户输入


def judge_size():
    i = 1
    data = []  # 使用sort对列表进行排序，取出最后一个索引
    while i <= 3:
        a = input(f'请输入第{i}个整数：')
        if a.replace('-', '', 1).isdigit():  # 0是整数 负数也是整数
            if a.find('-') == -1 or a.find('-') == 0:  # 判断数据只能没有"-", 或者第一个为"-"
                data.append(int(a))  # 转换为int传入列表中
                i += 1
                if len(data) == 3:
                    print(f'您输入的数据是：{data}, ', end='')
                    data.sort()  # 对列表进行排序
                    print(f'最大值为：{data[-1]}')
                else:
                    pass
            else:
                print('您的输入有误, 请输入整数：\n')
        else:
            print('您的输入有误, 请输入整数：\n')


judge_size()  # 函数不调用，不执行

print('*' * 30, '第二题', '*' * 30)


# 2、分别使用for和while打印九九乘法表
# 提示：
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）


# 使用for循环
def multiplication_table_for():
    for a in range(1, 10):
        for b in range(1, a + 1):
            print(f"{a}*{b}={a * b}\t", end='')
        print()  # 循环一次换行一次


multiplication_table_for()  # 函数不调用，不执行


# 使用while循环
def multiplication_table_while():
    c = 1
    while c < 10:
        d = 1  # 一定要写在里面，每次循环都是从一开始的.
        while d <= c:  # <=
            print(f'{c}*{d}={c * d}\t', end='')
            d += 1
        c += 1
        print()


multiplication_table_while()  # 函数不调用，不执行

print('*' * 30, '第三题', '*' * 30)


# 3、你的微信好友当中有 5 个推销的，他们存在一个列表中
# black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
# 第一种做法


def delete_friend_01():
    black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
    """ 每次循环索引加一, 循环到第二次的时候索引是一, 就会落下一个所以要对列表进行复制 """
    for sell in black_list[:]:
        black_list.remove(sell)
    print(f'最终结果为：black_list = {black_list}')


delete_friend_01()  # 函数不调用，不执行


# 第二种做法
def delete_friend_02():
    black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
    for sell in black_list[:]:
        """ 简单粗暴款, 循环几次删几次. """
        black_list.pop(0)
    print(f'最终结果为：black_list = {black_list}')


delete_friend_02()  # 函数不调用，不执行.

print('*' * 30, '第四题', '*' * 30)
# 4、使用循环实现排序算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面）
# ，不能使用sort、sorted等内置函数或方法
""" 这个是看视频学了之后才会写的, 自己没写出来... """


def rank():
    arr = [9, 7, 4, 89, 34, 2]
    length = len(arr)  # 查看列表的长度
    for i in range(length):  # 判断最外圈的循环次数 控制跑多少次
        for j in range(length - 1):  # 每循环一次可以判断出一个最大值，两两比较需要长度减去 1
            if arr[j] > arr[j + 1]:  # 判断当前索引值的值是否大于后面的值  如：9 > 7
                tmp = arr[j]  # 创建一个变量用来储存当前索引的值(现在索引的值是大于后面索引的值) 如：变量a = 9
                arr[j] = arr[j + 1]  # 判断后把后面的值交给前面的值 如：赋值前 9 = 7  赋值后就是 7 = 7
                arr[j + 1] = tmp  # 把大的值在交给后面的索引值 如：赋值前 7 = 9 赋值后就是 9 = 9

    print(f'排序后的循序为：{arr}')


rank()  # 函数不调用，不执行.

print('*' * 30, '第五题', '*' * 30)


# 5、编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best


def user(account, cipher):
    if account == 'lemon' and cipher == 'best':
        print('登录系统成功！')
    else:
        print('用户名或密码错误.')


user(account=input('请输入用户名：'), cipher=input('请输入密码：'))
