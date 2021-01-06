# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习requests_get不带参数.py
# Author       : 大壮
# Create time  : 2019-10-15 19:59
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！

# requests 第三方库  pip install requests
import requests

# 发送 http 请求
# (get, post), put, delete

# 发送 get 请求 requests.get(url地址，参数)
url = 'http://127.0.0.1:5000/'
res = requests.get(url)  # 没有参数就不用传递参数
print(res)  # 打印出来的一个对象

# 状态码
print(f'返回的响应码：{res.status_code}')  # 返回的响应码


# ------------------ 接收文本的几种方式 ------------------
# 返回的数据 文本形式  主要用来接收普通文本或者XTML格式
print(f'返回的数据 文本：\n{res.text}')
# 接收响应数据：二进制形式  服务器返回二进制数据：图片或者视频
print(f'二进制：{res.content}')
print(f'二进制转换字符串：\n{res.content.decode()}')

# json 格式的响应 得到的 json 是字典格式的
# 如果服务器返回的文本不是一个 json 格式的，会报错
# 当服务器返回的是一个标准的json格式的，接口主要用 json 格式
print(f'json 格式：{res.json()}')
