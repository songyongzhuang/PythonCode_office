# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190906.py
# Author       : 大壮
# Create time  : 2019-09-07 07:46
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
"""
# 导入模块，路径处理
import os

# 获取现在的文件夹路径
# 在哪里运行就打印运行的路径，在哪里运行的python, 就是获取这个文件夹
# 获取当前的工作目录，这种方式很少使用
# print(os.getcwd())


# 文件的绝对路径
# 绝对不会变，非常有用
a = os.path.abspath(__file__)


# 获取路径的文件夹路径
b = os.path.dirname(os.path.abspath(__file__))
# print(os.path.dirname(a))


# 创建文件
# 路径拼接
# 字符串拼接
# print('字符串拼接：', end='')
# c = os.path.join(b, 'data', 'ddd')

# 路径拼接
# print('路径拼接：', end='')
# 一个反斜杠表示转移，需要写两个
# 还需要处理操作系统，还有反斜杠
# print(b + '\\')

# 创建文件夹, mkdir, 要一层一层创建
# os.mkdir(c)
# 判断文件是否存在
# os.path.exists()
# c = os.path.join(b, 'data', 'ddd')
# c_01 = os.path.dirname(c)
# if os.path.exists(os.path.dirname(c)):
#     os.mkdir(c_01)
# else:
#     print("文件夹不存在")


# 创建一个文件
# os.mkdir(os.path.join(b, 'data'))


# 判断某个路径是否存在 返回的是布尔类型
# print(os.path.exists(os.path.join(b, 'data')))


# 判断是否是一个文件夹
# print(os.path.isdir(os.path.join(b, 'data')))

# 判断是否是一个文件
# print(os.path.isfile(os.path.join(b, 'data')))

"""


""" 内置函数
a = print('hello')
print(a)  # None

mylist = ['呜呜', '梅梅', '棒棒糖']
c = mylist.append('哈哈')
print(c)  # None
# print(mylist.append('小雨'))  # None

# 同时获取值和索引
for index, w in enumerate(mylist):
    print(index, w)
    
"""


# -------------------- 文件操作 --------------------------------
"""
# 文件读写
# 内置函数
# open()
# f = open('demo.txt', encoding='utf-8')

# 读文件的内容
# print(f.read())

# 写文件
# f = open('new_fil.txt', mode='r', encoding='utf-8')
# f.write('人生苦读，我用python')
# print(f.readlines())

# 关闭文件，当执行了打开文件操作，一定要记得关闭
f.close()

# with open('demo.txt', mode='r', encoding='utf-8') as f:
#     print(f.read())
"""


# -------------------- 异常处理 --------------------------------

# 异常处理
try:
    1/0
except ZeroDivisionError:  # 错误类型一定要调试，不能用别的代替
    print('不能看小姐姐')
except IndexError:
    print('不能去打篮球')

# try遇到错误代码就终止就不执行，判断错误类似是否是except后面的错误类型
# 找对应的错误类型，判断所有的except，找到就运行下面的代码，没有就把所有的except都执行完毕
