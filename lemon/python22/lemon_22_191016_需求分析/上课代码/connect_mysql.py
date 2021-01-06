#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/16 21:46
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# pymysql, oracle,
# 连接 == 》
import pymysql

# 建立连接
from pymysql.cursors import DictCursor

conn = pymysql.connect(
    host='120.78.128.25',
    port=3306,
    user='future',
    password='123456',
    charset='utf8', # 不能是 utf-8
    database='futureloan',
    cursorclass=DictCursor

)

# cursor 游标 每一次操作的
cursor = conn.cursor()

sql = "SELECT * FROM member WHERE id=%s;"

cursor.execute(sql, args=[2])

# 获取数据 获取一条记录
res = cursor.fetchone()
print(res)
# 获取所有的记录
# res1 = cursor.fetchall()
# print(res1)

cursor.close()
conn.close()
