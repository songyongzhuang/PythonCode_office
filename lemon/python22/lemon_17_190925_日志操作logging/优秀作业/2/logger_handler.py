# -*- coding:UTF-8 -*-
# @Time     : 2019/9/26 13:44
# @Author   : yizizhiyue
# @Email    : yizizhiyue@qq.com
# @File     : logger_handler.py
# @Software : PyCharm
import os
import logging
from class_0925.config.config_handle import ConfigHandler

class LoggerHandler:
    def __init__(self, log_name, log_path):
        self.log_name = log_name
        self.log_path = log_path

    def my_log(self, log_level='DEBUG', handler_level='DEBUG', message=''):
        ''' 对日志的收集、输出进行封装处理
        :param log_level: 日志收集器级别
        :param handler_level: 处理器级别
        :param message: 信息
        '''
        # 进行大写处理
        log_level = log_level.upper()

        # 定义日志收集器
        mylogger = logging.getLogger(self.log_name)
        # 设定级别
        mylogger.setLevel(log_level)

        # 设置处理器
        logging.StreamHandler
        file_handle = logging.FileHandler(self.log_path, 'a', encoding='utf-8')
        file_handle.setLevel(handler_level.upper())
        fmt = logging.Formatter('%(filename)s-%(asctime)s-%(levelname)s-日志信息：%(message)s')
        file_handle.setFormatter(fmt)

        # 与处理器建立连接
        mylogger.addHandler(file_handle)

        # 收集日志
        if log_level == 'DEBUG':
            mylogger.debug(message)
        elif log_level == 'INFO':
            mylogger.info(message)
        elif log_level == 'WARNING':
            mylogger.warning(message)
        elif log_level == 'ERROR':
            mylogger.error(message)
        elif log_level == 'CRITICAL':
            mylogger.critical(message)

        # 关闭处理器 （否则每一次新日志的输出都会同时输出上一次的信息，造成重复输出）
        mylogger.removeHandler(file_handle)

    def debu(self, handle_level='debug', msg=''):
        self.my_log('debug', handle_level, msg)

    def info(self, handle_level='debug', msg=''):
        self.my_log('info', handle_level, msg)

    def warning(self, handle_level='debug', msg=''):
        self.my_log('warning', handle_level, msg)

    def error(self, handle_level='debug', msg=''):
        self.my_log('error', handle_level, msg)

    def critical(self, handle_level='debug', msg=''):
        self.my_log('critical', handle_level, msg)

if __name__ == '__main__':
    # 调试
    # 从配置文件读取关于log的配置信息
    uppath = os.path.dirname(__file__)
    cf = ConfigHandler(os.path.join(uppath, 'config', 'setting.ini'))
    # log收集器名称
    logname = cf.get('LOG', 'logger_name')
    # log文件路径
    filepath = cf.get('LOG', 'file_handler_path')
    # 处理器级别
    stream_level = cf.get('LOG', 'stream_handler_level')

    # 日志收集
    lg = LoggerHandler(logname, filepath)
    lg.info(stream_level, 'info级别log信息1')
    lg.debu(stream_level, 'debug级别log信息2')
    lg.warning(stream_level, 'warning级别log信息3')
    lg.error(stream_level, 'error级别log信息4')
    lg.critical(stream_level,'critical级别log信息5')


