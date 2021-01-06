# --*-- coding : utf-8 --*--
# Project      : python22
# IDE          : PyCharm

# 1.编写如下程序
#
# 创建一个txt文本文件，来添加数据
#
# a.第一行添加如下内容：
#
# name,age,gender,hobby,motto
f = open('txt.txt', mode='w', encoding='utf-8')
f.write('name,age,gender,hobby,motto')
# b.从第二行开始，每行添加具体用户信息，例如：
# yuze,17,男,假正经, I am yours
# cainiao,18,女,看书,Lemon is best!
# 追加模式 a
f = open('txt.txt', mode='a', encoding='utf-8')
f.write("""
yuze,17,男,假正经, I am yours
cainiao,18,女,看书,Lemon is best!""")

# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
person_info = [{"name": "yuze", "age": 18, "gender": "男", "hobby": "", "motto": "hehe"}]
# d.将所有用户信息写入到txt文件中之后，然后再读出
d = open('new01_txt.txt', mode='w', encoding='utf-8')
for i in person_info:
    for ii in i.items():
        for iii in ii:
            d.write(str(iii) + ' ')

d = open('new01_txt.txt', mode='r', encoding='utf-8')
d_01 = d.readlines()  # 返回的是一个列表
d_02 = (d_01[0].split(' '))
d_02.pop()
d_03 = d_02
print(d_02)

#
#
# 2.编写如下程序
# 有两行数据，存放在txt文件里面：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
# [{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]

# 创建新文件写入数据
# f = open('new_txt.txt', mode='w', encoding='utf-8')
# f.write("""url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000""")
cc = []
new_dict = {}
f = open('new_txt.txt', mode='r', encoding='utf-8')
a = f.readlines()  # 返回的是一个列表
list_01 = []
for aa in a:
    list_01.append(aa.split('@'))
    for b in list_01:
        for c in b:
            c = c.rstrip('\n')  # 移除行尾换行符
            cc.append(c.split(':'))
# print(cc)


# 3.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况

"""
def buy_tangerine(price, weight):
    try:
        sum = float(price) * float(weight)
        return f"付款金额为{sum}"
    except ValueError:
        return '输入有误'


while True:
    price = input('输入橘子的价格, 单位:元／斤：')
    weight = input('输入用户购买橘子的重量, 单位:斤：')
    print(buy_tangerine(price, weight))
"""

#
# 3.编写如下程序
# 优化剪刀石头布游戏程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平

import random  # 导入模块, 一般放在文件顶部

number = 0  # 次数
victory = 0  # 胜利
defeated = 0  # 失败
dogfall = 0  # 平局
game = {1: '石头', 2: '剪刀', 3: '布'}  # 创建个字典, 存数据
print('---石头剪刀布游戏开始---\n请按下面提示出拳：')
while True:
    number += 1
    player = input("石头【1】 剪刀【2】 布【3】 退出【4】\n请输入您的选项：")
    robot = random.randint(1, 3)
    try:
        if player.isdigit():  # 字符串操作，判断是不是都是正整数
            int_player = int(player)  # 把玩家输入的数据转换为int
            try:
                if 4 > int_player != 0:  # 确保数据是：1~3
                    if int_player == robot:  # 首先判断平局, 就是两个值相等.
                        dogfall += 1
                        print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 平局.\n')
                    elif (int_player == 1 and robot == 3) \
                            or (int_player == 2 and robot == 1) \
                            or (int_player == 3 and robot == 2):  # 进行游戏规则的判断
                        defeated += 1
                        print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 您失败了.\n')
                    else:
                        victory += 1
                        print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 您胜利了.\n')
                elif int_player == 4:
                    print('游戏结束\n')
                    break  # 退出循环.
            except:
                print('您的输入有误, 请重新输入.\n')
    except:
        print('您的输入有误, 请重新输入.\n')
print(f'次数{number - 1}, 胜利{victory}次, 失败{defeated}次, 平局{dogfall}次.')
