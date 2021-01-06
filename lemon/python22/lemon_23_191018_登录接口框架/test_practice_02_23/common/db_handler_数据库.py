# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : db_handler_shujuku.py
# Author       : 大壮
# Create time  : 2019-10-20 09:05
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pymysql


class DBHandler:
    def __init__(self, host='120.78.128.25',
                 port=3306,
                 user='future',
                 password='123456',
                 charset='utf8',
                 database='futureloan',
                 **kw):
        """ 初始化数据库
        conn = pymysql.connect(
            host=host,  # 主机ip地址
            port=port,  # 端口号不要穿字符串，
            user=user,  # 用户名
            password=password,  # 密码
            charset=charset,  # 编码格式不能写utf-8
            database=database,  # 数据库库名
            **kw
        )"""
        # 建立连接
        self.conn = pymysql.connect(
            host=host,  # 主机ip地址
            port=port,  # 端口号不要穿字符串，
            user=user,  # 用户名
            password=password,  # 密码
            charset=charset,  # 编码格式不能写utf-8
            database=database,  # 数据库库名
            **kw
        )
        # cursor 游标,每一次操作都是通过游标
        self.cursor = self.conn.cursor()

    def query_one(self, sql, args=None):
        """ 查询数据库 args传递参数 fetchone只查询一条数据
        每一次在执行 fetchone 之前都要确保有 execute 在他前面
        """
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    def query_all(self, sql, args=None):
        """ 查询数据库，所有数据 args传递参数 """
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    def query(self, sql, args=None, one=True):
        """ 查询主函数  args传递参数 """
        if one:  # 等于1就执行query_one 这一条
            return self.query_one(sql, args)
        else:  # 否则就执行查询所有数据
            return self.query_all(sql, args)

    def update(self):
        """ 更新 """
        pass

    def close(self):
        """ 关闭 执行完测试用例就要关闭 """
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭数据连接


