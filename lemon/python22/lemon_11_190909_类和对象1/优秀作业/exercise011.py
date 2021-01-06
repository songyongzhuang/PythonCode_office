"""
1、实现一个手机类，并实例化你的手机。
要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
尽量多的获取不同属性和使用不同的功能。
"""


class Phone:
    # 初始化手机的属性：品牌，型号，价格，摄像头，屏幕，cpu，内存，存储
    def __init__(self, make, model, price, camera, screen, cpu, ram, rom):
        self.make = make
        self.model = model
        self.price = price
        self.camera = camera
        self.screen = screen
        self.cpu = cpu
        self.ram = ram
        self.rom = rom

    # 定义手机的打电话，发短信，拍照，运行app等方法
    def make_phone_call(self):
        return '{}品牌{}型号的手机可拨打电话'.format(self.make, self.model)

    def send_message(self):
        return '{}品牌{}型号的手机能发短信'.format(self.make, self.model)

    def take_photo(self):
        return '{}品牌{}型号的手机，使用{}镜头拍照'.format(self.make, self.model, self.camera)

    def run_app(self):
        return '{}品牌{}型号的手机，CPU为{}，内存为{}，存储空间为{}，能流程运行app' \
            .format(self.make, self.model, self.cpu, self.ram, self.rom)


# 实例化
my_phone = Phone('Apple', 'XR', 5000, '1200W像素', '6.2英寸', 'A12', '3GB', '128GB')

"""
2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
"""


class Cat:
    # 初始化猫的属性：名字，颜色，年龄
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    # 定义吃，喝，享受3个方法
    def eat(self):
        return '{}的{}猫，今年{}岁，吃着美味的食物'.format(self.color, self.name, self.age)

    def drink(self):
        return '{}的{}猫，今年{}岁，喝着可口的饮料'.format(self.color, self.name, self.age)

    def enjoy(self):
        return '{}的{}猫，今年{}岁，非常享受的样子'.format(self.color, self.name, self.age)


# a.根据以上信息，抽象出一个类
tom_cat = Cat('Tom', '灰色', 1)
# b.定义相关属性，并能在类的外面调用
print(tom_cat.name)
print(tom_cat.age)
print(tom_cat.color)
# c.定义相关方法，在方法中打印相应信息
print(tom_cat.eat())
print(tom_cat.drink())
print(tom_cat.enjoy())

"""
3.列举3个生活中类和对象的例子，用代码表示
"""


# a.做饭
class Cook:
    # 初始化做饭的属性：厨师，方法，材料，菜名
    def __init__(self, cooker, how, item, dish_name):
        self.cooker = cooker
        self.how = how
        self.item = item
        self.dish_name = dish_name

    # 定义哪个大厨做哪道菜
    def cooker_to_dish(self):
        return '{}大厨做了{}菜'.format(self.cooker, self.dish_name)

    # 定义这道菜使用的方法和材料
    def cook_item(self):
        return '{}用{}材料{}的'.format(self.dish_name, self.item, self.how)


# 实例化
my_cook = Cook('我', '炒', ('肉丝', '竹笋', '辣椒'), '鱼香肉丝')


# b.电脑
class Computer:
    # 初始化电脑的配置信息：cpu，内存，硬盘，主板，电源
    def __init__(self, cpu, ram, disk, motherboard, power):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.motherboard = motherboard
        self.power = power

    # 定义电脑的配置信息，玩游戏
    def computer_info(self):
        return '这台电脑的配置cpu：{}，内存：{}，硬盘：{}'.format(self.cpu, self.ram, self.disk)

    def play_game(self):
        return '这台电脑电源{}，内存为{}，超过推荐配置，打王者农药不会炸!'.format(self.power, self.ram)


# 实例化
my_computer = Computer('I5', '8G', '250G', '高端主板', '600W电源')


# c.球队队员
class Teammenber:
    # 初始化球队队员：队员姓名，身高，位置，表现
    def __init__(self, name, height, position, play):
        self.name = name
        self.height = height
        self.position = position
        self.play = play

    # 定义队员的姓名和表现，身高适合打什么位置
    def name_play(self):
        return '球员{}表现{}！'.format(self.name, self.play)

    def position_fit(self):
        if self.height > 180:
            return '球员{}身高{},大于180,适合打{}'.format(self.name, self.height, self.position)
        elif 160 < self.height < 180:
            return '球员{}身高{},在160-180之间,适合打{}'.format(self.name, self.height, self.position)
        else:
            return '球员{}身高{},不适合打球'.format(self.name, self.height)


# 实例化
my_teammenber = Teammenber('张三', '175', '后卫', '非常棒')

"""
4.编写如下程序
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""


# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
class Restaurant:
    def __init__(self, restaurant_name, cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        return '饭店名为：{}，美食种类有：{}'.format(self.restaurant_name, self.cooking_type)

    def open_restaurant(self):
        return '饭店名为：{},正在营业中！'.format(self.restaurant_name)


# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
restaurant = Restaurant('老王饭馆', '炒菜，烧烤，火锅，闷锅')
print(restaurant.restaurant_name)
print(restaurant.cooking_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
