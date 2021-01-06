# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : d1.py
# Author       : 大壮
# Create time  : 2019-10-03 10:29
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import logging

# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0

# 快速创建一个logger收集器，RootLogger
# RootLogger(WARNING) ==> 继承自Logger
# RootLogger 的等级是warning
logging.warning('hello world')  # 这是快速初始化logging

# logger, 设置改变值
logger = logging.getLogger('debug_logger')
logger.setLevel('DEBUG')

#
handler = logging.StreamHandler()
handler.setLevel('DEBUG')
logger.addHandler(handler)

logger.debug('hello world')

# 什么时候用logging快速收集器RootLogger, 什么时候用定义的logging.getLogger()
# 1.学习的时候的方便使用 调试, 写代码阶段
# 2.生熟框架, 或者生产代码。logger = logging.getLogger('demo')自定义logger收集器.


# logger收集器, 具体Logger类
logger_demo = logging.Logger('demo', level=0)
handler = logging.StreamHandler()
handler.setLevel('DEBUG')
logger_demo.addHandler(handler)
logger_demo.info('正在测试logger demo')






