""""""
'''
1.求三个整数中的最大值
提示：三个整数使用input提示用户输入'''

# 方法一：max()判断最大值
number = input('请输入三个整数（用逗号分隔）：')
number_list = number.split(',')
for i in range(3):
    number_list[i] = int(number_list[i])
print(max(number_list))

# 方法二：if比较
number_one = int(input('请输入一个整数：'))
number_two = int(input('请输入一个整数：'))
number_three = int(input('请输入一个整数：'))
if number_one > number_two:
    if number_one > number_three:
        print(number_one)
    else:
        print(number_three)
else:
    if number_two > number_three:
        print(number_two)
    else:
        print(number_three)

'''2.分别使用for和while打印九九乘法表'''
#使用for循环打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{} * {} = {}'.format( j,i, i * j), end='\t')
        if i == j:
            print()
#使用while循环打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{} * {} = {}'.format(j, i, i * j), end='\t')
        if i == j:
            print()
        j = j + 1
    i = i + 1

'''3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。'''
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
print(len(black_list))
for i in range(len(black_list)):
    black_list.pop()
    print(black_list)

'''4.使用循环实现排序算法 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法'''
a = [1,7,4,89,34,2]
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            print(a)


'''5. .编写如下程序; 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best'''

# 校验用户名和密码是否正确
def check_login(username,password):
    if username == 'lemon' and password == 'best':
        print('{}登录系统成功！'.format(username))
    else:
        print('用户名或密码错误')

username = input('请输入用户名：')
password = input('请输入密  码：')
# 调用校验方法，判断是否登录成功
check_login(username,password)