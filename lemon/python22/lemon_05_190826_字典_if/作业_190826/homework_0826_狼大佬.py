# -*- coding: utf-8 -*- 
# @Time     : 2019/8/17 23:49 
# @Author   : wolf_eye 
# @Email    : 15840995236@163.com 
# @File     : homework_0816.py 
# @student  : 狼眸

# Q1: 请写出if判断语句的格式（考虑 2 种典型的 if...if 场景。）
# 场景一：嵌套if
# 如果 "condition_1" 为 True，将执行 "statement_block_1" 块语句，后面的elif...else程序将不会执行。
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True，将执行 "statement_block_2" 块语句，后面的else程序将不会执行。
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3

# 场景二：并行if
# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句，
# 如果 "condition_2" 为 True 将执行 "statement_block_2" 块语句
# 但是不论"condition_1" 为 True或 False，只要不抛异常，都会执行到if condition_2：
# if condition_1:
#     statement_block_1
# if condition_2:
#     statement_block_2

# Q2: 判断是否为闰年
# 方法一：定义一个可以重复输入年份并且进行判断的函数leap_year()


def leap_year():

    while True:
        try:
            year = int(input('请您输入一个有效的年份：'))
            if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
                print(f'{year}年是闰年')
            else:
                print(f'{year}年不是闰年')
        except Exception as err:
            print('您输入的内容无法识别，请重新输入')
            print(f'输入内容非法原因为：{err}')
        finally:
            leap_year()
# 调用函数


leap_year()

# 方法二：可选择退出的判断闰年的程序
while True:
    year = input('请您输入一个有效的年份(若您不想进行本次验证，请输入“No”)：')
    if year == 'No':
        print('本次验证结束！')
        break
    elif year.isdigit():
        year_int = int(year)
        if year_int % 400 == 0 or year_int % 100 != 0 and year_int % 4 == 0:
            print(f'{year}年是闰年')
        else:
            print(f'{year}年不是闰年')
    else:
        print('您输入的内容无法识别，请重新输入')

# Q3: 使用条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
import random
print('''---石头剪刀布游戏开始-----
请按下面提示出拳：''')
game_dict = {'1': '石头', '2': '剪刀', '3': '布', '4': '退出'}
while True:
    print('石头[1] 剪刀[2] 布[3] 退出[4]')
    num_people = input('请输入你的选项：')
    num_computer = random.randint(1, 3)
    if num_people in game_dict.keys():
        num_int = int(num_people)
        if num_int == 4:
            print('游戏结束')
            break
        elif num_int - num_computer == (-1 or 2):
            print(f'您的出拳为:{game_dict[num_people]},电脑出拳:{game_dict[str(num_computer)]},您胜利了')
        elif num_int == num_computer:
            print(f'您的出拳为:{game_dict[num_people]},电脑出拳:{game_dict[str(num_computer)]},平局')
        else:
            print(f'您的出拳为:{game_dict[num_people]},电脑出拳:{game_dict[str(num_computer)]},您输了')
    else:
        print('您输入的内容无法识别，请重新输入')


# Q4：一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# 购买金额 = 价格 * 数量
import re
# lambda函数判断正则表达式
is_legal = lambda pattern, string: re.match(pattern, string)
# lambda函数计算最终价格
final_price = lambda total_price, discount: total_price * discount
# 浮点数正则表达式，缺陷没有过滤0.00
pattern_float = re.compile(r'^[0-9]+\.[0-9]+$')
# 非0正整数正则表达式
pattern_int = re.compile(r'^[1-9]\d*$')
# 循环输入商品价格与数量，计算最终价格
while True:
    price = input("请输入商品名价格：")
    if is_legal(pattern_float, price) or is_legal(pattern_int, price):
        while True:
            number = input("请输入商品的数量：")
            if is_legal(pattern_int, number):
                total_price = float(price) * int(number)
                if total_price > 100:
                    print(f'您的购买价格为{price}元，您的购买数量为{number}，给您的折扣为20%，最终价格为{round(final_price(total_price, 0.8),2)}元')
                    break
                elif total_price in range(50, 101):
                    print(f'您的购买价格为{price}元，您的购买数量为{number}，给您的折扣为10%，最终价格为{round(final_price(total_price, 0.9),2)}元')
                    break
                else:
                    print(f'您的购买价格为{price}元，您的购买数量为{number}，没有折扣，最终价格为{round(final_price(total_price, 1),2)}元')
                    break
            else:
                print('您输入的数量无法识别，请重新输入')
    else:
        print('您输入的价格无法识别，请重新输入')
