# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 练习2.py
# Author       : Administrator
# Create time  : 2019-09-16 15:03
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

"""
读取文件
"""

"""
def read_file(filename, encoding):
    with open(filename, encoding=encoding) as f:
        a = f.read()
    return a


def write_file(filename, encoding):
    with open(filename, 'w', encoding=encoding):
        pass
"""

'''
class FileHandler:

    def __init__(self,filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding

    def read_file(self):
        """ 读取文件 """
        with open(self.filename, encoding=self.encoding) as f:
            a = f.read()
        return a

    def write_file(self, data, mode='w'):
        """ 写文件 """
        with open(self.filename, mode, encoding=self.encoding) as f:
            f.write(data)


handler = FileHandler('demo.txt')
print(handler.read_file())

# import sys
# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)
# print('\n\nThe PYTHONPATH is', sys.path, '\n')
'''


class DaLaoParent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bbb(self):
        print(f'{self.a}爱上了{self.b}...')

    def ccc(self, type):
        print('刺客伍六七')


class DaLao(DaLaoParent):
    """ 继承上面的类 """''

    def aaa(self):
        DaLaoParent('阿珍', '阿强')
        super().__init__('阿珍', '阿强')
        super().ccc(type)
        print(f'{self.a}爱上了{self.b}, 在一个没有星星的夜晚')


dalao = DaLao('阿珍', '阿强')
dalao.aaa()


# c = '没有星星','阿珍', '阿强'


























