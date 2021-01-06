# 第一题、求三个整数中最大值
# 定义一个取最大值的函数
# 引入math库使用负无穷
import math


def GetMaxNumber():
    while True:
        temp_list = input("请输入三个整数，以空格分隔开：")
        number_list = temp_list.split()

        # 最大值赋值成负无穷
        max_number = -math.inf
        if len(number_list) != 3:
            print("您输入整数个数不对")
            continue

        for element in number_list:
            try:
                temp_element=int(element)
                if max_number < temp_element:
                    max_number = temp_element
            except:
                print(f"{element}不是整数")
                break
        else:
            print('三个数中最大的是：{}'.format(max_number))


# 调用函数获取三个整数中的最大值
GetMaxNumber()
exit(0)

# 第二题 打印九九乘法表

# for形式
for line in range(1, 10):
    for i in range(1, line+1):
        print("{}*{}={}\t".format(i, line, i*line), end='')
    print('\n')

# while形式
temp_line = 1
while temp_line < 10:
    # 换行要将列重置为1
    temp_colum = 1
    # 列从1开始直到递增为行的值
    while temp_colum <= temp_line:
        print("{}*{}={}\t".format(temp_colum,
                                  temp_line, temp_colum*temp_line), end='')
        temp_colum += 1

    # 行递增
    temp_line += 1
    print('\n')

# 第三题
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '买手机']
# 第一种方法clear：
black_list.clear()
print(black_list)

# 第二种方法直接赋值为空：
black_list = []

# 第三种方法while循环删：
temp_count = len(black_list)
while temp_count > 0:
    black_list.pop()
    temp_count -= 1
print(black_list)

# 第四种从后面删
while black_list:
    black_list.pop()

# 第五种从前面删
while black_list:
    black_list.pop(0)

# 第六种for循环删
for i in range(0, len(black_list)):
    black_list.pop()

# 第四题：使用循环实现排序算法


def sortlist(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            # 第一个跟后面的比较，大的话向后交换
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


# 调用排序函数
a = [1, 7, 4, 89, 34, 2]
ret = sortlist(a)
print(ret)



# 第五题：
# 定义一个函数判断用户名密码是否存在
def Authentation(username, password):
    return (username, password) in [('lemon', 'best')]

usrname = input("请输入用户名：")
password = input("请输入密码：")

# 调用认证方法
ret = Authentation(usrname, password)
print("登录成功" if ret else "用户名或密码错误")
