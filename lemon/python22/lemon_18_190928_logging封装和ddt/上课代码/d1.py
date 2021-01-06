#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/28 17:27
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


import logging

# 快速创建一个 logger 收集器， RootLogger
# RootLogger(WANING)  ==> 继承自 Logger
# RootLogger 的登记是 warning,
logging.warning('hello world')

# logger 不去手动的添加 handler, 默认的handler, 默认级别就是 warning
logger = logging.getLogger('debug_logger')
logger.setLevel('DEBUG')

# handler,
handler = logging.StreamHandler()
handler.setLevel('WARNING')
logger.addHandler(handler)

logger.debug('hello world')

# 什么时候用 logging 快速收集器 RootLogger, 什么时候用自定义的 logging.getLogger()
# logging, 1, 学习时， 调试，写代码阶段。
# 成熟框架，或者生产代码。 logger = logging.getLogger('demo') 自定义 logger 收集器。


# logger 收集器，具体 Logger 类
logging.getLogger('demo')
logger_demo = logging.Logger('demo', level=0)
handler = logging.StreamHandler()
handler.setLevel('DEBUG')
logger_demo.addHandler(handler)
logger_demo.info("正在测试 logger demo")



# 练习 python 基础
# 实战顺畅，解决问题的能力。

