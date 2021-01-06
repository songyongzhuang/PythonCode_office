# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : module1.py
# Author       : Administrator
# Create time  : 2019-09-05 08:42
# IDE          : PyCharm
# 新建一个包pack，在包中新建两个模块module1，module2

# 1， 在module1中定义一个函数 func_name，
""""""
# 2，在module2中导入module1中定义的函数，并调用。

# 3,  在module2 中定义一个 func_name 会存在什么问题？？
"""
再定义一个func_name会存在重名现象，只会运行一个
存在两个同名的要给调用的起一个别名区分
"""

# 4， 在 2 个模块中分别 print(__name__), 运行 module1 的时候会打印什么？  运行 module2 的时候会打印什么？
"""
运行 module1 , __name__ 主程序运行时，会打印“__main__”, 
在module2 运行的时候会打印：模块的名称

__name__,被主程序调用时，打印的是__main__
不是主程序运行打印的是:模块的名称
"""

# 什么是模块？有什么作用？
"""
什么是模块：在python里面，一个py文件就是一个模块

模块的作用：
1、模块可以被别的程序引入
2、可以在另外的函数调用其他地方封装好的函数
3、可以调用同一个项目里的，不同的文件
"""
# 模块的导入方式有哪几种？
"""见 module2"""


def func_name(name):
    print(f'{name}正在努力赚钱')
    return True


a = '失败是成功之母'


print(__name__)
# 被module2运行打印的是模块的名称
# 在自己模板运行打印的是 __main__






