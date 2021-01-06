# -*- coding:utf-8 -*-
# @Time   : 2019/9/11 11:02
# @Author : caoyq
# @Email  : 1456039626@qq.com
# @File   : home_work10.py

# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。

class MobilePhone:
    '''该类记录了手机的部分功能及使用'''

    def __init__(self, brand, model, number, sms, game):  # 手机的品牌，型号，功能等
        self.brand = brand
        self.model = model
        self.number = number
        self.sms = sms
        self.game = game

    def call(self):
        return '{}是iOS系统，号码是{}，我用的是{}'.format(self.brand, self.number, self.model)

    def texting(self):
        return '您收到一条短信,内容是{}，内容太短已自动屏蔽'.format(self.sms)

    def play_game(self):
        return '最喜欢的游戏是{}'.format(self.game)


resp = MobilePhone('iphone', 'ipone4s', 13111111111, '你好', '街机三国')  # 类对象化并用变量resp接收
print(resp.call())  # 对象调用类方法，并打印
print(resp.texting())
print(resp.play_game())


# 2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息
class MyCat():
    '''该类描述了猫的一些信息和行为'''

    # def __init__(self, name, age, food, drink):  也可以参数化
    #     self.name = name
    #     self.age = age
    #     self.food = food
    #     self.drink = drink

    name = 'Tom'
    age = 1
    food = '猫粮'
    drink = 'coffee'

    def cat(self):
        print('大家好，我叫{}，'
              '今年{}岁了，'
              '最喜欢吃的食物是{}，'
              '当然没事还喜欢翘着二郎腿喝的美味的饮料{}'.format(self.name, self.age, self.food, self.drink))


res = MyCat()
res.cat()
print(res.name)


# 3.列举3个生活中类和对象的例子，用代码表示。
class Car:
    '''该类主要说明部分品牌汽车的优点'''

    def __init__(self, name):
        self.name = name

    def bwm(self):
        print('{}的优点：操控性强的发动机，时尚有活力的外表'.format(self.name))

    def red_flag(self):
        print('{}的优点：安全性和舒适度高'.format(self.name))


Car('红旗').red_flag()


class MyComputer:
    '''该类写的是我喜欢的电脑'''

    def __init__(self, computer):
        self.computer = computer

    def computer_one(self):
        return '我最喜欢的电脑是{}'.format(self.computer)


resp_one = MyComputer('小米').computer_one()
print(resp_one)


class People:
    '''该类写的是神话人物及其故事'''

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def child(self):
        return '我叫{}，今年{}岁，最喜欢{}'.format(self.name, self.age, self.hobby)


resp_two = People('哪吒', 9, '闹东海').child()
print(resp_two)


# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant:
    '''该类描述了饭店的营业状态和营业范围'''

    def __init__(self, restaurant_name, cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        return '饭店名为{}，已有的美食种类有{}'.format(self.restaurant_name, self.cooking_type)

    def open_restaurant(self):
        return '饭店正在营业中'


restaurant = Restaurant('新月饭店', '中餐，中式面点，特色小吃，西餐')  # 类实例化
restaurant.describe_restaurant()  # 调用类方法
restaurant.open_restaurant()  # 调用类方法
