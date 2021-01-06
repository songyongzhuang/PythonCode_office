# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 连接数据库_pymysql.py
# Author       : Administrator
# Create time  : 2019-10-17 16:56
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

#  安装：pip install pymysql
import pymysql
from pymysql.cursors import DictCursor


# 建立连接
conn = pymysql.connect(
    host='120.78.128.25',  # 主机ip地址
    port=3306,  # 端口号不要穿字符串，
    user='future',  # 用户名
    password='123456',  # 密码
    charset='utf8',  # 编码格式不能写utf-8
    database='futureloan',  # 数据库库名
    cursorclass=DictCursor  # 转换成字典格式
)

# cursor 游标,每一次操作都是通过游标
cursor = conn.cursor()

# 发起请求，是游标发起的
sql = 'select * from member where id = %s'
# 动态传递cid 只能传递 元组、字典、列表
cursor.execute(sql, args=[1])

# 获取所有的数据
res = cursor.fetchall()
print(res)


# 断开连接
cursor.close()  # 游标
conn.close()  # 库
