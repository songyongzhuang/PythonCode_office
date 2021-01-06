#-*- coding：utf-8 -*-
#时间 ：2019-09-01 00:01
#作者：小白

'''


3.将两个变量的值进行交换（a = 100, b = 200）

交换之后，a = 200， b = 100， 使用函数。
'''
'''
思路：
1。定义一个函数在进行值的位置交换，可以进行多个值的位置的交换
2。让用户输入值，将值存在列表中，然后调用函数。用户可以输入2个值，或者多个值。
'''
def change(change_list):

    for i in range(len(change_list)):      #通过for循环来打印未进行位置调换时的对应的位置的值
        print("交换前的第{}个值为：{}".format((i+1),change_list[i]),end='\t')
    print()
    for i in range(len(change_list)-1):    #通过for循环来进行位置调换
        change_list[i],change_list[i+1] = change_list[i+1],change_list[i]

    for j in range(len(change_list)):    #通过for循环来进行调换位置后对应的位置的值的输出
        print("交换后的第{}个值为：{}".format((j+1),change_list[j]),end='\t')
    #print(change_list)
    return change_list       #返回change_list

user_change = []   #定义一个空别表，来接收用户输入
user_change.extend(input("请输入您要调换位置的值（中间用空格隔开）：").split(" "))    #用户输入的值存放到列表中

change(user_change)