# 这也许就是大佬吧
# datetime:2019/08/21 10:06
"""
闭包函数：
1.函数中嵌套一个函数
2.嵌套的内层函数有会外部一个非全局变量的引用（不能引用全局变量）
3.外层函数返回的是内层函数的函数名
"""
# 装饰器
# 需求：为这个以实现的功能函数扩展，
# 要求，遵循开放封闭原则
users = {'username':'python', 'pwd':'123'}


# 闭包函数
def deco(fun):
    a = 100

    def wrapper():
        print(a)
        print(fun)
    return wrapper


def func():
    print('个人中心')


res = deco(100)










# def func():
#     print('123')
# func()