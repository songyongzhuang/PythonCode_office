# -*- encoding: utf-8 -*-

# @Author  :   满满
# @Contact :   867232508@qq.com
# @Software:   PyCharm
# @File    :   test_log.py
# @Time    :   2019/9/26 12:32
# @Desc    :

import logging
import datetime
import os
from utils_0818.config import ConfigHandler
from logging.handlers import TimedRotatingFileHandler


# 项目根目录位置
base_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(base_name, 'log')


class LoggerHandler(object):

    def __init__(self, logger_name):
        """
        1、初始化收集器
        2、设置收集器级别
        3、初始化日志处理器
        4、设置日志处理器级别
        5、设置日志输出格式
        6、日志输出格式关联文件处理器
        7、文件处理器关联收集器
        """
        config = ConfigHandler('setting.ini')
        # self.logger_name = config.read('log', 'logger_name')
        self.file_name = config.read('log', 'file_name')
        # 日志输出级别
        self.file_output_level = config.read('log', 'file_output_level')
        self.console_output_level = config.read('log', 'console_output_level')

        # 初始化收集器
        self.logger = logging.getLogger(logger_name)
        # 设置收集器日志级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志输出格式
        pattern = config.read('log', 'pattern')
        self.format = logging.Formatter(pattern)

    def get_log(self):
        file_name = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        file_name = os.path.join(log_path, file_name)

        '''判断日志是否有句柄，有句柄的话直接返回'''
        if not self.logger.handlers:
            # 初始化日志处理器
            # file_output = logging.FileHandler(self.file_name,encoding='utf-8')
            # when='D',每天生成新的日志文件
            file_output = TimedRotatingFileHandler(file_name, when='D', interval=1, backupCount=3, encoding='utf-8')
            # 设置日志处理器的级别
            file_output.setLevel(self.file_output_level)
            file_output.setFormatter(self.format)
            self.logger.addHandler(file_output)

            console_output = logging.StreamHandler()
            console_output.setLevel(self.console_output_level)
            console_output.setFormatter(self.format)
            self.logger.addHandler(console_output)
        return self.logger


if __name__ == '__main__':
    log = LoggerHandler('python22第二次日志')
    log.get_log().warning('python第er次测试')
    log.get_log().warning('python  test')
