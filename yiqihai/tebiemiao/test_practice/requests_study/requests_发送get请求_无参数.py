# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : requests_发送get请求_无参数.py
# Author       : 大壮
# Create time  : 2020-01-13 11:38
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import requests

# requests 第三方库
#   安装： pip install requests todo 文件名称千万不要和 requests 同名
url = 'http://127.0.0.1:5000/'
res = requests.get(url)  # 没有参数就不用传递参数
print('打印出来的一个对象：\n', res)  # 打印出来的一个对象
# 状态码
print('状态码：\n', res.status_code)
# 返回的数据 文本，用来接收普通文本
print('返回的数据 文本：\n', res.text)
# 接受响应数据，二进制 b开头 二进制，服务器返回二进制数据，图片、视频等
print('返回二进制 b开头：\n', res.content)
# 接受响应数据， decode() 二进制转换成字符串
print('二进制转换成字符串：\n', res.content.decode())
# json格式是字典格式
# 接受响应数据，js格式 如果服务器返回的不是 json 格式的会报错
# 当服务器返回的是标准的json格式时候使用，接口主要用 json 格式
print('js格式：\n', res.json())
