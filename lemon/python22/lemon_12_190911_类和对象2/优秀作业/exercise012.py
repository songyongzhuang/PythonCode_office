import random


# 1.编写如下程序：编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cal_add(self):
        return self.x + self.y

    def cal_minus(self):
        return self.x - self.y

    def cal_multiply(self):
        return self.x * self.y

    def cal_divide(self):
        return self.x / self.y


cal = Calculator(3, 4)
print(cal.cal_add())
print(cal.cal_minus())
print(cal.cal_multiply())
print(cal.cal_divide())

"""
2：编程题
人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
"""


class Game:
    character_dict = {1: '曹操', 2: '张飞', 3: '刘备'}
    result = {'曹操': 0, '张飞': 0, '刘备': 0, 'computer': 0, 'draw': 0}

    @staticmethod
    def select_character():
        while True:
            character = input("请选择角色:")
            if int(character) in (1, 2, 3):
                character_name = Game.character_dict[int(character)]
                return character_name
            else:
                return '角色选择错误，请重新选择'

    @staticmethod
    def character_choice():
        while True:
            # 1为剪刀，2为石头，3为布
            choice = input("请输入一个1-3的数字：")
            if int(choice) in (1, 2, 3):
                character_choice = int(choice)
                return character_choice
            else:
                return '数字输入错误，请重新输入'

    @staticmethod
    def computer_choice():
        computer_choice = random.randint(1, 3)
        return computer_choice

    @staticmethod
    def battle():
        while True:
            battle_character = Game.select_character()
            character_choice = Game.character_choice()
            computer_choice = Game.computer_choice()

            if character_choice == computer_choice:
                print('本局对战结果平局')
                Game.result['draw'] += 1
            elif (character_choice, computer_choice) in (1, 3) or (2, 1) or (3, 2):
                print('{}赢，电脑输'.format(battle_character))
                Game.result[battle_character] += 1
            elif (character_choice, computer_choice) in (1, 2) or (2, 3) or (3, 1):
                print('电脑赢，{}输'.format(battle_character))
                Game.result['computer'] += 1

            game_continue = input('是否继续？按y继续，按n退出')
            if game_continue == 'y':
                continue
            elif game_continue == 'n':
                print('曹操赢{}局，张飞赢{}局，刘备赢{}局，电脑赢{}局，平局{}次，游戏结束'.format(
                    Game.result['曹操'], Game.result['张飞'], Game.result['刘备'], Game.result['computer'],
                    Game.result['draw']
                ))
                break


Game.battle()

"""
3、实现文字版游戏：坦克大战
步骤一：定义TANK类：
1、实现一个BaseTank类（所有Tank的父类）
BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
BaseTank拥有position属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
BaseTank拥有HP属性（代表血量，默认为10）
BaseTank拥有attack_position属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）BaseTank拥有HP属性（代表血量，默认为10）
BaseTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10）
"""


# 步骤一，定义一个tank类，1.实现一个BaseTank类（所有Tank的父类）
class BaseTank:
    def __init__(self, live=1, hp=10):
        self.live = live
        self.position = random.randint(1, 10)
        self.hp = hp
        self.attack_position = random.randint(1, 10)

    def hit(self, other):
        if self.position == other.attack_position:
            self.hp -= 1
            if self.hp == 0:
                self.live = 0
                return '有坦克已阵亡！存活下来的坦克胜利！'


# 2.实现一个玩家坦克类，MyTank,继承于BaseTank
class MyTank(BaseTank):
    def move(self):
        while True:
            try:
                position = input('请输入目标位置:')
                if int(position) in range(1, 11):
                    self.position = position
                else:
                    print('请输入1-10的数据')
            except ValueError:
                print('无效数据，请重新输入')

    def bullet_launch(self):
        while True:
            try:
                bullet_position = input('请输入目标位置:')
                if int(bullet_position) in range(1, 11):
                    self.attack_position = bullet_position
                else:
                    print('请输入1-10的数据')
            except ValueError:
                print('无效数据，请重新输入')


# 3.实现一个电脑坦克类，MyTank,继承于BaseTank
class PCTank(BaseTank):
    def move(self):
        while True:
            try:
                position = input('请输入目标位置:')
                if int(position) in range(1, 11):
                    self.position = position
                else:
                    print('请输入1-10的数据')
            except ValueError:
                print('无效数据，请重新输入')

    def bullet_launch(self):
        while True:
            try:
                bullet_position = input('请输入目标位置:')
                if int(bullet_position) in range(1, 11):
                    self.attack_position = bullet_position
                else:
                    print('请输入1-10的数据')
            except ValueError:
                print('无效数据，请重新输入')


"""
步骤二：选做题（扩展题，不要求提交）
2、游戏环节（循环，直到有tank死亡才退出循环）
1、玩家发生子弹，然后电脑坦克发射子弹，
2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
4、玩家移动、电脑移动
"""
player_tank = MyTank()
pc_tank = PCTank()
# 循环，直到有tank死亡才退出循环
while player_tank.live == 1 and pc_tank.live == 1:
    # 玩家和电脑互相发射子弹
    player_tank.bullet_launch()
    pc_tank.bullet_launch()
    # 判断互相之间是否击中
    player_tank.hit(pc_tank)
    pc_tank.hit(player_tank)
    # 判断玩家和电脑是否存活，有一方live属性为0则跳出循环
    if player_tank.live == 0:
        print('玩家坦克阵亡，电脑赢！')
        break
    elif pc_tank.live == 0:
        print('电脑坦克阵亡，电脑赢！')
        break
    # 有任意一方存活的情况下，继续游戏，玩家移动，电脑移动
    else:
        player_tank.move()
        pc_tank.move()
