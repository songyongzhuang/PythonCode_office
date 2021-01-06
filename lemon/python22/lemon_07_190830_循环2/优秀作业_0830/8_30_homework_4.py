#-*- coding：utf-8 -*-
#时间 ：2019-09-01 00:08
#作者：小白
'''
4.编写如下程序

尝试函数部分封装：
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数

a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8

b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
'''
"""
思路：1。定义一个计算BMI的函数：通过身高，体重，公式计算出BMI指数，并通过if判断，给出相应提醒
     2。当用户输入的身高和体重都不为0时，会一直运行程序，当输入的身高和体重都为0时，退出程序
     2。做用户输入的判断，当身高超过3米和体重超过300公斤，已经输入为非数值时，都会提醒用户输入异常
"""
#定义函数，计算BMI，有两个形参：身高和体重
def BMI_count(height,weight):
    BMI = weight / height ** 2 #计算BMI的公式
    if BMI < 18.5:      #对计算出的BMI做判断
        print("体重过轻")
    elif BMI >= 25 and BMI <= 28:
        print("正常")
    elif BMI > 28 and BMI < 32:
        print("肥胖")
    else:
        print("严重肥胖")
    return BMI  #返BMI值

height_input = input("请输入你的身高（单位：m）：")  #用户输入身高
weight_input = input("请输入你的体重（单位：kg）：") #用户输入体重
while height_input != '0' and weight_input != '0':  #while循环，当身高和体重都不为0时，执行循环体
    if height_input.replace(".","",1).isdigit() and weight_input.replace(".",'',1).isdigit():   #判断输入身高体重的值为数值。
        float_height = float(height_input)    #将身高从字符串转换成浮点数
        float_weight = float(weight_input)    #将体重从字符串转换成浮点数
        if float_height < 3 and float_weight < 300:   #对身高体重进行判断，如果身高小于3米，体重小于300kg，则可以调用BMI函数
            BMI_count(float_height,float_weight)

        elif float_height >= 3 and float_weight < 300: #如果身高大于等于3米，但是体重小于300kg，则提醒用户身高输入异常
            print("身高输入异常")

        elif float_height < 3 and float_weight >= 300:  #如果身高小于3米，体重超过300kg，则提醒用户体重输入异常
            print("体重输入异常")

        else:           #否则输入都异常
            print("体重和升高身高输入异常")

    else:     #输入的值为非数值时，提醒用户输入值非法
        print("身高和体重输入的值不合法")
    height_input = input("请重新输入你的身高：")      #用户重新输入
    weight_input = input("请重新输入你的体重：")      #用户重新输入
print("登出系统")
