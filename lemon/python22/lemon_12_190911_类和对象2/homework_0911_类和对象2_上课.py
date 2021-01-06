#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/9/16 16:21
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

"""
1.编写如下程序

编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
"""


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        """功力。"""
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


c = Calculator(3, 4)
print(c.cal_add())

"""
2：编程题

人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
"""

import random


class Game:

    roles = {"1": "曹操", "2": "张飞", "3": "刘备"}
    choices = {"1": "剪刀", "2": "石头", "3": "布"}
    result = {'victory': 0, 'peace': 0, 'failed': 0, 'total': 0}

    def get_role(self):
        role = input('请选择角色：1 曹操 2张飞 3 刘备')
        if role.isdigit() and role in self.roles:
            print("您选择的角色是{}".format(self.roles[role]))

    def user_choose(self):
        """
        出拳
        :return:
        """
        choice_key = input('请出拳：1剪刀 2石头 3布')
        if choice_key.isdigit() and choice_key in self.choices:
            choice = self.choices[choice_key]
            print("您的出拳是{}".format(choice))
            return choice

    def computer_choose(self):
        k = random.choice(list(self.choices.keys()))
        # random.randint(1,10)
        choice = self.choices[k]
        print("电脑出拳是{}".format(choice))
        return choice

    def get_result(self):
        user_choice = self.user_choose()
        computer_choice = self.computer_choose()
        if user_choice is not None:
            if (user_choice, computer_choice) in (
                    ('剪刀', '布'), ('石头', '剪刀'), ('布', '石头')
            ):
                self.result['victory'] += 1
                print("赢！电脑弱爆了！！！")
            elif computer_choice == user_choice:
                self.result['peace'] += 1
                print("平局，心有灵犀，要不咋再来一盘！")
            else:
                self.result['failed'] += 1
                print("输了，不行，我要和你决战到天亮！")

            self.result['total'] += 1
        else:
            print('你的出拳错误')
        continued = input("是否继续？按y继续，按n退出")
        if continued == 'y':
            return True
        # 其他情况需求不明。
        return False

    def total_result(self):
        print("******" * 10)
        print("你获胜 {}".format(self.result['victory']))
        print("电脑获胜 {}".format(self.result['total'] - self.result['victory'] - self.result['peace']))
        print("平局 {}".format(self.result['peace']))


def main():
    game = Game()
    while True:
        r = game.get_result()
        if r is False:
            game.total_result()
            break


if __name__ == '__main__':
    main()


"""
3、实现文字版游戏：坦克大战
步骤一：定义TANK类：

    1、实现一个BaseTank类（所有Tank的父类）
        BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
        BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
        BeseTank拥有HP属性（代表血量，默认为10）
        BeseTank拥有attack_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）BeseTank拥有HP属性（代表血量，默认为10）
        BaesTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
    2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
        move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
        Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
    3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
        move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
        Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），


步骤二：选做题（扩展题，不要求提交）
2、游戏环节（循环，直到有tank死亡才退出循环）

    1、玩家发生子弹，然后电脑坦克发射子弹，
    2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
    3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
    4、玩家移动、电脑移动
"""


class UserTank:
    def __init__(self, postion, attack_postion, live=True):
        self.live = live
        self.position = postion
        self.attack_postion = attack_postion

    def move(self, x, y):
        # 实例方法，修改实例属性。
        self.position = (x, y)
        return x, y
        # return None

    def bullet_launch(self, x, y):
        self.attack_postion = (x, y)
        return x, y


class PCTank:
    def __init__(self, postion, attack_postion, live=True):
        self.live = live
        self.position = postion
        self.attack_postion = attack_postion

    def move(self, x, y):
        # 实例方法，修改实例属性。
        self.position = (x, y)
        return x, y

    def bullet_launch(self, x, y):
        self.attack_postion = (x, y)
        return x, y


#
# class BaseTank:
#
#     def __init__(self):
#         self.live = 1
#         self.position = random.randint(1,10)
#         self.HP = 2
#         self.attack_position = random.randint(1,10)
#
#     def hit(self, other):
#         """
#         a = PCtank() MyTank()
#         :param other: 只是一个参数。other 规定这是一个坦克的实例
#         :return:
#         """
#         # tank.attack_postion
#         if other.attack_position == self.position:
#             self.HP -= 1
#             print("{} 被攻击，血量 -1, 剩余血量{}".format(self, self.HP))
#             if self.HP <= 0:
#                 self.live = 0
#
#
# class MyTank(BaseTank):


    def move(self):
        # continue_move = True
        while True:
            postion = input("输入移动位置：1-10的数字:")
            if postion.isdigit():
                postion = int(postion)
            if postion in range(1, 11):
                self.position = postion
                print("你现在的位置：{}".format(self.position))
                break
#
#     def bullet_launch(self):
#         continue_bull = True
#         while continue_bull:
#             postion = input("输入攻击位置：1-10的数字:")
#             if postion.isdigit():
#                 postion = int(postion)
#             if postion in range(1, 11):
#                 self.attack_position = postion
#                 print("你攻击的位置：{}".format(self.attack_position))
#                 break
#
#
# class PCTank(BaseTank):
#     def move(self):
#         self.position = random.randint(1,10)
#
#     def bullet_launch(self):
#         self.attack_position = random.randint(1,10)
#
# mytank = MyTank()
# pctank = PCTank()
#
# while all((mytank.live, pctank.live)):
#     # all()
#     mytank.bullet_launch()
#     pctank.bullet_launch()
#     pctank.hit(mytank)
#     mytank.hit(pctank)
#
#     if pctank.live == 0:
#         print("电脑已死")
#         break
#     if mytank.live == 0:
#         print("玩家牺牲")
#         break
#
#     mytank.move()
#     pctank.move()
