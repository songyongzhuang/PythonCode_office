# !/usr/bin/env python3
# -*-coding:utf-8-*-
# @time    :2019/9/1015:38:18
# @Author  :天儿
# @Email   :839444324@qq.com
# @file    :Hmoework_tinaer_0909.py
# @Software:PyCharm Community Edition
#
# 0910-类和对象

# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。


class MobilePhone(object):
    have = '屏幕'  # 类属性，所有实例的共同特征

    def __init__(self, name, phone_num, mark, model, ram, space, system='Android 8.1.0'):  # 实例属性
        self.name = name   # 主人
        self.phone_num = phone_num # 电话号码
        self.mark = mark   # 品牌
        self.model = model  # 型号
        self.system = system  # 操作系统
        self.ram = ram   # 运行内存
        self.space = space  # 存储空间

    def check(self):
        """查看手机一些基本信息"""
        print(f'{self.name}的手机品牌是{self.mark}，型号是{self.model}，'
               f'操作系统是{self.system}, 运行内存是{self.ram}')

    def call_up(self, name, phone_num):
        """ 给指名名字和电话的人打电话"""
        print(f'"{self.name}"正在给"{name}"，打电话：我的电话号码是{self.phone_num}，'
               f'他的电话号码是{phone_num}')

    def send_message(self, name, *content):
        """给指定的人发送多条短信"""
        for i in content:
            n = content.index(i)
            print(f'"{self.name}"正在给"{name}"发送短信,'
               f'第{n+1}条，内容是："{i}"')

    def download(self, app_name, size):
        """下载app,根据app大小计算剩余空间"""
        print(f'"{self.name}"的"{self.model}",现在需要下载{app_name}！')
        try:
            if float(size) < float(self.space):
                self.space -= size
                return(f'空间够用，可以下载,剩余空间为{self.space}G！')
            else:
                return(f'当前剩余空间是{self.space}G，空间不够用，无法下载！')
        except ValueError:
            return('下载大小或空间参数无法识别！')


def main1(info):

    person_mobile1 = MobilePhone(**info)  # 传入对象信息

# ****************************#查看手机主人****************************

    print('手机主人是："{}"!'.format(person_mobile1.name)) #

# ****************************查看类属性*******************************

    print(f'手机的类属性，所有手机都有"{person_mobile1.have}"!')

# ****************************查看手机基本信息**************************

    person_mobile1.check()

# ****************************给指定人员和手机号打电话*******************

    person_mobile1.call_up('王俊凯', '13067675298')

# ****************************给指定人员发多条短信***********************

    person_mobile1.send_message('五月天', '我好喜欢你们', '喜欢你们的歌', '我想去看你们的演唱会！')

# ************************判断app是否可下载，并计算剩余空间****************

    download_value = person_mobile1.download('柠檬班APP', 30.8)
    # 传入app名称和大小，返回是否可以下载，并返回剩余空间，没有超出空间
    print(download_value)

    download_value = person_mobile1.download('课堂派', 40)
    # 传入app名称和大小，返回是否可以下载，并返回剩余空间，超出空间
    print(download_value)


if __name__ == '__main__':
    info = {"name": "天天", "phone_num": "18898958360", "mark": "vivo", "model": "vivoX20", "ram": "6G",
            "space": 64}
    info1 = {"name": "棒棒", "phone_num": "15039067654", "mark": "iPhone", "model": "iPhone7plus", "ram": "8G",
             "space": '22', "system": 'ios 8.0.0'}
    main1(info)
    main1(info1)




# 2、
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息

class Cats(object):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food):
        print(f"它正在吃着美味的{food}")

    def drink(self, drink):
        print(f"它正在喝着可口的{drink}")

    def enjoy(self, status):
        print(f"它正在{status}")


def main2():
    my_cat = Cats('Tom', '1岁', '灰色的')
    print(f"{my_cat.color}猫咪{my_cat.name},今年{my_cat.age}了")
    my_cat.eat('猫粮')
    my_cat.drink('酸奶')
    my_cat.enjoy('享受阳光')


main2()




# 3.列举3个生活中类和对象的例子，用代码表示。

#**********************男朋友******************************

class BoyFriend(object):
    sex = '男'

    def __init__(self, outside, inherent, height, family_conditions):

        self.outside = outside

        self.inherent = inherent

        self.height = height

        self.family_conditions = family_conditions


    def make_money(self, wages):
        print("男朋友会挣钱！")

    def do_romantic_sth(self, sth):
        print("那朋友会做浪漫的事!")

    def marry__me(self):
        print("男朋友最终会变成老公！")

#**********************笔******************************

class Pen(object):  #笔

    def __init__(self, type, color):
        self.type = type

        self.color = color


    def write(self, content):
        print("笔用写字！")

    def turn(self):
        print("转笔!转 转 转 转~~~~")


#**********************游乐园******************************

class AmusementPark(object):  # 游乐园

    def __init__(self, name, location, scale, facility_type):
        self.name = name

        self.location = location

        self.scale = scale

        self.facility_type = facility_type


    def buy_tickets(self):
        print("进游乐园需要买票！")

    def play_game(self):
        print(f"在游乐园可以玩{self.facility_type}这些设施")

    def if_open(self, start_time,stop_time):
        print(f"游乐园{start_time}点开始营业，{stop_time}点结束营业！")





# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）
#   和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant(object):

    def __init__(self, restaurant_name, *cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print(f"饭店名称为:{self.restaurant_name}\n"
              f"饭店的美食种类有：")
        for i in self.cooking_type:
            print(i)

    def open_restaurant(self):
        print(f"饭店现在正在营业！")

def main3(a):
    restaurant = Restaurant(*a)

    print(restaurant.restaurant_name)
    print(restaurant.cooking_type)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

list_1 = ['柠檬大酒楼','粤菜', '川菜', '湘菜', '豫菜']
main3(list_1)




