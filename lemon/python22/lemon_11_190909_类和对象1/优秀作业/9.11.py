# 1、实现一个手机类，并实例化你的手机。
# 要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
# 尽量多的获取不同属性和使用不同的功能。


# class phone(object):
#     def __init__(self,pinpai,xinghao):
#         self.pinpai = pinpai
#         self.xinghao = xinghao
#
# xianshi = phone('huawei','mate20')
# print(xianshi.pinpai)
# print(xianshi.xinghao)


# 2、
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息

# class cat():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def dongzuo(self):
#          print('吃着美味的食物，喝着可口的饮料，非常享受的样子')
#
# xianshi = cat('tom','1岁')
# print(xianshi.name)
# print(xianshi.age)
# cat.dongzuo(1)#不懂为啥还要参数



# 3.列举3个生活中类和对象的例子，用代码表示。

# class shenghuo():
#     zaoshang = '上班'
#     zhongwu = '吃饭'
#     wanshang = '睡觉'
#
# print(shenghuo.zaoshang)
# print(shenghuo.zhongwu)
# print(shenghuo.wanshang)

# 4.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant():
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print('吃饭店已经有一百年历史，食物都非常好吃')

    def open_restaurant(self,kaidian):
        if kaidian == 1:
            print('正在营业')
        else:
            print('休息中')

restaurant = Restaurant('和平饭店','中菜')
print(restaurant.restaurant_name)
print(restaurant.cooking_type)
restaurant.describe_restaurant()
restaurant.open_restaurant(0)