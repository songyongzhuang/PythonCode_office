#1.
'''class phone():
    def __init__(self,pinpai,xinghao,call,massage):
        self.pinpai=pinpai
        self.xinghao=xinghao
        self.call=call
        self.massage=massage
    def Pinpai(self):
        print('品牌是:%s,型号是：%s'%(self.pinpai,self.xinghao))
    def gongneng(self):
        print('打电话：%s,发信息：%s'%(self.call,self.massage))
pi=phone('huawei','p30','123156545','niaho')
pi.Pinpai()
pi.gongneng()'''

#2
age=1
color='black'
class Tom():
    def eat(self):
        print('吃着美味的食物')
    def drink(self):
        print('喝着可口可乐')
t=Tom()
t.drink()
t.eat()

#3
class Persion():
    height=175
    weight=74
    def run(self):
        print('我喜欢跑步')
    def sing(self):
        print('我喜欢唱歌')
p=Persion()
p.run()
p.sing()

#4
class Restaurant():
    restaurant_name='沙县小吃'
    cooking_type='南方小吃'
    def describe_restaurant(self):
        print('本饭店的名字是%s,主要的美食种类是%s')
    def open_restaurant(self):
        print('饭店正在营业')
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type
        print('饭店的名字是%s,主要的美食种类是%s'%(self.restaurant_name,self.cooking_type))

r=Restaurant('沙县小吃','南方小吃')
r.describe_restaurant()
r.open_restaurant()



