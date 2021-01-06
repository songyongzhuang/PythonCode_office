# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。

# class Mobile:
#     brand = ''
#     type = ''
#     def __init__(self, b, t):
#         self.brand = b
#         self.type = t
#
#     def Dial(self, num):
#         print('正在呼叫的号码为：{}'.format(num))
#
#
#     def Sms(self, num, content):
#         print('给{}的号码发送的短信为{}'.format(num, content))
#
#
# mobile1 = Mobile('vivo', 'uda-x21')
# mobile1.Dial(133847878787)
# mobile1.Sms(12357455252, 'dhaosdaosdhncasfh')
# print(mobile1.brand)

# 2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息
# class Cat:
#     age = 0
#     color = ''
#     name = ''
#     def __init__(self, age, color,name):
#         self.age = age
#         self.color = color
#         self.name = name
#
#     def eat(self, food, drink, statu):
#         print('{}的{}猫,今年{}岁，吃着{}的食物，喝着{}的饮料，非常{}的样子'
#               .format(self.color, self.name, self.age, food, drink, statu))
#
#
# cat = Cat(1, '灰色', 'Tom')
# cat.eat('美味', '可口', '享受')

# 3.列举3个生活中类和对象的例子，用代码表示。
# class Man:
#     name = ''
#     age = ''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print('吃东西')
#
# man = Man('波浪线', '20')
# man.eat()
#
# class Car:
#     num = 0
#     color = ''
#     def __init__(self, num ,color):
#         self.num = num
#         self.color = color
#
#     def shache(self):
#         print('shache')      #还有前进后退等方法
#
# car = Car(2012221, '白色')
# car.shache()
#
#
# class Movie:
#     name = ''
#     date = ''
#     time = ''
#     def __init__(self, name, date, time):
#         self.name = name
#         self.date = date
#         self.time = time
#
# movie = Movie('罗小黑', '2019.9.10', '120')

# 4.编写如下程序创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# # a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名
# # 为 open_restaurant()的方法（显示饭店正在营业）。
# # b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant:
    restaurant_name = ''
    cooking_type = ''

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cooking_type = type

    def describe_restaurant(self):
        print('饭店名：{} 美食种类：{}'.format(self.restaurant_name, self.cooking_type))

    def open_restaurant(self):
        print('正在营业')

restaurant = Restaurant('和平饭店', '甜点，炒菜，粉类')
print(restaurant.restaurant_name+'  '+restaurant.cooking_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

