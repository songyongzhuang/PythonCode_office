#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/14 21:51
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


import requests

url = 'http://127.0.0.1:5000/'
url_login = 'http://127.0.0.1:5000/login'
# 创建会话对象
session = requests.Session()

# 会话访问
# res = session.get(url_login)

res1 = session.get(url)
print(res1.text)


"""
data 和 header 是什么类型？？？ 字典类型
res = request.get(url, params=data, header=headers)
# 响应对象
# res.text, res.content, res.json()
# res.cookies 获取 cookie

post 请求 params, data, json 三种传递数据
用哪一种？？？根据接口文档。
res = request.post(url, params=data, header=headers)

requests 的session机制
作用是动态管理 cookie, 几种管理所有的资源，不需要我们手工进行设置
s = request.Session(),  requests.get 和 s.get()
s.get()

"""