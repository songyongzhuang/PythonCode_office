#@time:15:25
#@author:tianhongsheng
#@file:homework_tianhs_0910

# 第一题：实现一个手机类，并实例化你的手机。 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。
# class Moblie:
#     #初始化函数
#     def __init__(self,brand,xinghao):
#         self.brand=brand
#         self.xinghao=xinghao
#
#     def tel(self):
#         print("我打电话的手机是：",self.brand)
#
#     def faduanxin(self):
#         print("我发短信的手机型号是：",self.xinghao)
#
#
# mb = Moblie("华为","p20")
# mb.tel()
# mb.faduanxin()


#第二题：
# class Tom:
#     age=2
#     def __init__(self,name,color,food):
#         self.name=name
#         self.color=color
#         self.likefood=food
#
#     def eat(self):
#         print("我的名字叫%s,今年%s岁了，我喜欢吃%s"%(self.name,self.age,self.likefood))
#
#
# tom = Tom("小白","白色","鱼")
# tom.eat()


#第三题列举3个生活中类和对象的例子，用代码表示。
#
#车类
# class car:
#     xinghao="奔驰"
#     chepaihao="桂A88888"
#     color="红色"
#
#     def seed(self):
#         print("速度150m/km")

#人类
# class people:
#     def __init__(self,name,hight):
#         self.name=name
#         self.hight=hight
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass

# #动物类
# class Animal:
#
#     # 方法
#     def __init__(self, name):
#         self.name = name
#
#     def printName(self):
#         print('名字为:%s'%self.name)


# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
#
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


# class Restaurant:
#     def __init__(self,restaurant_name,cooking_type):
#         self.restaurant_name=restaurant_name
#         self.cooking_type=cooking_type
#         print(self.restaurant_name)
#         print(self.cooking_type)
#      #饭店信息描述
#     def describe_restaurant(self):
#         print("{}的{}非常美味！".format(self.restaurant_name,self.cooking_type))
#     #饭店正在营业
#     def open_restaurant(self):
#         print("%s饭店正在营业！"%self.restaurant_name)


# restaurant = Restaurant("南宁饭店","川菜")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()



