# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : logger.py
# Author       : 大壮
# Create time  : 2020-01-13 10:43
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import logging
import os
from logging.handlers import RotatingFileHandler
import time
from setting.project_path import ProjectPath

"""
日志
"""

formats = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

# 控制台显示
handler_1 = logging.StreamHandler()
# 本地时间，格式年月日时分  strftime 将元组装换成字符串，localtime 当前时间
curTime = time.strftime("%Y-%m-%d %H-%M", time.localtime())
# 创建日志路径
log_path = os.path.join(ProjectPath.logs_dir, f'Autotest_{curTime}.log')

handler_2 = RotatingFileHandler(log_path, backupCount=20, encoding='utf-8')
# 设置root logger 的输出内容形式，输出渠道
# format 日志格式、datefmt 时间格式、level日记级别、handlers
logging.basicConfig(format=formats, datefmt=datefmt, level=logging.DEBUG, handlers=[handler_1, handler_2])

if __name__ == '__main__':
    logging.debug('日志')
