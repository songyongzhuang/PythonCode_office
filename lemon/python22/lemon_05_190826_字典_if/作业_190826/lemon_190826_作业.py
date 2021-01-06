# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190826_作业.py
# Author       : 大壮
# Create time  : 2019-08-27 08:36
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


# 1.请写出if判断语句的格式（考虑 2 种典型的 if...if 场景。）
# 1.1、第一个场景 写嵌套
while True:
    week = input('1-7七个数字，分别代表一周七天(回复“退出”退出本系统)：')
    if week.isdigit():  # 只要不是正整数的都剔除
        int_week = int(week)  # 转换为int
        if 0 < int_week <= 7:
            if int_week >= 6:
                print(f'今天是周{int_week}, 知识记住再出去浪\n')
            else:
                print(f'今天是周{int_week}, 努力工作、学习呀\n')
        else:
            print('输入有误，请输入1~7：\n')
    elif week == '退出':
        print('退出系统成功！\n')
        break
    else:
        print('输入有误，请输入1~7：\n')

# 1.2、判断学生成绩 (这里没有对数据进行判断，只是为了写流程) 写if elif elif ... else
while True:
    grade = input('请输入学生的考试成绩((回复“0”退出本系统).满分100)：')
    int_grade = int(grade)
    if int_grade > 100:
        print('请输入正确考试成绩满分100.\n')
    elif int_grade == 100:
        print('完美')
    elif 99 >= int_grade >= 90:
        print('优秀')
    elif 89 >= int_grade >= 80:
        print('良好')
    elif 79 >= int_grade >= 70:
        print('一般')
    elif 69 >= int_grade >= 60:
        print('合格')
    elif int_grade == 0:
        print('退出！')
        break  # 结束循环
    else:
        print('抓紧复习下次考过')


# 第二题
# 2.判断是否为闰年
# 提示:
# 输入一个有效的年份（如：2019），判断是否为闰年
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
# 那么某一年是不是闰年该怎么判断呢？
# A： 可以被4整除的，但不能被100整除
# B： 可以被400整除
# 只要满足AB任意一种情况就是闰年。

while True:
    year = input('请输入一个年份, 判断是否是闰年, 回复“1”退出本系统, 谢谢合作：')
    if year.isdigit():  # 字符串操作，判断是不是都是正整数
        int_year = int(year)  # 把字符串转换为int类型, 方便进行计算
        if int_year == 0:  # 公元纪年的起点是公元1年，而没有“公元0年”。
            print(f'{int_year}年不是闰年\n')
        elif (int_year % 4 == 0 and int_year % 100 != 0) or int_year % 400 == 0:  # 逻辑运算.
            print(f'{int_year}年是闰年\n')
        elif int_year == 1:
            print('退出系统成功, 期待您的下次使用, 祝您生活愉快.\n')
            break
        else:
            print(f'{int_year}年不是闰年\n')
    else:
        print('您的输入有误, 请重新输入正确的年份.\n')


""" 3.剪刀石头布游戏
使用条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：
---石头剪刀布游戏开始---
请按下面提示出拳：
石头【1】 剪刀【2】 布【3】 退出【4】
请输入您的选项：1
您出拳为：石头, 电脑出拳为：剪刀, 您胜利了
石头【1】 剪刀【2】 布【3】 退出【4】
请输入您的选项：4
游戏结束
-------------------------------------------------------------------------------------------------
电脑随机出拳
使用随机数，首先需要导入随机数的模块 —— “工具包”
import random
导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
random.randint(a, b)，返回[a, b]之间的整数，包含a和b
random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
random.randint(4, 4)  # 结果永远是 4
random.randint(25, 12)  # 该语句是错误的，下限必须小于上限 """

import random  # 导入模块, 一般放在文件顶部

game = {1: '石头', 2: '剪刀', 3: '布'}  # 创建个字典, 存数据
print('---石头剪刀布游戏开始---\n请按下面提示出拳：')
while True:
    player = input("石头【1】 剪刀【2】 布【3】 退出【4】\n请输入您的选项：")
    robot = random.randint(1, 3)
    if player.isdigit():              # 字符串操作，判断是不是都是正整数
        int_player = int(player)      # 把玩家输入的数据转换为int
        if 4 > int_player != 0:       # 确保数据是：1~3
            if int_player == robot:   # 首先判断平局, 就是两个值相等.
                print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 平局.\n')
            elif (int_player == 1 and robot == 3) or \
                    (int_player == 2 and robot == 1) or \
                    (int_player == 3 and robot == 2):  # 进行游戏规则的判断
                print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 您失败了.\n')
            else:
                print(f'您出拳为：{game.get(int_player)}, 电脑出拳为：{game.get(robot)}, 您胜利了.\n')
        elif int_player == 4:
            print('游戏结束\n')
            break  # 退出循环.
        else:
            print('您的输入有误, 请重新输入.\n')
    else:
        print('您的输入有误, 请重新输入.\n')


# 4、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。

while True:
    money = input('请您输入购买金额(回复“退出”退出本系统)：')
    if money.replace('.', '').isdigit():  # replace方法不会改变原字符串, 把所有的"."替换成"", 再判断是不是纯数字.
        if money.count('.') < 2:  # 用count来查找字符串中的".", 判断"."要小于2个
            float_money = float(money)  # 字符串转为浮点类型
            if float_money == 0:
                print('您的输入数据有误, 金额不能为零.\n')
            elif 50 <= float_money <= 100:  # 包含50元和100元
                print('您购买的商品价格为：{}元, 给予10%折扣, 最终价格为：{:.2f}元.\n'
                      .format(float_money, (float_money - float_money * (10 / 100))))  # 折扣百分比除100就是
            elif float_money > 100:
                print('您购买的商品价格为：{}元, 给予20%折扣, 最终价格为：{:.2f}元.\n'
                      .format(float_money, (float_money - float_money * (20 / 100))))
            else:
                print(f'您购买的商品价格为：{float_money}元, 没有折扣, 只有购买五十及以上金额才有折扣. \n')
        else:
            print('您的输入数据有误请重试\n')
    elif money == '退出':
        print('退出系统成功, 期待您的下次使用, 祝您生活愉快.')
        break
    else:
        print('您的输入数据有误请重试\n')
