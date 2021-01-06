# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : connect_mysql.py
# Author       : 大壮
# Create time  : 2020-01-22 15:14
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import pymysql
from pymysql.cursors import DictCursor

# 建立连接
connect = pymysql.connect(
    host='127.0.0.1',  # 连接名
    port=3306,  # 端口
    user='root',  # 用户名
    password='root',  # 密码
    charset='utf8',  # 不能写utf-8 在MySQL里面写utf-8会报错
    database='pymysql_test',  # 数据库库名
    cursorclass=DictCursor  # 数据转换成字典格式
)

# 创建“游标” 每一次查询数据或者操作都是由游标来进行
cursor = connect.cursor()

# 发起请求
sql = "select * from authors where authorId = %s;"
# 使用 execute 查询数据，并传递参数
cursor.execute(sql, args=[1, ])

# 获取数据, 获取一条记录
res = cursor.fetchone()
connect.commit()
print(res)
# 获取数据, 获取所有记录
# 调用了fetchone以后，fetchall 是从第二行开始的，是因为游标读取完第一行后，跑到了第二行
# 最好是每查询一次就关掉
cursor.execute(sql, args=[1, ])
res1 = cursor.fetchall()
connect.commit()
print(res1)
# 关闭游标
cursor.close()
# 断开数据库连接
connect.close()
