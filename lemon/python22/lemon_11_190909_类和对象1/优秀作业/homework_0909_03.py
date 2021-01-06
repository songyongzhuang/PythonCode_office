# _*_ coding: utf-8 _*_
#@Time    : 2019/9/11 11:10
#@Author  : 满满
#@File    : homework_0909_03.py
#@Email   :867232508@qq.com

'''3.列举3个生活中类和对象的例子，用代码表示。'''
#汽车类
class Car():


    def __init__(self,brand,model,price,color):
        self.brand = brand      #品牌
        self.model = model      #型号
        self.price = price      #价格
        self.color = color      #颜色
        print('有一辆价值{}的{}品牌{}型号{}颜色的车'.format(self.price,self.brand,self.model,self.color))


    def run(self,speed=100):
        str = '正在以每小时{}公里的速度在奔驰'.format(speed)
        return  str


##动物类
class Animal():

    def __init__(self,type):
        self.type = type
        print('有一只{}'.format(self.type))

    #动物奔跑
    def run(self,speed=10):
        str = '正在以每小时{}公里的速度在奔跑'.format(speed)
        return  str


class Person():


    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
        print('有一个{}岁的名叫{}的工作是{}的'.format(self.age,self.name,self.job))

    def eat(self,food):
        str = '吃{}东西'.format(food)
        return str


if __name__ == '__main__':
    car = Car('大众','X7','500万','白')
    print(car.run())
    print('***************************************')
    animal = Animal('老虎')
    print(animal.run(20))
    print('***************************************')
    person = Person('满满',23,'测试')
    print(person.eat('苹果'))
