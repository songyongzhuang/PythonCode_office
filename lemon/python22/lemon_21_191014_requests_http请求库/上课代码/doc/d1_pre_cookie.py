#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/12 17:49
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import requests

# res = requests.get('http://localhost:5000/login')
# print(res.text)
#
# cookies = res.cookies
#
# res = requests.get('http://localhost:5000', cookies=cookies)
# print(res.text)



session = requests.Session()

res = session.get('http://localhost:5000/login')
print(res.text)


res = session.get('http://localhost:5000')
print(res.text)

