# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 190916_练习.py
# Author       : Administrator
# Create time  : 2019-09-12 10:11
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

"""
class Game:

    logo = True

    # 实例属性
    def __init__(self, name):
        self.name = name

    @classmethod  # 声明使用的是类方法, 实例方法是不需要声明的
    def if_logo(cls):
        # cls 类方法  cls表示类本身
        print(cls.logo)

    # 静态方法
    @staticmethod
    def check_weather():
        print('天气')


for i in range(3):
    print(i)  # 0 1 2
"""

"""
def offer(name, money, time):
    print("{}, {}, {}".format(name, money, time))
    eat(name,'大辣皮')


def eat(name, food):
    print('{}, {}'.format(name,food))


offer('dalao', 50, 1)
"""


# class InterViewer:
#
#     def __init__(self, name):
#         self.name = name  # 简化了调用过程
#
#     def offer(self,money, time):
#         print("大佬{}收到了一个offer, 月薪{}K, 需要{}天到岗".format(self.name, money, time))
#         self.eat('大辣皮')
#
#     def eat(self, food):
#         print('{}爱吃{}'.format(self.name, food))
#
#     def interviwing(self):
#         print('--面试--')
#
#
# dalao = InterViewer('海绵')  # 函数创建对象类名称后面一定要加()加()加()
# print(dalao.offer(50,1))
# dalao.interviwing()


class Game:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        name_dict = {1: '曹操', 2: '张飞', 3: '刘备'}
        real_name = name_dict[self.name]
        return real_name

    def get_player_guess(self):
        a = int(input('请输入1-3任一数字:'))
        return a

    def get_pc_random(self):
        import random
        b = random.randint(1, 3)
        return b

    def game_result(self):
        game_dict = {1: '剪刀', 2: '石头', 3: '布'}
        count_1 = 0
        count_2 = 0
        count_3 = 0

        while True:
            player_guess = self.get_player_guess()
            pc_guess = self.get_pc_random()

            print(self.get_name() + '出拳：', game_dict[player_guess])
            print('电脑出拳：', game_dict[pc_guess])

            if player_guess == pc_guess:
                count_1 = count_1 + 1
                print('平局')
            elif (player_guess == 1 and pc_guess == 3) \
                    or (player_guess == 2 and pc_guess == 1) \
                    or (player_guess == 3 and pc_guess == 1):
                count_2 = count_2 + 1
                print(self.get_name() + '胜')
            else:
                count_3 = count_3 + 1
                print('电脑胜')

            again = input('是否继续？y/n:')

            if again == 'n':
                print(self.get_name() + '赢：' + str(count_2) + '局')
                print('电脑赢：' + str(count_3) + '局')
                print('平局：' + str(count_1))
                print('游戏结束')
                break


game = Game(2)
game.game_result()
