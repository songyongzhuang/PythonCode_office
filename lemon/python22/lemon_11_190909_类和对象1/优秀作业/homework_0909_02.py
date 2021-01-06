# _*_ coding: utf-8 _*_
#@Time    : 2019/9/11 11:09
#@Author  : 满满
#@File    : homework_0909_02.py
#@Email   :867232508@qq.com

'''Q2:
灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息'''


class Cat():


    def __init__(self,name,age,color):
        self.name = name        #姓名
        self.age = age          #年龄
        self.color = color      #颜色
        print('有一只{}颜色的{}岁的名叫{}的猫'.format(self.color,self.age,self.name))

    #吃什么东西
    def eat(self,food = '汉堡'):
        return_str = '吃着美味的{}'.format(food)
        return  return_str

    #喝什么
    def drink(self,type = '可乐'):
        return_str = '喝着{}饮料'.format(type)
        return return_str

if __name__ == '__main__':
    cat = Cat('Tom',2,'灰')
    print(cat.eat('烧烤'))
    print(cat.drink('橙汁'))


