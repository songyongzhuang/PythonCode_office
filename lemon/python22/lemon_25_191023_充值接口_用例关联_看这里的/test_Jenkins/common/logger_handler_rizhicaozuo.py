# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : logger_handler_rizhicaozuo.py
# Author       : 大壮
# Create time  : 2019-10-10 21:01
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import logging


class LoggerHandler(logging.Logger):
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


logger = LoggerHandler('python22')
