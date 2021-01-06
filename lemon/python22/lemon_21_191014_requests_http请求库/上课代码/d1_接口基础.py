#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/10/14 19:52
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# requests 第三放库 pip install requests
import requests

# 发送 http 请求的。
# get, post, put, delete

# 发送 get 请求 requests.get(url, 参数)
url = 'http://127.0.0.1:5000/'
res = requests.get(url)
print(res)
# 状态码
print(res.status_code)
# 返回的数据文本， 主要用来接收普通文本或者 html
print(res.text)
# 接收响应数据，二进制形式.服务器返回二进制数据，图片，视频
print(res.content)
# json 格式的响应， 是字典格式,
# 如果服务器返回的不是一个json格式的。会报错。
# 当服务器返回的是标准的json格式的时候。接口主要用 json 格式
print(res.json())

print('hello')


