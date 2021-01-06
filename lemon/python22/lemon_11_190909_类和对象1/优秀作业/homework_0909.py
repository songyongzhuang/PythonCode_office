# -*- coding:UTF-8 -*-
# @Time     : 2019-09-10 18:26
# @Author   : yizizhiyue
# @Email    : yizizhiyue@qq.com
# @File     : homework_0909.py
# @Software : PyCharm


''' ***************************************** 第一题 *****************************************  '''
class Phone:
    # 类的初始化方法
    def __init__(self, brand, model, color, size):
        # 设置Phone类的属性
        self.brand = brand
        self.model = model
        self.color = color
        self.size = size

    # 类的实例方法---打电话
    def do_call(self, to_person):
        print('我的那部{}的{}-{}手机正在给{}打电话...'.format(self.color, self.brand, self.model, to_person))

    # 类的实例方法---发短信
    def send_message(self, to_person = 'Tom', message = 'have a nice day!!!'):
        print('给{}成功发送了一条短信，短信内容为：'.format(to_person))
        print(f'''
        ****************************
        hi,{to_person},我今天买了一部{self.brand}手机
        型号：{self.model}
        颜色：是我最爱的{self.color}
        尺寸：{self.size},非常适合玩游戏
        {message}
        ****************************
        ''')
# 实例化一个Phone类的对象
myphone = Phone('HuaWei', 'nova4', '亮红色', '3.5英寸')
# 调用对象myphone的do_call方法
myphone.do_call('Tom')
# 调用对象myphone的send_message方法
myphone.send_message()



''' ***************************************** 第二题 *****************************************  '''
class Cat:
    def __init__(self):
        self.name = 'Tom'
        self.color = '灰色'
        self.age = '1岁'

    # 定义eating方法，在方法中打印相应信息
    def eating(self):
        print('{}的{}猫，今年{}，吃着美味的食物，非常享受的样子'.format(self.color, self.name, self.age))

    # 定义drinking方法，在方法中打印相应信息
    def drinking(self):
        print('{}的{}猫，今年{}，喝着可口的饮料，非常享受的样子'.format(self.color, self.name, self.age))

# 实例化Cat类
cat = Cat()
# 调用Cat的实例方法eating
cat.eating()
# 调用Cat的实例方法drinking
cat.drinking()
# 在类的外面调用Cat类的属性
print(cat.name)
print(cat.color)
print(cat.age)



''' ***************************************** 第三题 *****************************************  '''
# 第一个例子
# 定义一个人类的类
class Human:
    ''' 类的实例化方法
        根据人类的特性，抽象出'人类'这个类的属性
        姓名、性别、年龄、爱好
    '''
    def __init__(self, name, gender, age, hobby):
        print('我是一个人类，我有鼻子、眼睛、耳朵等人类的基本特征')
        self.name = name
        self.gender = gender
        self.age = age
        self.hobby = hobby

    # 打印'人类'的特征信息
    def get_human_info(self):
        print(f'''
            **********我的个人信息是******************
            姓名：{self.name}
            性别：{self.gender}
            年龄：{self.age}
            爱好：{self.hobby},想和我一起玩儿吗
            ****************************
            ''')

# 实例化一个'人类'的对象lucy
lucy = Human('luch','女生', '23岁','看宫崎骏的动漫，喜欢游泳')
# 打印对象lucy的个人信息
lucy.get_human_info()

# 实例化一个'人类'的对象jack
jack = Human('jack','男生', '29岁','喜欢健身、徒步，看世界杯')
# 打印对象lucy的个人信息
jack.get_human_info()



# 第二个例子
# 定义一个老师类
class Teacher:
    ''' 类的实例化方法
        根据老师的特性，抽象出'老师'这个类的属性
        姓名、年龄、教授学科、经验
    '''
    def __init__(self, name, age, teach, expires):
        print('我是一个老师')
        self.name = name
        self.teach = teach
        self.age = age
        self.expires = expires

    def teach_class(self):
        print('我正在上{}课'.format(self.teach))

    # 打印'老师'的特征信息
    def get_teacher_info(self):
        print('大家好，我叫{}，我是一个{}岁的{}老师，目前已经任课{}年'.format(self.name, self.age, self.teach, self.expires))

# 实例化一个英语老师
english_teacher = Teacher('Tracy', '32', '英语', '10')
# 调用'老师'的实例方法
english_teacher.get_teacher_info()


# 第三个例子
# 定义一个花朵类
class Flowers:
    ''' 类的实例化方法
        根据花朵的特性，抽象出'花朵'这个类的属性
        种类名称、颜色
    '''
    def __init__(self, name, color):
        print('我是一朵花')
        self.name = name
        self.color = color

    def open_flower(self):
        print('我要开始开花了')

# 实例化一个牡丹花对象
mudan = Flowers('mudan', 'red')
# 调用'花朵'的实例方法
mudan.open_flower()




''' ***************************************** 第四题 *****************************************  '''
class Restaurant:
    def __init__(self, restaurant_name, *cooking_type):
        # 设置属性
        # 饭店名（restaurant_name）
        self.restaurant_name = restaurant_name
        # 美食种类（cooking_type）
        self.cooking_type = cooking_type


    def describe_restaurant(self):
        print('我们的饭店名称是：{}'.format(self.restaurant_name))
        print('我们的美食有：{}'.format(self.cooking_type))

    def open_restaurant(self):
        print('显示饭店正在营业,客人可随时进店享受我们的美食服务')

# restaurant 的实例
restaurant = Restaurant('和平饭店', '红烧茄子', '蒜苗回锅', '黄焖牛肉', '龙井虾仁')
# 打印对象的两个属性
print(restaurant.restaurant_name)
print(restaurant.cooking_type)
# 调用两个方法
restaurant.describe_restaurant()
restaurant.open_restaurant()
