# -*- coding: utf-8 -*-
# datetime：2019-08-28
# author：ms
# email：1065867482@qq.com

'''
1.求三个整数中的最大值
提示：三个整数使用input提示用户输入
'''
# 提示用户输入
# num1 = int(input('please input the first number:'))
# num2 = int(input('please input the second number:'))
# num3 = int(input('please input the third number:'))
# if num1 > num2 and num1 >num3:
#     max_num = num1
# elif num2 > num1 and num2 > num3:
#     max_num = num2
# elif num3 > num1 and num3 > num2:
#     max_num = num3
# print(max_num)
# max_num = num1
# if max_num < num2:
#     max_num = num2
# elif max_num < num3:
#     max_num = num3
# print(max_num)


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
#  for循环
#  定义一个变量i，取值范围在1~9，每一个循环后，会自动进行i += 1
# for i in range(1, 10):
#     #  定义一个变量j，起始值为1，结束值为i+1，当结束值取为i+1,每次就会输出1~i+1范围的信息，确定换行范围
#     for j in range(1, i + 1):
#         # 将i*j 所得到的值赋值给value
#         value = i * j
#         # 输出信息并以tab键空格
#         print("{} * {} = {}".format(j, i, value), end='\t')
#     print('\n')
#  while循环
# i = 1
# #  当i<=9进入循环
# while i <= 9:
#     j = 1
#     # 当j<=i进入循环
#     while j <= i:
#         # 将i*j 所得到的值赋值给value
#         value = i * j
#         # 输出信息并以tab键空格
#         print("{} * {} = {}".format(j, i, value), end='\t')
#         #  把j+1赋值给j
#         j = j + 1
#     print('\n')
#     #  把i+1赋值给i
#     i = i + 1


'''
3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=

['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
 当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
'''
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# for循环取遍历black_list列表
for sale_people in black_list[:]:
    # 删除sale_people信息
    black_list.remove(sale_people)
    # 打印black_list列表信息
    print(black_list)

'''
4.使用循环实现排序算法
提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
'''
a = [1, 7, 4, 89, 34, 2]
# i的取值范围是从1到len(a)，每一个循环后，会自动进行i += 1
for i in range(1, len(a)):
    # j的取值范围是从1到len(a)-i，每一个循环后，会自动进行j += 1
    for j in range(0, len(a) - i):
        # 假如a[j]的值大于a[j+1]的值
        if a[j] > a[j + 1]:
            # 将a[j],a[j+1]的值互换
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

'''
5. .编写如下程序

从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。

a.定义一个函数，接收用户输入的用户名和密码作为参数

b.正确的账号，用户名为lemon，密码为best
'''
# 定义一个函数info
def info(name, password):
    # 将lemon赋值给user_name
    user_name = 'lemon'
    # 将best赋值给user_pass
    user_pass = 'best'
    # 将user_name、user_pass与name,password进行比较，两者一致，输出登录系统成功
    if user_name == name and user_pass == password:
        print('登录系统成功!')
    # 如果user_name不等于name，输出请输入正确的用户名
    elif user_pass != name and user_pass == password:
        print('请输入正确的用户名！')
    # 如果user_pass不等于password，输出请输入正确的密码
    elif user_name == name and user_pass != password:
        print('请输入正确的密码！')
    # 如果user_name、user_pass不等于name、password，输出请输入正确的用户名与密码
    else:
        print('请输入正确的用户名与密码！')
    return

name = input('输入用户名：')
password = input('请输入密码：')
# 调用函数，并传入参数
info(name, password)