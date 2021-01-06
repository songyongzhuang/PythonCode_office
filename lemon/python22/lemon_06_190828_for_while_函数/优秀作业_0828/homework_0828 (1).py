# 1.求三个整数中的最大值

# 1通过内置函数返回最大值
# 2比较两个数的大小，返回最大值
def isInt(num):
    try:
        num = int(str(num))
        return isinstance(num, int)
    except:
        return False
def max1(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

first_num=input('请你输入第一个整数：')
second_num = input('请你输入第二个整数：')
third_num=input('请你输入第三个整数：')
if  isInt(first_num)==False or isInt(second_num)==False or isInt(third_num)==False:
    print("你输入的不是整数")
else:
    max_1=max(first_num,second_num,third_num)
    max_2=max1(max1(first_num,second_num),third_num)
    print('三个数中的最大值是：{}'.format(max_1))
    print('三个数中的最大值是：{}'.format(max_2))
# 3比较三个数的大小，返回最大值
def max1(num1, num2,num3):
    if num1 > num2:
        if(num1>num3):
            k=num1
        else:
            k=num3
    else:
        if (num2 < num3):
            k = num3
        else:
            k = num2
    return k
first_num=input('请你输入第一个整数：')
second_num = input('请你输入第二个整数：')
third_num=input('请你输入第三个整数：')
if  (first_num)==False or isInt(second_num)==False or isInt(third_num)==False:
    print("你输入的不是整数")
else:
    max_1=max1(first_num,second_num,third_num)

    print('三个数中的最大值是：{}'.format(max_1))

# 2.分别使用for和while打印九九乘法表
# 通过while
li=[1,2,3,4,5,6,7,8,9]
i=0
while i<9:
    j = 0
    while j<=i:
        print('{}*{}={}'.format(li[j],li[i],li[i]*li[j]),end='\t')

        j=j+1
    print()
    i=i+1
#通过获取值遍历，e得到的是值
li=[1,2,3,4,5,6,7,8,9]
for e in li:
    for j in li:

        if(j<=e):
            print('{}*{}={}'.format(j, e, j*e), end='\t')
    print()
#通过索引遍历，index得到的是索引
li=[1,2,3,4,5,6,7,8,9]
for index in range(len(li)):

     for j in range(len(li)):
          if(j<=index):
           print('{}*{}={}'.format(li[j], li[index], li[index] * li[j]), end='\t')
     print()
#
# 3、你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=
#
# ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
#  当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空。
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']

for e in range(len(black_list)):
    black_list.pop(e)
    print(black_list)
for e in black_list:
    black_list.remove(e)
    print(black_list)

# 4.
# 使用循环实现排序算法
#
# 提示：利用for循环，完成a = [1, 7, 4, 89, 34, 2]
# 的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法

li = [1,7,4,89,34,2]
n= len(li)

for x in range(n-1):
   for y in range(n-1-x):
      if li[y]>li[y+1]:
         li[y],li[y+1]=li[y+1],li[y]

print(li)
# 5. .编写如下程序
#
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
#
# a.定义一个函数，接收用户输入的用户名和密码作为参数
#
# b.正确的账号，用户名为lemon，密码为best
def login(username,password):
    if username=='lemon' and password=='best':
        return True
    else:
        return False

name=input('请你输入一个用户名：')
pwd=input('请你输入一个密码：')
if login(name,pwd):
    print('登录系统成功')
else:
    print('用户名或密码错误')
def login(username,password):
    if username=='lemon' and password=='best':
        print('登录系统成功')
        return True
    else:
        print('用户名或密码错误')
        return False
name=input('请你输入一个用户名：')
pwd=input('请你输入一个密码：')
login(name,pwd)
#直接return
def login(username,password):
    if username=='lemon' and password=='best':
       return '登录系统成功'
    else:
        return '用户名或密码错误'
name=input('请你输入一个用户名：')
pwd=input('请你输入一个密码：')
print(login(name,pwd))

