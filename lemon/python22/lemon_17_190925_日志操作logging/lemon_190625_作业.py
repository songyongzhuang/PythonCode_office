# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : lemon_190625_作业.py
# Author       : Administrator
# Create time  : 2019-09-26 09:30
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# 0925-日志收集器封装
# 截至：09月27日  18:00展示词云
# 日志文件配置有很多参数
# 0、日志收集器名称
# 1、日志收集器级别
# 2、日志处理器输出级别
# 请利用配置文件，来封装日志处理模块 LoggerHandler

import logging
import configparser


class Handler(object):

    def __init__(self, file, mode='w', encoding=None):
        # 1、初始化ConfigParser
        self.config = configparser.ConfigParser()

        self.file = file  # 文件名
        self.mode = mode  # 模式
        self.encoding = encoding  # 编码格式
        # 2、读取配置文件，填写文件名称，编码格式
        self.config.read(self.file, self.encoding)

    def read_file(self, section, option):
        """读取配置参数"""''
        try:
            a = self.config.get(section, option)
            return a
        except configparser.NoSectionError:
            return '请输入正确的片名'
            # raise
        except configparser.NoOptionError:
            return '请输入正确的键名'


class LoggerHandler(Handler):

    def __init__(self, name):
        super(Handler, self).__init__()
        # 日志收集器
        self.logger_22 = logging.getLogger(name)

    def journal_rank(self, rank='INFO'):
        # 设置日志收集器级别
        self.logger_22.setLevel(rank)
        print(f"日志收集器级别：{rank}")

    def initialize_processor(self, file_name, rank='INFO',mode='a', encoding='utf-8'):
        # 初始化文件处理器, 处理器的级别设置的高获取的日志越少
        # file_name FileHandler 写到某一个文件
        # rank 处理器的级别
        self.file_handler = logging.FileHandler(file_name, mode=mode, encoding=encoding)
        # rank 处理器的级别
        self.file_handler.setLevel(rank)
        print(f"初始化文件处理器：{rank}")

    def journal_addition(self,layout):
        # 日志收集器添加处理器  初始化完一定要把处理器添加收集器
        self.logger_22.addHandler(self.file_handler)
        self.file_fmt = logging.Formatter(layout)
        self.file_handler.setFormatter(self.file_fmt)

        self.logger_22.warning('22期起航')


handler = Handler(file='./setting.ini', encoding='utf-8')
logger = LoggerHandler('22日志收集器')  # 日志收集器名字
logger.journal_rank(handler.read_file('deploy', 'debug'))  # 设置日志收集器级别
logger.initialize_processor('demo.log', rank=handler.read_file('deploy', 'debug'))  # 初始化文件处理器
logger.journal_addition(layout='%(asctime)s———%(name)s———%(levelno)s———'
                               '%(filename)s———%(lineno)d———%(message)s')
