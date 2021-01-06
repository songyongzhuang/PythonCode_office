#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/23 19:58
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import logging
from configparser import NoSectionError, NoOptionError, ConfigParser


class ConfigHandler:

    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.config = ConfigParser()
        a = self.config.read(filename, encoding=encoding)
        # self.config = config

    def read(self, section, option):
        """读取配置文件某一项"""
        try:
            return self.config.get(section, option)
        except NoSectionError:
            print('没有这个 section')
        except NoOptionError:
            print("没有这个 option")

    def read_2(self, section, option):
        try:
            return self.config[section][option]
        except NoSectionError:
            print('没有这个 section')
        except NoOptionError:
            print("没有这个 option")

    def write(self, section, option, value, mode='w'):
        """写操作"""
        if self.config.has_section(section):
            self.config.set(section, option, value)
            with open(self.filename, mode=mode, encoding=self.encoding) as f:
                self.config.write(f)
                # f.write(config)

    def get_list(self, section, option):
        option_str =  self.read(section, option)
        # list 转化
        if isinstance(eval(option_str), list):
            return eval(option_str)
        return None


class LoggerHandler():
    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                 **kw
                 ):
        """初始化函数。完成 level, format, handler 配置"""
        # 初始化 logger
        logger = logging.Logger(name, level=level)

        self.logger = logger

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)
        # handler 的级别
        handler.setLevel(handler_level)
        # 添加 handler
        logger.addHandler(handler)
        # 设置 format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)

    def info(self, msg, *args, **kwargs):
        """info 级别日志"""
        return self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return self.logger.debug(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        return self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.logger.critical(msg, *args, **kwargs)


class LoggerHandlerTwo(logging.Logger):
    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                 **kw
                 ):
        """初始化函数。完成 level, format, handler 配置"""
        # 子类的初始化使用了父类的 # Dog, eating
        super().__init__(name, level=level)

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)
        # handler 的级别
        handler.setLevel(handler_level)
        # 添加 handler
        self.addHandler(handler)
        # 设置 format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


conf = ConfigHandler('setting.ini')
logger = LoggerHandlerTwo(conf.read('logger', 'name'),
                          level=conf.read('logger', 'level'),
                          fmt=conf.read('logger', 'format'))




