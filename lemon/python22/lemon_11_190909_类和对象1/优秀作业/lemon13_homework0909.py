# -*- coding: utf-8 -*-
# @Time     : 2019/9/10 22:22
# @Author   : wolf_eye
# @Email    : 15840995236@163.com
# @File     : lemon13_homework0909.py
# @student  : 狼眸

# Q1:实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。
class MobilePhone(object):
    def __init__(self, system_type, logo, size, version):
        self.sys_type = system_type     # 手机系统类型
        self.logo = logo                # 手机品牌
        self.size = size                # 手机型号
        self.version = version          # 手机版本

    def call_number(self, name, phone_number):
        print(f'呼叫{name},电话号码{phone_number}')

    def send_message(self, content):
        return f'发送内容：{content}'

    def listen_music(self, music_name):
        return f'正在播放歌曲：{music_name}'


# 实例化对象
my_phone = MobilePhone('Android', 'XiaoMi', 'Mix2', 'MIUI 10.4.2')
# 调用实例属性
print(f'这个实例化对象是一个系统类型为：{my_phone.sys_type}，手机品牌型号为：'
      f'{my_phone.logo} {my_phone.size}，手机版本为：{my_phone.version} 的手机')
# 调用实例方法
my_phone.call_number('wolf', '15800000000')
message = my_phone.send_message('Python is my life')
print(message)
print(my_phone.listen_music('芒种'))

# Q2：灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息
class Cat(object):
    # 定义一个类属性试试水
    leg_num = 4
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def eat_food(self):
        print(f'一只叫{self.name}{self.color}{self.age}岁的猫，正在吃美味的食物')
    def drink_color(self):
        print(f'一只叫{self.name}{self.color}色{self.age}岁的猫，正在喝可口的饮料')

# 实例化对象
tomcat = Cat('Tom', '1', 'grey')
# 调用类属性、实例属性
print(f'这是一只名字叫{tomcat.name},今年{tomcat.age}岁{tomcat.color}色，有{tomcat.leg_num}只腿的猫')
# 调用类方法
tomcat.eat_food()
tomcat.drink_color()


# 列举3个生活中类和对象的例子，用代码表示。
# 举例1：
'''
  1.声明一个类：花类
    1.1 花类属性：颜色(color)、花季(adolescence)、名称、花语(florid)、花瓣数(petal_count)
    1.2 花类功能：泡茶(brew)、洗澡(shower)、是否爱我(花瓣数)(love)、清新空气(clean_air)
创建花对象：
    rose = Flower('红色', '5-9月', '玫瑰', '爱情', 21)
    rose.泡茶()
    rose.是否爱我() 判断花瓣数是奇数，输出不爱我，是偶数，输出爱我
'''
# 声明类
class Flower(object):
    # 初始化属性
    def __init__(self, color, adolescence, name, florid, petal_count):
        # 赋值
        self.color = color
        self.adolescence = adolescence
        self.name = name
        self.florid = florid
        self.petal_count = petal_count

    # 各种功能
    # 泡茶：水的种类，时间，多不定长参数
    def brew(self, water, time, **kwargs):
        print(water, time, kwargs)

    # 洗澡：水温（temperature），时间
    def shower(self, temperature, time):
        print(temperature, time)

    # 是否爱我(花瓣数):爱^-^!!! 不爱QAQ!
    def love_ask(self, love, not_love):
        if self.petal_count % 2 == 0:
            print('花瓣数是%s，表示%s' % (self.petal_count, love))
        else:
            print('花瓣数是%s，表示%s' % (self.petal_count, not_love))

    # 清新空气: 速度等级，空气体积/天
    def clean_air(self, speed, air_volume_day):
        print(speed, air_volume_day)

# 创建对象
# 玫瑰
rose = Flower('红色', '5-9月', '玫瑰', '爱情', 21)
# 泡茶
rose.brew('泉水', '30分钟', step1='赏茶', step2='品茶', step3='回味')
# 是否爱我(花瓣数)
rose.love_ask('爱^-^!!!', '不爱QAQ!')
# 洗澡
rose.shower('66℃', '1小时')
# 清新空气
rose.clean_air('中', '1立方/天')

# 举例2：声明银行账号类，
# 属性：姓名，存款，
# 类方法：存钱、取钱、查询余额
class Account(object):
    def __init__(self, name, balance):
        # "初始化一个新的Account实例"
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        # "存款"
        self.balance = self.balance + amt
        return self.balance
    def withdraw(self, amt):
        # "取款"
        if self.balance < amt:
            return '余额不足'
        else:
            self.balance = self.balance - amt
            return self.balance
    def inquiry(self):
        # "查询当前余额"
        return self.balance


# 实例化一个银行账户
account = Account('狼眸', 10000)
# 调用属性
print(f'开户人:{account.name}，存入金额:{account.balance}')
# 存钱
print(f'存钱后余额为：{account.deposit(1000)}')
# 取钱
print(f'取钱后余额为：{account.withdraw(100000)}')
print(f'取钱后余额为：{account.withdraw(100)}')
# 查询余额
print(f'存钱后余额为：{account.inquiry()}')


# 举例3：柠檬班有老师布置作业、班主任催作业，导师检查作业，学生完成作业
class Lemon:
    def __init__(self, teacher, headmaster, tutor, student):
        self.teacher = teacher
        self.headmaster = headmaster
        self.tutor = tutor
        self.student = student
    def assign_homework(self):
        # 布置作业
        print(f'{self.teacher}布置作业')
    def urge_homework(self):
        # 催作业
        print(f'{self.headmaster}夺命三连催作业')
    def check_homework(self):
        # 检查作业
        print(f'帅气的{self.tutor}辛苦的检查作业')
    def finish_homework(self):
        # 完成作业
        print(f'{self.student}努力完成作业')


lemon = Lemon('雨泽', '文文', '超哥', '狼眸')
lemon.assign_homework()
lemon.urge_homework()
lemon.check_homework()
lemon.finish_homework()


# Q4: 编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant(object):
    def __init__(self, name, *kargs):
        self.restaurant_name = name
        self.cooking_type = kargs
    def describe_restaurant(self):
        print(f'本饭店是{self.restaurant_name}，拥有的美食种类有{self.cooking_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业')


# food_kind = {'东北菜':'锅包肉，猪肉炖粉条','川菜':'宫保鸡丁，水煮鱼'}
food_kind = ('东北菜', '川菜', '湘菜', '鲁菜')
# 实例化对象
restaurant = Restaurant('温馨大酒店', *food_kind)
# 调用实例属性
print(f'欢迎光临{restaurant.restaurant_name}，本饭店美食种类有{restaurant.cooking_type}')
# 调用类方法
restaurant.describe_restaurant()
restaurant.open_restaurant()

