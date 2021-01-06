# -*- coding:utf-8 -*-
# @Time : 2019-09-12 08:31
# @Author : 潘潘达
# @File : day11.py

"""
1.编写如下程序：编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
"""


class MathCalculation(object):
    # 定义初始化方法，需传入两个用于计算的数字
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    # 加法
    def addition(self):
        result = self.num_first + self.num_second
        return result

    # 减法
    def subtraction(self):
        result = self.num_first - self.num_second
        return result

    # 乘法
    def multiplication(self):
        result = self.num_first * self.num_second
        return result

    # 除法
    def division(self):
        result = self.num_first / self.num_second
        return result


# 实例化一个MathCalculation类
cal = MathCalculation(2, 1)
# 调用cal对象的属性方法
print(cal.addition())
print(cal.division())
print(cal.multiplication())
print(cal.subtraction())


"""
2、编程题:人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色 1曹操 2张飞 3刘备
2）函数2：角色猜拳 1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
"""
import random


# 定义玩游戏类
class PlayGame(object):
    # 将角色字典定义为类变量
    roles = {
        "1": "曹操",
        "2": "张飞",
        "3": "刘备"
    }
    # 将出拳字典定义为类变量
    game_punches = {
        "1": "剪刀",
        "2": "石头",
        "3": "布"
    }
    # 定义用于统计胜局、败局、平局的变量
    victory = 0
    lose = 0
    ping = 0

    # 定义角色生成方法
    def role(self):
        while True:
            choice = input("请选择角色(曹操请输入1，张飞请输入2，刘备请输入3)：")
            if choice in self.roles.keys():
                role_name = self.roles[choice]
                return role_name
            else:
                print("输入角色代号错误!")
                continue

    # 定义玩家出拳方法
    def punches(self):
        while True:
            punch = input("请输入你的出拳(剪刀请输入1，石头请输入2，布请输入3)：")
            if punch in self.game_punches.keys():
                role_punch = self.game_punches[punch]
                return punch, role_punch
            else:
                print("输入出拳代号错误！")
                continue

    # 定义电脑出拳方法
    def computer(self):
        punch = random.randint(1, 3)
        computer_punch = self.game_punches[str(punch)]
        print("电脑出拳为：{}".format(computer_punch))
        return str(punch), computer_punch

    # 定义玩家与电脑猜拳的方法
    def pk(self):
        # 调用实例方法，生成玩家角色
        role_name = self.role()
        while True:
            # 调用实例方法，记录玩家出拳的数字
            role_punch_num = self.punches()[0]
            # 调用实例方法，记录电脑出拳的数字
            computer_punch_num = self.computer()[0]
            # 记录玩家的出拳
            computer_punch = self.game_punches[computer_punch_num]
            # 记录角色的出拳
            role_punch = self.game_punches[role_punch_num]
            # 判断角色赢的情况
            if (role_punch_num, computer_punch_num) in [("1", "3"), ("2", "1"), ("3", "2")]:
                print("电脑出拳{}，{}出拳{}，你赢了！".format(computer_punch, role_name, role_punch))
                # 计数器+1
                self.victory = self.victory + 1
            # 判断角色平局的情况
            elif role_punch_num == computer_punch_num:
                print("电脑出拳{}，{}出拳{}，平局！".format(computer_punch, role_name, role_punch))
                self.ping = self.ping + 1
            else:
                print("电脑出拳{}，{}出拳{}，你输了！".format(computer_punch, role_name, role_punch))
                self.lose = self.lose + 1
            # 是否继续游戏判断
            game_continue = input("是否想要继续游戏？继续请输入y，退出请输入n：")
            if game_continue == "y":
                continue
            elif game_continue == "n":
                # 调用实例方法，计算出赢的、输的、平的总局数
                game_result = self.result()
                print("角色{}赢了{}局，电脑赢了{}局，平局{}次，退出游戏...".format(role_name, game_result[0], game_result[1], game_result[2]))
                return None

    # 返回统计结果方法
    def result(self):
        return self.victory, self.lose, self.ping


punch_game = PlayGame()
punch_game.pk()

