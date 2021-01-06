# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : lemon_190909_作业.py
# Author       : Administrator
# Create time  : 2019-09-10 10:23
# IDE          : PyCharm

# 0910-类和对象
# 截至：09月15日  23:59展示词云
# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。


class Phone:
    # name = name  这是类属性：类属性是写在初始化方法外，类下方的

    # __init__ 初始化方法，初始化函数
    def __init__(self, system, brand, versions):
        """ 实例属性是写在初始化方法里面的 """
        self.system = system  # 系统
        self.brand = brand  # 品牌
        self.versions = versions  # 型号

    def ring_up(self):
        """ 打电话，调用实例属性 """
        print(f'用{self.system}手机{self.brand}打电话')

    def send_messages(self):
        """ 发短信，调用实例属性 """
        print(f'用{self.brand}发短信')

    def look_movie(self):
        """ 看电影，调用实例属性 """
        print(f'用{self.brand}{self.versions}看电影')


phone = Phone(system='安卓', brand='华为', versions='P40')
phone.ring_up()  # 打电话
phone.send_messages()  # 发短信
phone.look_movie()  # 看电影


# 2、
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息


class Cat:
    def __init__(self, name, age, colour):
        self.name = name  # 名字
        self.age = age  # 年龄
        self.colour = colour  # 颜色

    def eat(self, food):
        """ 吃 """
        print(f'{self.colour}的小猫它叫:{self.name}, 今年{self.age}岁, 吃着美味的{food}, 非常享受的样子.')

    def drink(self, drinks):
        """ 喝 """
        print(f'{self.colour}的小猫它叫:{self.name}, 今年{self.age}岁, 喝着可口的{drinks}, 非常享受的样子.')


cat = Cat(name='Python', age='1', colour='雪白')
cat.eat('鱼')  # 吃
cat.drink('牛奶')  # 喝


# 3.列举3个生活中类和对象的例子，用代码表示。

class WriteCode:

    def __init__(self, computer, ide, language):
        self.computer = computer  # 电脑
        self.ide = ide  # 编辑器
        self.language = language  # 语言

    def open_computer(self):
        print(f'打开电脑：{self.computer}')

    def open_ide(self):
        print(f'打开编辑器：{self.ide}')

    def write_code(self):
        print(f'编程语言选择：{self.language}')


study = WriteCode(computer='Alienware Area-51m', ide='PyCharm', language='python')
study.open_computer()  # 打开电脑
study.open_ide()  # 打开编辑器
study.write_code()  # 选择语言

#
#
# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


class Restaurant:

    def __init__(self, restaurant_name, *cooking_type):
        self.restaurant_name = restaurant_name  # 饭店名
        self.cooking_type = cooking_type  # 美食种类

    def describe_restaurant(self):
        print(f"饭店名称:{self.restaurant_name}, 拥有的美食种类有:{self.cooking_type}.")

    def open_restaurant(self):
        print(f"饭店:{self.restaurant_name}, 正在营业.")


cooking_type = ('川菜', '鲁菜', '湘菜')  # 传多个 *解包
restaurant = Restaurant('吃饭不要钱', *cooking_type)
# 打印两个属性
print(f"酒店名称：{restaurant.restaurant_name}")
print(f"美食种类：{restaurant.cooking_type}")

# 调用前述两个方法
restaurant.describe_restaurant()
restaurant.open_restaurant()
