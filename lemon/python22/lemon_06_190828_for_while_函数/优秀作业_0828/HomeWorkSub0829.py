# -*- coding:utf-8 -*-
# time: 2019/8/29 20:10
# email: 870903061@qq.com
# author: sub
# copyright: null
# file: HomeWorkSub0829.py
'''
1.求三个整数中的最大值
提示：三个整数使用input提示用户输入
'''

digit = []  # 存储输入的三个整数
# 循环输入三个整数
num = 1
while num <= 3:
    digit01 = input("请输入第" + str(num) + "个整数： ")
    # 判断输入的是否为整数，非整数重新输入，输入整数则将输入的整数存入digit
    if digit01.isdigit():
        digit.append(digit01)
        num += 1
    else:
        print("您输入的不是整数，请重新输入")
# 对输入的三个整数进行判断
if (int(digit[0]) >= int(digit[1])) and (int(digit[0]) >= int(digit[2])):
    print("您输入的最大值为：" + digit[0])
elif (int(digit[1]) >= int(digit[0])) and (int(digit[1]) >= int(digit[2])):
    print("您输入的最大值为：" + digit[1])
else:
    print("您输入的最大值为：" + digit[2])


'''
2.分别使用for和while打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
1 * 1 = 1	
1 * 2 = 2    2 * 2 = 4	
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9	
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16	
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25	
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36	
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49	
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64	
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
'''
# 使用for循环
for x in range(1, 10):
    # 保持第一个乘数不变，第二个乘数从1递增到x相等
    for y in range(1, x+1):
        # 打印出第一个乘数不变的
        print('''{} * {} = {}'''.format(x, y, x*y), end='\t')
    # 打印里面放for循环的结果
    print()

# 使用while循环
x = 1
while x <= 9:
    y = 1
    while y < x + 1:
        print('''{} * {} = {}'''.format(x, y, x * y), end='\t')
        y += 1
    print()
    x += 1

'''
3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']当中, 
请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
'''
# 1.使用函数清空
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
black_list.clear()
print(black_list)

# 2.使用while循环删除
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
while True:
    if len(black_list) == 0:  # 判断列表是否全部删除
        print("当前black_list列表为:" + str(black_list) + ",已全部删除")
        break
    else:
        black_list.pop(0)

# 3.使用for循环删除
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 第一次for循环会删除索引为1的，即卖茶叶，第二次循环会删除索引为1的，即删除买保险，第三次循环会删除索引为2的，即删除买手机
for num in black_list:
    print('''当前删除的为{}'''.format(num))
    black_list.remove(num)
# 第一次for循环会删除索引为1的，即删除卖面膜，第二次循环会删除索引为1的，无索引为1的
for num1 in black_list:
    print('''当前删除的为{}'''.format(num1))
    black_list.remove(num1)
# 删除最后一个
for num2 in black_list:
    print('''当前删除的为{}'''.format(num2))
    black_list.remove(num2)
print("当前black_list列表为:" + str(black_list) + ",已全部删除")

# 4.第二种使用for循环删除，获取列表长度，决定循环删除次数
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for num in range(len(black_list)):
    black_list.pop()
print("当前black_list列表为:" + str(black_list) + ",已全部删除")


'''
4.使用循环实现排序算法
提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
'''
a = [1, 7, 4, 89, 34, 2]
for m in range(len(a)-1):     # 取出最后的索引位置，得到大循序的次数
    # 将m索引位置与之后位置循环比较大小，将小于m索引位置的值更新到m索引位置，将原先m索引位置的值更新到n索引的位置
    for n in range(m+1, len(a)):
        if a[m] > a[n]:
            k = a[n]     # 将小的值付给一个变量
            a[n] = a[m]  # 将小的值更新为大的值，两个索引位置的值相等
            a[m] = k     # 将原先大的索引位置值更新为之前保存的变量（小的值）
print(a)

'''
5. .编写如下程序
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
'''
# 定义函数user_info，用来判断账号密码是否正确
def user_info(user_name,user_pass):
    if user_name == 'lemon' and user_pass == 'best':
        return "账号密码正确，登录成功"
    else:
        return "账号密码错误!"
# 对输入的内容进行判断，输入正确登录系统成功，否则显示用户名或密码错误，要求重新输入,累计输入错误5次，账号锁定
# 定义输入次数
num = 0
while num <= 4:
    user_name = input("请输入账号： ")
    user_pass = input("请输入密码： ")
    login = user_info(user_name, user_pass)  # 调用函数user_info
    # 判断输入的账号密码是否正确
    if login == '账号密码正确，登录成功':
        print(login)
        break
    else:
        # 输入错误的情况，对输入次数进行校验
        if num <= 3:
            print("账号密码错误，请重新输入！")
            num += 1
        else:
            print("账号密码输入错误已累计5次，账号锁定")
            break


