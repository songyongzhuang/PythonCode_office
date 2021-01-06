# --*-- coding : utf-8 --*--
# Project      : test-yqhk-Project
# Current file : logger.py
# Author       : 菜鸟一号
# Create time  : 2020-12-10 09:46
# IDE          : PyCharm
# MAIL         : 邮箱地址
# TODO 成长很苦，进步很甜，加油！
import logging
import os
from logging.handlers import RotatingFileHandler
import time
from framework.dir_path import DirPath

"""
日志
"""

formats = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H-%M", time.localtime())
log_path = os.path.join(DirPath.logs_dir, f'Web_logging_{curTime}.log')
handler_2 = RotatingFileHandler(log_path, backupCount=20, encoding='utf-8')
logging.basicConfig(format=formats, datefmt=datefmt, level=logging.DEBUG, handlers=[handler_1, handler_2])

if __name__ == '__main__':
    logging.debug('-----日志-----')
