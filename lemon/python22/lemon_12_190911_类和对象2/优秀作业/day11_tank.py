# -*- coding:utf-8 -*-
# @Time : 2019-09-15 10:29
# @Author : 潘潘达
# @File : day11_tank.py

"""
实现文字版游戏：坦克大战
步骤一：定义TANK类：
1、实现一个BaseTank类（所有Tank的父类）
BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
BaseTank拥有position属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
BaseTank拥有HP属性（代表血量，默认为10）
BaseTank拥有attack_position属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）
BaseTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）

2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）

3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），

步骤二：选做题（扩展题，不要求提交）
2、游戏环节（循环，直到有tank死亡才退出循环）
1、玩家坦克发射子弹，然后电脑坦克发射子弹，
2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
4、玩家移动、电脑移动
"""
import random


class BaseTank(object):
    # 每个坦克都会有live和HP属性，且初始状态均一致，故定义为类变量
    live = 1
    HP = 1

    # 由于每个坦克的初始位置和攻击的位置可能不一致，故定义为实例变量
    def __init__(self):
        self.position = random.randint(1, 10)
        self.attack_position = random.randint(1, 10)

    # 定义实例方法，形参other为一个类
    def hit(self, other):
        if self.position == other.attack_position:
            self.HP = self.HP - 1
            if self.HP == 0:
                self.live = 0


# 定义我方坦克类，继承于基础坦克类
class MyTank(BaseTank):
    # 定义move方法
    def move(self):
        tank_position = input("请输入我方坦克的初始位置(1~10)：")
        while True:
            try:
                self.position = int(tank_position)
                break
            except ValueError:
                tank_position = input("坦克初始位置输入错误！请重新输入(1~10)：")
                continue

    # 定义发送子弹方法
    def bullet_launch(self):
        enemy_position = input("请输入我方坦克攻击的位置(1~10)：")
        while True:
            try:
                self.attack_position = int(enemy_position)
                break
            except ValueError:
                enemy_position = input("攻击位置输入错误！请重新输入(1~10)：")
                continue
        print("我方坦克正在向敌方位置 {} 发送子弹...".format(self.attack_position))


# 定义敌方坦克类，继承于基础坦克类
class PCTank(BaseTank):
    def move(self):
        self.position = random.randint(1, 10)

    def bullet_launch(self):
        self.attack_position = random.randint(1, 10)
        print("敌方坦克正在向玩家位置 {} 发送子弹...".format(self.attack_position))


my_tank = MyTank()
pc_tank = PCTank()


while True:
    # 我方坦克移动
    my_tank.move()
    # 我方坦克攻击
    my_tank.bullet_launch()
    print("-------------------------------")
    # 敌方坦克移动
    pc_tank.move()
    # 敌方坦克攻击
    pc_tank.bullet_launch()

    # 我方坦克攻击敌方坦克
    pc_tank.hit(my_tank)
    if pc_tank.live == 0:
        print("游戏结束，我方坦克胜利")
        print("-------------结算--------------")
        print("我方坦克位置：{}，我方坦克攻击位置：{}".format(my_tank.position, my_tank.attack_position))
        print("敌方坦克位置：{}，敌方坦克攻击位置：{}".format(pc_tank.position, pc_tank.attack_position))
        print("我方坦克血量：{}，敌方坦克血量：{}".format(my_tank.HP, pc_tank.HP))
        print("-------------------------------")
        break
    # 敌方坦克攻击我方坦克
    my_tank.hit(pc_tank)
    if my_tank.live == 0:
        print("游戏结束，敌方坦克胜利")
        print("-------------结算--------------")
        print("我方坦克位置：{}，我方坦克攻击位置：{}".format(my_tank.position, my_tank.attack_position))
        print("敌方坦克位置：{}，敌方坦克攻击位置：{}".format(pc_tank.position, pc_tank.attack_position))
        print("我方坦克血量：{}，敌方坦克血量：{}".format(my_tank.HP, pc_tank.HP))
        print("-------------------------------")
        break

    print("-------------结算--------------")
    print("我方坦克位置：{}，我方坦克攻击位置：{}".format(my_tank.position, my_tank.attack_position))
    print("敌方坦克位置：{}，敌方坦克攻击位置：{}".format(pc_tank.position, pc_tank.attack_position))
    print("我方坦克血量：{}，敌方坦克血量：{}".format(my_tank.HP, pc_tank.HP))
    print("-------------------------------")


