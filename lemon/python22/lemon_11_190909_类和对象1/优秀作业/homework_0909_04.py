# _*_ coding: utf-8 _*_
#@Time    : 2019/9/11 11:10
#@Author  : 满满
#@File    : homework_0909_04.py
#@Email   :867232508@qq.com

'''
4.编写如下程序
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
'''
import  datetime

class Restaurant():


    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    #描述饭店信息
    def describe_restaurant(self):
        return_str = '{}饭店是一个五星级饭店，其中有{}美食'.format(self.restaurant_name,self.cooking_type)
        return  return_str


    #饭店是否营业，当对象创建的时间为8-12或16-22时间内，返回饭店正在营业
    def open_restaurant(self):
        #获取当前系统的时间
        curr_time = datetime.datetime.now()
        #获取系统时间的小时
        hour = curr_time.hour
        if 8 < hour < 12 or 16 < hour< 22:
            str = '饭店正在营业'
        else:
            str = '休息中'
        return str

if __name__ == '__main__':
    #创建一个饭店对象
    restaurant = Restaurant('江宴楼','中餐')
    print(restaurant.restaurant_name)
    print(restaurant.cooking_type)
    print(restaurant.describe_restaurant())
    print(restaurant.open_restaurant())