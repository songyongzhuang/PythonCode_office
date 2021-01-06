# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 21:22
# @Author  : li_ma
# @FileName: 0909.py

# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。
class Mobile:
    system_verson = 8.0

    def __init__(self, brand, model, cpu_count, price, screen_size, camera_count):
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.cpu_count = cpu_count  # cpu核心数
        self.price = price  # 价格
        self.screen_size = screen_size  # 屏幕尺寸
        self.camera_count = camera_count  # 摄像头个数


    def make_call(self, mobile_num):
        """
        打电话功能
        :param mobile_num:  电话号码
        :return:
        """
        print('正在给{}打电话......'.format(mobile_num))
        return '电话接通成功'

    def send_message(self, mobile_num, message_content):
        """
        发短信功能
        :param mobile_num:  电话号码
        :param message_content:  短信内容
        :return:
        """
        print('正在给{}发短信，短信内容是: {}......'.format(mobile_num, message_content))
        return '短信发送成功'

    def take_picture(self):
        """
        照相功能
        """
        print('{}个摄像头正在拍照......'.format(self.camera_count))
        return '已拍照'

    def open_app(self, app_name):
        """
        打开指定app
        :param app_name:  应用名称
        :return:
        """
        print('正在打开{}应用......'.format(app_name))
        return '{}已打开，显示在{}寸的屏幕上'.format(app_name,self.screen_size)

    def run_score(self):
        """
        跑个分
        :return: 跑分结果
        """
        print('正在跑分......')
        score = int(self.camera_count) * 10000
        return '跑分完毕，分数是{}分'.format(score)

    def upadte_system_verson(self,new_version):
        """
        升级系统版本
        :param new_version:  新版本号
        :return:  升级成功或者失败
        """
        print('正在升级到{}版本......'.format(new_version))
        if new_version > self.system_verson:
            self.system_verson = new_version
            return '升级成功'
        else:
            return '升级失败'



if __name__ == '__main__':
    huawei = Mobile('huawei', 'MATE 30', '4', '6000', '6.3', '3')
    print(huawei.make_call('13901234567'))
    print(huawei.send_message('13901234567', '你好'))
    print(huawei.take_picture())
    print(huawei.open_app('腾讯课堂'))
    print(huawei.run_score())
    print(huawei.upadte_system_verson(8.1))
    print(huawei.system_verson)


# 2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息
class Cat:
    mood = '一般'  # 心情

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    def eat(self, food_kind):
        return '吃着{}的食物'.format(food_kind)

    def drink(self, drink_kind):
        return '喝着{}的饮料'.format(drink_kind)


if __name__ == '__main__':
    tom = Cat('灰色', 'Tom', '1')
    tom.mood = '享受'
    print('{color}的{name}猫，今年{age}岁，吃着{eat}的食物，喝着{drink}的饮料，非常{mood}的样子'
          .format(color=tom.color, name=tom.name, age=tom.age, eat=tom.eat('美味'), drink=tom.drink('可口'), mood=tom.mood))

# 3.列举3个生活中类和对象的例子，用代码表示。
# 例子1  Pycharm
class Pycharm:
    version = '2019.2'

    def __init__(self, platform, edition, settings):
        self.platform = platform  # 平台类型 如windows Mac linux...
        self.edition = edition  # 版本类型， 专业版，社区版
        self.settings = settings

    def change_settings(self, setting_content):
        print('进行更改为{}...'.format(setting_content))
        self.settings = setting_content
        return '设置成功'

    def coding(self, codes):
        print('正在写{}代码...'.format(codes))

    def run(self, codes):
        self.coding(codes)
        return '运行成功'


if __name__ == '__main__':
    p = Pycharm('windows', '社区版', '默认设置')
    print(p.run('haha'))


# 例子2  空调
class AirConditioner:
    work_tpye = '制冷'
    temperature = '26度'

    def __init__(self, brand, value, power_waste):
        self.brand = brand  # 品牌
        self.value = value  # 价格
        self.power_waste = power_waste  # 功耗类型

    def power_on(self):
        print('空调已打开，当前为{}模式，温度{}'.format(self.work_tpye, self.temperature))

    def power_off(self):
        print('空调已关闭')


if __name__ == '__main__':
    a = AirConditioner('格力', '3000', '低功耗')
    a.work_tpye = '制热'
    a.temperature = '30度'
    a.power_on()
    a.power_off()


# 例子3  汽车
class MotorCar:
    oil_box = 100  # 油箱剩余量

    def __init__(self, brand, car_type):
        self.brand = brand  # 品牌
        self.car_type = car_type  # 车辆类型 如轿车 suv 货车

    def drive_car(self):
        print('开车中。。。')
        if self.car_type == '轿车':
            self.oil_box -= 1
        elif self.car_type == 'suv':
            self.oil_box -= 2
        elif self.car_type == '货车':
            self.oil_box -= 10
        else:
            self.oil_box -= 3

    def stop_car(self):
        print('已停车，剩余油量{}'.format(self.oil_box))


if __name__ == '__main__':
    car = MotorCar('宝马', 'suv')
    car.drive_car()
    car.stop_car()


# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant:

    def __init__(self, restaurant_name, cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print('本饭店名字叫{}，主要美食种类为{},欢迎品尝'.format(self.restaurant_name, self.cooking_type))

    def open_restaurant(self):
        print('{}正在营业'.format(self.restaurant_name))


if __name__ == '__main__':
    xi_bei = Restaurant('西贝莜面村', '陕西面食')
    print(xi_bei.restaurant_name)
    print(xi_bei.cooking_type)
    xi_bei.open_restaurant()
