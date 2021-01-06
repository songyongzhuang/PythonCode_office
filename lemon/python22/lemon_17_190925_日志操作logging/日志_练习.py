# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 日志_练习.py
# Author       : Administrator
# Create time  : 2019-09-26 09:30
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import logging
""" 
# 初始化logger
logging.basicConfig(level='debug')


def epual(a, b, c):
    # 为什么，info和debug没有显示
    logging.debug('DEBUG-10-调试')
    logging.info('INFO-20-信息')
    logging.warning('WARNING-30-发出警告')
    logging.error('ERROR-40-比较严重')
    logging.critical('CRITICAL-50-极其严重，系统要崩了')
    print('c:', c)
    return a+b == c


print(epual(1, 2, 3))
# 大写是属性，小写是函数
# WARNING:root:WARNING
# root表示日志收集器，对debug和info不会记录，
"""

# 完整的用例
# 1、日志收集器：logger
# 2、日志收集器级别
# 3、日志处理器准备：handler
# 4、日志处理器级别设置
# 5、设置日志输出格式：format
# 6、添加日志处理器


# logger 日志收集器
logger_22 = logging.getLogger('22日志收集器')


# 设置日志收集器级别。收集器的级别比较低的时候，信息都会收集起来，但是不一定会展示出来
logger_22.setLevel('DEBUG')
# 处理器的级别不写也是可以的 一般是info
logger_22.setLevel(logging.DEBUG)


# 控制台显示，日志处理器，显示log信息 StreamHandler 控制台
concole_handler = logging.StreamHandler()
concole_handler.setLevel('DEBUG')


# 初始化文件处理器 ，，处理器的级别设置的比较高的时候， FileHandler 写到某一个文件
# filename, mode='a'默认是追加, encoding=None, delay=False
file_handler = logging.FileHandler('demo.log', encoding='utf-8')
concole_handler.setLevel(logging.DEBUG) # 控制台
file_handler.setLevel(logging.DEBUG)


# 日志收集器添加处理器  初始化完一定要把处理器添加收集器
logger_22.addHandler(concole_handler)
logger_22.addHandler(file_handler)


# 设置日志输出格式：format， 和处理器handler关联
# %(name)s 日志记录器的名称,
# %(levelno)s 日志级别(“DEBUG”、“INFO”、“WARNING”、“ERROR”、“CRITICAL”)
# %(pathname)s 日志调用的源文件的完整路径名
# %(filename)s 文件名
# %(lineno)d 哪一行出现问题
# %(message)s 输出来内容
console_fmt = logging.Formatter('%(asctime)s———%(name)s———%(levelno)s———'
                                '%(filename)s———%(lineno)d———%(message)s')
concole_handler.setFormatter(console_fmt)


# 保存到文件
file_fmt = logging.Formatter('%(asctime)s———%(name)s———%(levelno)s———'
                             '%(filename)s———%(lineno)d———%(message)s')
file_handler.setFormatter(file_fmt)

logger_22.debug('22期起航')
'''critical= 50 error= 40 warning= 30 info = 20 debug = 10'''
