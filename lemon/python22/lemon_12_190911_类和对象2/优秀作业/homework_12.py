# -*- coding: utf-8 -*-
# time:2019/9/1517:00
# author：小水
# E-mail：416682054@qq.com
# file：homework_12.py


# ======必做题==========
# 0、使用思维导图总结梳理类与对象相关知识点
# 1.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
class Computer:
    add = '+'
    dele = '-'
    cheng = '*'
    chu = '/'

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def adder(self):
        self.num1 += self.num2
        print(self.num1)

    def deler(self):
        self.num1 -= self.num2
        print(self.num1)

    def chenger(self):
        self.num1 *= self.num2
        print(self.num1)

    def chuer(self):
        result = self.num1/self.num2
        print(result)
haha =Computer(4,4)
haha.adder()
haha.deler()
haha.chenger()
haha.chuer()

# 2：编程题
# 人和机器猜拳游戏写成一个类，有如下几个函数：
#
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random
class HumanVSMachine:
    def choose_role(self):
        while True:
            role_info = {"1": "曹操", "2": "张飞", "3": "刘备"}
            role_num = input("请选择你喜欢的角色：1：曹操 2：张飞 3：刘备")
            if role_num in role_info.keys():
                print("你选择的角色是%s" % role_info[role_num])
                break
            else:
                print("角色选择错误，请重新选择！")
                continue
        # 返回一个值  返回角色值
        return role_info[role_num]

    # 方法一：
    def cq(self, role, mode):  # mode=1  人出拳 mode=2  就是电脑出拳
        cq_info = {"1": "石头", "2": "剪刀", "3": "布"}
        if mode == 1:
            cq_num = input("请输入对应的数字出拳:1石头 2剪刀 3布")
        elif mode == 2:
            cq_num = str(random.randint(1, 3))
        if cq_num in cq_info.keys():
            print(role + "出的是%s" % cq_info[cq_num])
        else:
            print("出拳错误！")
        return cq_num

    # 方法二：
    # def role_cq(self,role_name):
    #     cq_num=input("请输入对应的数字出拳:1剪刀 2石头 3布")
    #     cq_info={"1":"剪刀","2":"石头","3":"布"}
    #     if cq_num in cq_info.keys():
    #         print(role_name+",你出的是%s"%cq_info[cq_num])
    #     else:
    #         print("出拳错误！")
    #     return cq_num
    #
    # def machine_cq(self):
    #     cq_num=str(random.randint(1,3))#需要转换一下格式
    #     cq_info={"1":"剪刀","2":"石头","3":"布"}
    #     if cq_num in cq_info.keys():
    #         print("电脑出的是%s"%cq_info[cq_num])
    #     else:
    #         print("出拳错误！")
    #     return cq_num#字符串

    def human_vs_machine(self):
        # 人机对战
        role = self.choose_role()  # 角色
        # 变量：
        human_win = 0
        ping = 0
        machine_win = 0
        while True:
            # 方法一：
            # human_cq=int(self.role_cq(role))#角色出拳
            # machine_cq=int(self.machine_cq())#机器出拳
            # 方法二
            human_cq = int(self.cq(role, 1))
            machine_cq = int(self.cq("电脑", 2))

            if human_cq != machine_cq:  # 数值比较 1 石头  2 剪刀  3布
                if human_cq == 1 and machine_cq == 2:
                    human_win += 1
                elif human_cq == 2 and machine_cq == 3:
                    human_win += 1
                elif human_cq == 3 and machine_cq == 1:
                    human_win += 1
                else:
                    machine_win += 1
            else:
                ping += 1
            choice = input("是否要继续猜拳？按y继续，按n退出")
            if choice == 'y':
                continue
            else:
                break
        print("对战结束：人赢了%s局,电脑赢了%s局,平了%s局" % (human_win, machine_win, ping))

HumanVSMachine().human_vs_machine()
# 3、实现文字版游戏：坦克大战
# 步骤一：定义TANK类：
# 1、实现一个BaseTank类（所有Tank的父类）
# BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
# BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
# BeseTank拥有HP属性（代表血量，默认为10）
# BeseTank拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）BeseTank拥有HP属性（代表血量，默认为10）
# BaesTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
# 2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
# move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
# Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
# 3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
# move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
# Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），
#
# 步骤二：选做题（扩展题，不要求提交）
#
# 2、游戏环节（循环，直到有tank死亡才退出循环）
# 1、玩家发生子弹，然后电脑坦克发射子弹，
# 2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
# 3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
# 4、玩家移动、电脑移动
import random

class BaseTank:
    def __init__(self):  # 初始化
        self.live = live  # 1代表活的，0代表死
        self.postion = str(random.randint(1, 10))
        self.attck_postion = str(random.randint(1, 10))
        self.Pblood = 10  # 玩家血量
        self.Eblood = 10  # 其它坦克血量

    def hit(self,other):  # 开始一个游戏
        other_postion = str(random.randint(1, 10))
        if other_postion == self._postion:
            self.Pblood -=1
            if self.Pblood ==0:
                self.live = 0


class MyTank:
    def __init__(self):  # 初始化
        self.live = live  # 1代表活的，0代表死
        self.postion = str(random.randint(1, 10))
        self.attck_postion = str(random.randint(1, 10))
        self.Pblood = 10  # 玩家血量
        self.Eblood = 10  # 其它坦克血量

    def move(self):
        postion = input('请输入移动的目标位置')
        if postion in range(1,11):
            self.postion == postion
        else:
            print('输入无效数据，重新输入')

    def  Bullet_launch(self):
        optiom = input('请输入攻击目标位置')
        if optiom in range(1, 11):
            self.postion == optiom
        else:
            print('输入无效数据，重新输入')

class  PCTank:
    def __init__(self):  # 初始化
        self.live = live  # 1代表活的，0代表死
        self.postion = str(random.randint(1, 10))
        self.attck_postion = str(random.randint(1, 10))
        self.Pblood = 10  # 玩家血量
        self.Eblood = 10  # 其它坦克血量

    def move(self):
        self.postion = (1,10)

    def Bullet_launch(self):
        optiom = (1,10)

