# -*- coding: utf-8 -*- 
# @Time     : 2019/8/17 23:49 
# @Author   : wolf_eye 
# @Email    : 15840995236@163.com 
# @File     : homework_0904.py
# @student  : 狼眸0

# Q2，在module2中导入module1中定义的函数，并调用。
# from lemon_10_pack import module1_wolf
from lemon_09_190904_包和模块导入.优秀作业.module1_wolf import func_name


# def func_name(name):
#     print(f'第二眼看到{name}，还是感觉{name}很帅')
#     print(__name__)


# module1_wolf.func_name('超哥')
func_name('超哥')
print(__name__)


# def func_name(name):
#     print(f'第二眼看到{name}，还是感觉{name}很帅')
#     print(__name__)

# Q3: 在module2 中定义一个 func_name 会存在什么问题？
# 此问题从两个维度考虑——导包方式、func_name定义位置
# （1）若导包方式只导入到模块，没有导入到对应函数，那么调用函数方式为 模块名.函数，此种情况不论func_name在当前模块中定义
# 在哪里，执行的都是在module1的func_name函数
# （2）若导报方式导入到函数名，那么调用函数的方式，直接写函数名就可以：
#  此时，若module2中新定义的func_name在函数调用前，那么调用的是当前module2中新定义的func_name函数
#  若module2中新定义的func_name在函数调用后，那么调用的是module1中定义的func_name函数


# Q4：在 2 个模块中分别 print(__name__), 运行 module1 的时候会打印什么？  运行 module2 的时候会打印什么？
#  主模块中执行print(__name__)会打印__main__，调用模块执行print(__name__)会打印当前模块路径
# （1）在module1中运行print(__name__)，打印结果输出__main__，表示程序当前运行在主模块中
# （2）在module2中只运行print(__name__)，打印结果输出__main__；
#      导入模块module1，打印结果为lemon_10_pack.module1_wolf（因为导入模块会执行模块中所有顶格内容）
#      调用module1中func_name函数，打印结果为lemon_10_pack.module1_wolf，执行了函数中的print()

# Q5: 什么是模块？有什么作用？
# 模块就是一个.py文件（不论文件中是否定义内容都可以完成导入，只不过导入空模块没有可调用内容）
# 模块可以通过import导入的方式，来实现模块之间的相互调用。
# 避免将所有程序写在同一个文件中，不方便维护；亦或者某一个函数在不同的模块中都要用到，可以通过模块导入的方式完成调用，
# 避免在每个模块都要写一遍这个函数等。

# Q6：模块的导入方式有哪几种？
# （1）import 包.模块名
# （2）import 包.模块名 as 昵称（网名）
# （3）from 包.模块名 import 函数名
# （4）from 包.import 模块
# （5）from ... import ... as 新名称
# （6）from ... 模块 import *  所有内容（慎用，考虑导入内容与当前模块内容中有同名函数等）
