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
        option_str = self.read(section, option)
        # list 转化
        if isinstance(eval(option_str), list):
            return eval(option_str)
        return None


class LoggerHandler:
    def __init__(self, name, level=0, file_name=None, handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                 **kwargs):
        """ 初始化函数，完成level, fromat, handler 配置 """
        # logger = logging.getLogger(name)  # 使用第二种
        # 初始化logger 第二种 收集器
        logger = logging.Logger(name, level=level)
        self.logger = logger
        # 初始化handler
        if file_name is None:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)
        # 添加handler, 设置handler的级别
        handler.setLevel(handler_level)
        logger.addHandler(handler)
        # 设置format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


if __name__ == '__main__':
    logger = LoggerHandler('demo')
    logger.logger.info('打印')

