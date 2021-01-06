#-*- coding:utf-8 -*-
#@Time: 2019/9/118:52
#@Author:深圳+朱朱+python22
#@File:homework0909.py
#@Software: PyCharm

#1、实现一个手机类，并实例化你的手机。
class  MobilePhone(object): #定义一个手机类
    def __init__(self, brand, type, color,weight, size):
        #类的属性
        self.brand=brand
        self.type=type
        self.color=color
        self.weight=weight
        self.size=size
    #类的方法
    #介绍手机
    def printphone(self):
        print("手机品牌为：{}".format(self.brand))
        print("手机型号为：{}".format(self.type))
        print("手机颜色为：{}".format(self.color))
        print("手机重量为：{}".format(self.weight))
        print("手机屏幕尺寸为：{}".format(self.size))

    def  callphone(self,telnum):
        print("我正在给{}打电话".format(telnum))


    def sendmesg(self,telnum,content):
        print("我正在给{}发短信，短信内容为{}".format(telnum,content))


    def watchvedio(self):
        print("正在用手机看视频")

#实例化类会自动调用__init__函数初始化对象,方法：类名（参数）
my_phone=MobilePhone('华为','荣耀','蓝色','0.1',5)
my_phone.printphone()
my_phone.callphone('13767678987')
my_phone.sendmesg('13765456765','hello')
my_phone.watchvedio()

#实例2
my_phone=MobilePhone('苹果','6','粉色','0.2',7)
my_phone.printphone()
my_phone.callphone('137676876655')
my_phone.sendmesg('1376540000','你吃饭没')
my_phone.watchvedio()


'''2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息'''
class Cat(object):
    #初始化函数
    def __init__(self,name,age,color):
        #类的属性
        self.name=name
        self.age=age
        self.color=color
    #类的方法
    def eatfood(self,food):
        print("{}正在吃{}".format(self.name,food))

    def drink(self,juice):
        print("{}正在喝{}".format(self.name,juice))


#实例化对象
cat=Cat("Tom",1,'灰色')
cat.eatfood('5条鱼')
cat.drink('可口可乐')

#3.列举3个生活中类和对象的例子，用代码表示。
#人类
class Person(object):
    def __init__(self,name,age,sex,height,weight):
        self.name=name
        self.age=age
        self.sex=sex
        self.height=height
        self.weight=weight


    def introduceself(self):
        print("简单介绍下自己：我的名字为：{}，我是{}生，我今年{}岁了，我的身高为{}cm，我的体重为{}kg".format(self.name,self.sex,self.age,self.height,self.weight))


    def eatfood(self,food):
        print('我最喜欢吃的东西是{}'.format(food))

    def sing(self,song):
        print('我喜欢唱{}歌'.format(song))

p1=Person('xiaoming',18,'female',180,70)
p1.introduceself()
p1.eatfood('鸡肉')
p1.sing('小星星')


#房子类
class House(object):
    def __init__(self,area,color,price):
        self.area=area
        self.color=color
        self.price=price


    def printinfo(self):
         print('这个房子面积为{}平方，{}颜色，价格为{}万'.format(self.area,self.color,self.price))

    def liveperson(self,num):
        print('这个房子可以住{}几个人'.format(num))

bighouse=House(200,'白色',200)
bighouse.printinfo()
bighouse.liveperson(6)


#汽车类
class Car(object):
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price

    def printinfo(self):
        print('汽车品牌为{},{}颜色，价格为{}万'.format(self.brand,self.color,self.price))

    def run(self):
        print('汽车可以跑')

car=Car('宝马','白色',100)
car.printinfo()
car.run()






'''4.编写如下程序
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。'''

class Restaurant(object):
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type

    def open_restaurant(self):
        print('本店今天营业，欢迎进店品尝！！')

    def describe_restaurant(self):
        print("这家饭店名称为：{}".format(self.restaurant_name))
        print('这里有美味的美食,欢迎品尝')
        for item in self.cooking_type:
            print('美食： {}'.format(item))



cook_type=['蛋炒饭','宫保鸡丁','鱼香肉丝','剁椒鱼头','麻婆豆腐','小炒肉']
res=Restaurant("来一碗",cook_type)
res.open_restaurant()
res.describe_restaurant()
