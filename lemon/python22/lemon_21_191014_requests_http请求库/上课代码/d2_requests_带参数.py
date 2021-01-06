#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/14 21:12
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

import requests

url = 'http://127.0.0.1:5000/'
data = {"username":"yuze", "pwd":"1234556"}
res = requests.get(url, params=data)
print(res.text)

# 带请求头
headers = {"user-agent": "huawei p30"}
res = requests.get(url, params=data, headers=headers)
print(res.text)