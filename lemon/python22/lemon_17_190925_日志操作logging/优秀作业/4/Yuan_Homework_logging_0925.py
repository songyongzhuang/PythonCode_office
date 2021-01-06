# -*- coding:utf-8 -*-

"""
日志收集器封装
日志文件配置有很多参数：
0、日志收集器名称
1、日志收集器级别；
2、日志处理器输出级别
请利用配置文件，来封装日志处理模块 LoggerHandler
"""

import logging
from datetime import datetime
import os

from logging_0925.read_config import ConfigHandler


class LoggerHandler:
    """封装日志出来模块"""

    def __init__(self):
        self.config = ConfigHandler()
        self.dir_name = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件夹地址
        self.log_name = self.config.read_option("Log_info", "log_name")  # 初始化日志收集器的名字

    def my_log(self, msg, level):
        logger = logging.getLogger(self.log_name)
        logger.setLevel('DEBUG')  # 设置日志级别
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')  # 设置日志输出格式

        ch = logging.StreamHandler()  # 渠道指定输出到控制台
        ch.setLevel('DEBUG')  # 设置输出日志级别
        ch.setFormatter(formatter) # 设置输出到控制台的日志格式

        now_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")  # 获取当前时间
        log_path = os.path.join(self.dir_name, now_time + ".txt")   # 拼接log路径和文件名

        fh = logging.FileHandler(log_path, encoding="utf-8")    # 指定日志输出至文件
        fh.setLevel('DEBUG')    # 设置日志输出级别
        fh.setFormatter(formatter)  # 设置输出到文件的日志格式

        logger.addHandler(ch)   # 日志加载控制台
        logger.addHandler(fh)   # 日志加载文件

        # 判定level等级并输出相应信息
        if level == self.config.read_option("Level", "debug"):
            logger.debug(msg)
        elif level == self.config.read_option("Level", "info"):
            logger.info(msg)
        elif level == self.config.read_option("Level", "warning"):
            logger.warning(msg)
        elif level == self.config.read_option("Level", "error"):
            logger.error(msg)
        elif level == self.config.read_option("Level", "critical"):
            logger.critical(msg)

        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        return self.my_log(msg, self.config.read_option("Level", "debug"))

    def info(self, msg):
        return self.my_log(msg, self.config.read_option("Level", "info"))

    def warning(self, msg):
        return self.my_log(msg, self.config.read_option("Level", "warning"))

    def errot(self, msg):
        return self.my_log(msg, self.config.read_option("Level", "error"))

    def critical(self, msg):
        return self.my_log(msg, self.config.read_option("Level", "critical"))


if __name__ == "__main__":  # 增加测试封装的日志类的数据

    log = LoggerHandler()  # 创建实例


    def add(a, b):
        """ 创建2数相除的函数"""
        try:
            c = a / b
            return c
        except ZeroDivisionError as e:
            log.debug("数据错误{}".format(e))


    print(add(1, 0))  # 调用函数
