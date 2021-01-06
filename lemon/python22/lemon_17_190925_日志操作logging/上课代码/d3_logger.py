#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/25 19:57
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# logger
import logging


def equal(a, b, c):
    # 为什么没有显示出来。
    # root.debug
    logging.debug("查看 a, b") #error:root:..
    logging.info("a + b == c")
    logging.warning("正在抓取日志 WARNING")
    logging.error("正在抓取日志 ERROR")
    logging.critical("正在抓取日志 CRITICAL")
    return a + b == c


# logger 日志收集器, 收集log信息, 日记本
logger_22 = logging.getLogger('python22的日志收集器')
logger_22_cp = logging.getLogger('python22_cp 的日志收集器')

# 设置日志收集器的级别，信息我都会收集
logger_22.setLevel(logging.DEBUG)


# 控制台显示  日志处理器， 哪里显示我们的log 信息
concole_handler = logging.StreamHandler()
# 初始化文件处理器
file_handler = logging.FileHandler('demo.log', encoding='utf-8')

# 处理器的级别
concole_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.WARNING)


# 日志收集器添加处理器
logger_22.addHandler(concole_handler)
logger_22.addHandler(file_handler)


# 设置输出格式， 处理器 handler 关联的。
console_fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s ")
concole_handler.setFormatter(console_fmt)


file_fmt = logging.Formatter("%(asctime)s-%(name)s-%(message)s")
file_handler.setFormatter(file_fmt)


# 1， 收集器
# 2， 设置收集器的界别
# 3， 初始化处理器
# 4， 处理器的级别
# 5， 添加处理器
# 6， 初始化格式器
# 7， 设置处理器的格式

# 收集器级别低，
# 处理器的级别高。


def run(a, b):
    try:
        a / b
    except:
        logger_22.error("a / b  报错")


# run(2, 0)
run(1, 2)


