#!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @Author : duxiaocui
#######第一题######
# info = {"1": "查看手机信息", "2": "查看手机功能", "3": "打电话", "4": "发短信", "5": "退出"}  # 全局变量
# class Phone_2(object):  # 创建一个类
#     def __init__(self, brand, model, memory, resolution):  # 实例属性初始化
#         self.brand = brand
#         self.model = model
#         self.memory = memory
#         self.resolution = resolution
#
#     def function(self, texting, information):
#         self.texting = texting
#         self.information = information
#
#     def send(self, send_name, send_number, send_content):
#         self.send_name = send_name
#         self.send_number = send_number
#         self.send_content = send_content
#
#     def call(self, call_number):
#         self.call_number = call_number
#
#     def judge(self, judge_name):  # 类方法
#         self.judge_name = judge_name
#
#     def out_attribute(self):  # 类方法
#         print(f"这是一个{phone.brand}手机,手机的型号是：{phone.model},手机的内存是：{phone.memory},手机的分辨率是:{phone.resolution}")
#
#     def out_function(self):  # 类方法
#         print(f"手机的功能包括：{phone.texting}{phone.information}" )
#
#     def out_send(self):  # 类方法
#         print(f"已经给{phone.send_name} {phone.send_number}女士，发送成功，内容为:{phone.send_content}")
#     def out_call(self):  # 类方法
#         print(f"已经拨打{phone.call_number}电话，请注意接听！")
#
#
# phone = Phone_2("华为", "华为p10", "6g", "1080")  # 实例对象
# phone.function("发短信", "打电话")  # 改变实例属性
# phone.send("兜兜", "13520820169", "我喜欢你！")  # 改变实例属性
# phone.call("13520820169")  # 改变实例属性
# while True:
#     phone.judge(input("请选择您要进行的功能【1】查看手机信息【2】查看手机功能【3】打电话【4】发短信：【5】退出：")) # 访问类方法
#     if phone.judge_name in info.keys():
#         if phone.judge_name == "1":
#             phone.out_attribute()  # 访问类方法
#         elif phone.judge_name == "2":
#             phone.out_function()  # 访问类方法
#         elif phone.judge_name == "3":
#             phone.out_send()  # 访问类方法
#         elif phone.judge_name == "4":
#             phone.out_call()  # 访问类方法
#         else:
#             print("结束")
#             break
#     else:
#         print("输入错误，请重新选择")

######第二题#######
# class Tom():
#     def __init__(self,age,color,like):
#         self.age = age
#         self.color = color
#         self.like = like
#     def out_data(self):
#         print(f"{tom.color}Tom猫，今年{tom.age}岁，{tom.like},非常享受的样子，惹人爱！")
#
# tom = Tom("1","灰色的","吃着美味的食物，喝着可口的饮料")
# tom.out_data()
#######第三题######
###第一个例子
#class Drinks():
#     def __init__(self,species,ml):
#         self.species = species
#         self.ml = ml
#
#     def out_drinks(self):
#         print(f"我喜欢喝{drinks.ml}的{drinks.species}")
#
# drinks =  Drinks ("旺仔牛奶", "100ml")
# drinks.out_drinks()
# ##第二个例子
# class Flowers():
#     def __init__(self,classification,color,function):
#         self.classification = classification
#         self.color = color
#         self.function = function
#     def out_flowers(self):
#         print(f"{flowers.color}的{flowers.classification}，有{flowers.function}的功效")
#
# flowers = Flowers("玫瑰花", "红色", "美容养颜")
# flowers.out_flowers()
# ##第三个例子
# class Fruit():
#     def __init__(self,kinds,taste):
#         self.kinds = kinds
#         self.taste = taste
#     def out_fruit(self):
#         print(f"{fruit.kinds}是{fruit.taste}")
# fruit = Fruit("葡萄", "甜甜的")
# fruit.out_fruit()

######第四题#######
# class Restaurant(object):
#     def __init__(self,restaurant_name,cooking_type):  # 实例属性
#         self.restaurant_name = restaurant_name
#         self.cooking_type = cooking_type
#     def describe_restaurant(self):    # 类方法
#         print(f"{restaurant.restaurant_name}主要美食种类是:{restaurant.cooking_type}")
#     def open_restaurant(self):    # 类方法
#         print(f"{restaurant.restaurant_name}正在营业，欢迎进店品尝！")
# restaurant = Restaurant("二丫的店","东北菜")    # 实例对象
# restaurant.describe_restaurant()    # 实例方法
# restaurant.open_restaurant()        # 实例方法