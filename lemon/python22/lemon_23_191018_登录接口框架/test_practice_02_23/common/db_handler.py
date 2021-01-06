# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : db_handler.py
# Author       : 大壮
# Create time  : 2019-10-22 20:19
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 导入
import pymysql


class DBHandler(object):
    """ 初始化数据库 """

    def __init__(self,
                 host=None,
                 port=3306,
                 user='root',
                 password='',
                 charset='utf8',
                 database=None,
                 **kwargs
                 ):
        # 建立连接
        self.conn = pymysql.connect(
            host=host,  # 主机ip地址
            port=port,  # 端口号不要穿字符串，
            user=user,  # 用户名
            password=password,  # 密码
            charset=charset,  # 编码格式不能写utf-8
            database=database,  # 数据库库名
            **kwargs
        )
        # 初始化游标对象
        self.cursor = self.conn.cursor()
        # TODO 游标要是查询的是同一条sql，每次执行 fetchone 之前都要有 execute

    def query_one(self, sql, args=None):  # args与查询一起使用的参数，往SQL语句中传递值
        """ 查询一条数据信息 """
        # execute()查询一条
        self.cursor.execute(sql, args)
        # 返回一条记录(row)，如果没有结果 , 则返回 None
        return self.cursor.fetchone()

    def query_all(self, sql, args=None):
        """ 查询所有数据信息"""
        # execute()查询一条
        self.cursor.execute(sql, args)
        # 返回多条记录(rows),如果没有结果,则返回 ()
        return self.cursor.fetchall()

    def query(self, sql, args=None, one=True):
        """ 判读是读取一条数据还是多条 """
        if one:  # noe 的默认值是一，默认查询一条数据
            return self.query_one(sql, args=None)
        return self.query_all(sql, args=None)

    def close(self):
        """ 关闭游标和库连接
        tearDown 测试框架-它在每次用例执行完之后会执行一次
        """
        self.cursor.close()
        self.conn.close()

