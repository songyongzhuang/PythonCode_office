#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/14 21:12
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

import requests

url = 'http://127.0.0.1:5000/login'
data = {"username":"yuze", "pwd":"1234556"}
# 传递参数的三种方式， params, data, json
res = requests.post(url, data=data)
# c
print(res.text)
# 获取所有的 cookie
cookies = res.cookies


url1 = 'http://127.0.0.1:5000'
res1 = requests.post(url1, cookies=cookies)
print(res1.text)



