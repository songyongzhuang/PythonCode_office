# -*- coding: utf-8 -*- 
# @Time     : 2019/8/17 23:49 
# @Author   : wolf_eye 
# @Email    : 15840995236@163.com 
# @File     : homework_0904.py
# @student  : 狼眸
# import sys
# import os
#
#
# def get_module():
#     def main_module_name():
#         mod = sys.modules['__main__']
#         print(mod)
#         file = getattr(mod, '__file__', None)
#         return file and os.path.splitext(os.path.basename(file))[0]
#
#     def modname(fvars):
#         file, name = fvars.get('__file__'), fvars.get('__name__')
#         if file is None or name is None:
#             return None
#
#         if name == '__main__':
#             name = main_module_name()
#         return name
#
#     module_name = modname(globals())
#     # print globals()
# print(get_module())

# 新建一个包pack，在包中新建两个模块module1，module2
# Q1：1， 在module1中定义一个函数 func_name，


def func_name(name):
    print(f'第一眼看到{name}，就感觉{name}很帅')
    print(__name__)


print(__name__)

if __name__ == '__main__':
    print('这个模块的自测程序都觉得超哥最帅')

