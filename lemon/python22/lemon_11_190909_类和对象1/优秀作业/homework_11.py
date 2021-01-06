# -*- coding: utf-8 -*-
# time:2019/9/1010:35
# author：小水
# E-mail：416682054@qq.com
# file：homework_11.py
#
#
# 1、实现一个手机类，并实例化你的手机。
#
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
#
# 尽量多的获取不同属性和使用不同的功能。
class MobilePhone:
    name = '华为'
    number = 'p30'
    point = 'call'
    point_01 = 'message'
    def __init__(self,colour,price):
        self.colour = colour
        self.self = price

my_phone = MobilePhone('black','cheap')
print(my_phone)

# 2、
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
#
#
# a.根据以上信息，抽象出一个类
class Cat:
    colour = 'grep'
    eat = 'delision'
    drunk = 'coco'
    heart = 'enjoy'
# # b.定义相关属性，并能在类的外面调用
class Cat:
    colour = 'grep'
    eat = 'delision'
    drunk = 'coco'
    heart = 'enjoy'
print(Cat.colour)
# # c.定义相关方法，在方法中打印相应信息
class Cat:
    colour = 'grep'
    eat = 'delision'
    drunk = 'coco'
    heart = 'enjoy'
    def __init__(self):
        print('完美')
Cat()
# # 3.列举3个生活中类和对象的例子，用代码表示。
class ChenXuYuan:
    hair = 'little'
    sport = 'sleep'
    eat = '下午茶'
    work = '加班'
    def __init__(self,clothes):
        self.clothes = clothes

driver = ChenXuYuan('衬衫')
print(driver)

class TeaShop:
    tea = '铁观音'
    cuostmer = '爱喝茶'
    favor = '喝茶聊天'
    sport = '包茶叶'
    def __init__(self,taetype,teabag):
        self.taetype = taetype
        self.teabag = teabag

tea_01 = TeaShop('普洱','小泡茶')
print(tea_01)

class ShiTang:
    eatman = 'student'
    price = 'cheape'
    eat_type = '多种多样'
    drunk = 'shop'
    def __init__(self,drunking,aetname):
        self.drunking = drunking
        self.aetname = aetname

eat_01 = ShiTang('可乐','炒面')
print(eat_01)
# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
#
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
#
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant:
    restaurant_name = '火锅'
    cooking_type = '蔬菜'
    point = 'call'
    point_01 = 'message'
    def __init__(self,name,cook):
        self.nanme = name
        self.cook = cook

def describe_restaurant():
    return'四川火锅，涮菜'

def open_restaurant():
    return 'open'

restaurant = Restaurant('四川火锅','大白菜')
print(restaurant)
print(describe_restaurant())
print(open_restaurant())


