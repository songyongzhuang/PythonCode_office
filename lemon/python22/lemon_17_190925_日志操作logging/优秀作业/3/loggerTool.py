#-*- coding:utf-8 -*-
# datetime:2019/9/25
# author: jiayuan

# 0925-日志收集器封装
# 日志文件配置有很多参数：
# 0、日志收集器名称
# 1、日志收集器级别；
# 2、日志处理器输出级别

# 请利用配置文件，来封装日志处理模块 LoggerHandler

import logging
from work.proFile.profiletool import ProfileTool


class loggerTool:
    def __init__(self, name, level_1):
        self.sjq_name = name
        self.sjq_level = level_1
        self.pro = ProfileTool("./setting.ini")

    # 获取日志收集器
    def get_logger_sjq(self):
        logger = logging.getLogger(self.sjq_name)
        logger.setLevel(self.sjq_level)
        return logger

    # 获取控制台处理器
    def get_logger_StreamHandler(self, clq_level):
        # 初始化 StreamHandler并设置级别
        con_handler = logging.StreamHandler()
        con_handler.setLevel(clq_level)
        # 初始化输出格式
        con_fmt = logging.Formatter(self.pro.read('StreamHandler', 'format'))
        # 设置处理器输出格式
        con_handler.setFormatter(con_fmt)
        # 将处理器加入日志收集器
        self.get_logger_sjq().addHandler(con_handler)

    # 获取文件处理器
    def get_logger_FileHandler(self, clq_level):
        # 实例化文件处理器
        file_handler = logging.FileHandler(self.pro.read('FileHandler', 'file_name'),
                                           encoding=self.pro.read('FileHandler', 'encoding'))
        # 设置处理级别
        file_handler.setLevel(clq_level)

        # 初始化输出格式
        file_fmt = logging.Formatter(self.pro.read('FileHandler', 'format'))

        # 设置处理器输出格式
        file_handler.setFormatter(file_fmt)
        # 将处理器加入日志收集器
        self.get_logger_sjq().addHandler(file_handler)


if __name__ == '__main__':
    log = loggerTool("日志收集器6", 'DEBUG')
    logger = log.get_logger_sjq()
    log.get_logger_StreamHandler('INFO')
    log.get_logger_FileHandler('ERROR')
    logger.debug("debug22！")
    logger.info("info22！")
    logger.error("error22！")
    logger.critical("critical22！")
