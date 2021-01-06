# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : lemon_190911_作业.py
# Author       : Administrator
# Create time  : 2019-09-12 09:46
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！


# 0911-类和对象2 作业
# 截至：09月16日  14:00展示词云
# 1.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。


class Calculator:

    def __init__(self, figure_01=0.0, figure_02=0.0):
        self.figure_01 = figure_01
        self.figure_02 = figure_02

    def plus(self, operation):
        try:
            figure = f"{self.figure_01}{operation}{self.figure_02}"
            return '计算{}{}{}结果为：{}'.format(self.figure_01, operation, self.figure_02, eval(figure))
        except TypeError:
            print('做错了，怎么办？')
            return '重新输入'
        except SyntaxError:
            print('做错了，怎么办？')
            return '重新输入'


calculator = Calculator(5.5, 5.5)
print(calculator.plus("+"))


class Calculator:

    # def __init__(self, figure_01=0.0, figure_02=0.0):
    #     self.figure_01 = figure_01
    #     self.figure_02 = figure_02

    def addition(self, figure_01, figure_02):
        try:
            figure = figure_01 + figure_02
            return f'{figure_01}+{figure_02}={figure}'
        except TypeError:
            print('做错了，怎么办？')
            return '重新输入'
            
    def subtract(self, figure_01, figure_02):
        try:
            figure = figure_01 - figure_02
            return f'{figure_01}-{figure_02}={figure}'
        except TypeError:
            print('做错了，怎么办？')
            return '重新输入'

    def multiply(self, figure_01, figure_02):
        try:
            figure = figure_01 * figure_02
            return f'{figure_01}*{figure_02}={figure}'
        except TypeError:
            print('做错了，怎么办？')
            return '重新输入'

    def division(self, figure_01, figure_02):
        try:
            figure = figure_01 / figure_02
            return '{}/{}={:2}'.format(figure_01, figure_02, figure)
        except TypeError:
            print('做错了，怎么办？')
            return '重新输入'


calculator = Calculator()
print(calculator.addition(1, 2))  # 加
print(calculator.subtract(2, 3))  # 减
print(calculator.multiply(3, 4))  # 乘
print(calculator.division(4, 5))  # 除



#
#
# 2：编程题
# 人和机器猜拳游戏写成一个类，有如下几个函数：
#
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束


class Game:

    def hero_select(self, hero_number):
        """
        定义一个英雄 ,写一个字典，获取用户输入数字，来挑选英雄
        记录用户选择的英雄，给下面函数使用
        """
        hero_name = {1: '曹操', 2: '张飞', 3: '刘备'}
        hero = hero_name[hero_number]
        # print('您选择的英雄是:{}'.format(hero))
        return hero

    def hero_fist(self, fist_number):
        """
        拳, 定义拳，获取用户输入
        写一个字典，获取用户输入数字，来挑选拳
        """
        fist = {1: '石头', 2: '剪刀', 3: '布'}
        weapon = fist[fist_number]
        # print('您选择的武器是:{}'.format(weapon))
        return weapon

    def hrobot_fist(self):
        """
        记录电脑出拳  import random
        随机数：random.randint(1, 3)
        根据随机数获取电脑的拳
        """
        import random
        fist = {1: '石头', 2: '剪刀', 3: '布'}
        random_01 = random.randint(1,3)
        quan = fist[random_01]
        # print('电脑武器:{}'.format(quan))
        return quan

    def judgment(self):
        """ 判断
        根据获取玩家的角色、拳和电脑的拳进行判断
        设置变量保存输赢几局
        """
        victory = 0  # 胜利
        lose = 0  # 输
        dogfall = 0  # 平局

        while True:
            select_hero = input('请选择你需要的英雄：1: 曹操, 2: 张飞, 3: 刘备\n请输入您的选择：')
            hero = game.hero_select(int(select_hero))
            print(f'您选择的英雄为{hero}')
            serial = input(f'请选择{hero}需要的拳：1: 石头, 2: 剪刀, 3: 布\n请输入您的选择：')
            player = game.hero_fist(int(serial))  # 玩家选择的拳
            robot = game.hrobot_fist()  # 电脑选择的拳
            print(f'英雄{hero}出拳为：{player}')
            print(f'电脑出拳为：{robot}')
            if player == robot:
                dogfall += 1
                print(f'英雄{hero}出拳为：{player}, 电脑出拳为：{robot}, 平局.\n')
            elif (player == '石头' and robot == '剪刀') \
                or (player == '剪刀' and robot == '布') \
                or (player == '布' and robot == '石头'):  # 进行游戏规则的判断
                victory += 1
                print(f'英雄{hero}出拳为：{player}, 电脑出拳为：{robot}, 英雄{hero}胜利了.\n')
            else:
                lose += 1
                print(f'英雄{hero}出拳为：{player}, 电脑出拳为：{robot}, 英雄{hero}失败了.\n')

            e = input('是否继续？任意键继续，按n退出')
            if e == 'n':
                print(f'游戏结束，角色赢{victory}局 电脑赢{lose}局，平局{dogfall}次')
                break
            else:
                print('游戏继续')


game = Game()
game.judgment()

#
#
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
