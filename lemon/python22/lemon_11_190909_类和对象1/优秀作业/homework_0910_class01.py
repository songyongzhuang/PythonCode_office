# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 11:28
# @Author  : Camille
# @Email   : 273322931@qq.com
# @File    : homework_0910.py
# @Software: PyCharm

# 1、实现一个手机类，并实例化你的手机。
#
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
#
# 尽量多的获取不同属性和使用不同的功能。


class TelePhone:
    # 类的属性

    def __init__(self,brand,version,system,color):
        self.brand = brand
        self.version = version
        self.system = system
        self.color = color
    def call_number(self):
        print(self.color+self.brand+'手机可以播打电话')
    def message_send(self):
        print(self.system+'手机还可以发短信')
    # 创建实例，调用类函数

telephone_01 = TelePhone('华为','8.0','android','黑色的')  # 创建对象


telephone_01.call_number()   #  实例调用类的方法
telephone_01.message_send()    # 实例调用类的方法
print(telephone_01.version)









# 2、
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息


class Cat:

   def __init__(self,name,age,color):
       self.name = name
       self.age = age
       self.color = color
   def do_what(self):
       print(str(self.age)+'的'+self.color+self.name+'正在吃着美味的食物，喝着可口的饮料，非常享受的样子')
cat_01 = Cat('Tom猫','1岁','灰色的')
cat_01.do_what()



# 3.列举3个生活中类和对象的例子，用代码表示。




class profession:

    def __init__(self,name,age,work,salary):
        self.name = name
        self.age =age
        self.work = work
        self.salary = salary
    def introduction(self):
        print(self.name+'今年'+str(self.age)+'现在在'+self.work+'工作'+'月薪'+self.salary)
    def married(self):
        print(self.name+'今年结婚了吗，有对象了吗？要不要给介绍一个对象')
    def work_01(self):
        print(self.work+'工资高吗？今年还能涨薪吗')

profession_01 = profession('Camille','18岁','杭州','10000')
profession_01.introduction()
profession_01.married()
profession_01.work_01()







# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
#
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。



class Restaurant:
    def __init__(self,restaurant_name,cooking_type):

        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type
    def describe_restaurant(self):
        print(self.restaurant_name+'里面的饭菜很好吃,'+'里面最好吃的就是'+self.cooking_type)
    def open_restaurant(self):
        print(self.restaurant_name+'饭店正在营业')

restaurant_jieshao = Restaurant('全聚德','烤鸭')
restaurant_jieshao.describe_restaurant()
restaurant_jieshao.open_restaurant()