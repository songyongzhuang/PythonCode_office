# --*-- coding ：utf-8 --*--
# Project      ：python22
# Current file ：db_handler.py
# Author       ：Administrator
# Create time  ：2019/10/24 15:23
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
from pymysql.cursors import DictCursor

from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.db_handler_shujuku \
    import DBHandler  # 数据库
from lemon_25_191023_充值接口_用例关联.test_practice_01_25.common.config_handler_peizhiwenjian \
    import config  # 配置文件


class MyDBHandler(DBHandler):
    def __init__(self, **kw):  # 获取的数据默认是元组
        super().__init__(
            host=config.read('db', 'host'),
            port=eval(config.read('db', 'port')),  # int类型去掉两端字符串
            user=config.read('db', 'user'),
            password=config.read('db', 'password'),
            charset=config.read('db', 'charset'),
            database=config.read('db', 'database'),
            cursorclass=DictCursor,  # 默认是元组
            **kw
            )
