# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习session_自动管理cookie_5.py
# Author       : 大壮
# Create time  : 2019-10-15 20:56
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

url = 'http://127.0.0.1:5000/'
url_login = 'http://127.0.0.1:5000/login'

# 创建会话对象 Session会话机制
session = requests.Session()

# 会话访问
res = session.post(url_login)

res1 = session.post(url)
print(res1.text)

"""
data 和 header 是什么类型？？？字典类型
res = request.get(url, params=data, header=headers)

响应对象三种格式
res.text 文本格式 , res.content 二进制格式, res.json() json格式
res.cookies 获取全部的cookie

post 请求有三种方式传递参数 parames, data, json
是用哪一种根据接口文档、
res = request.post(url, params=data, header=headers)

requests.Session() 会话机制，
作用：动态管理cookie，集中管理所有的资源，不需要手工进行设置
s = requests.Session() 和 requests.get 和 s.get 是一样的作用
"""
