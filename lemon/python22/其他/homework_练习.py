
import requests

url = "http://127.0.0.1:5000/"
data = {"username":'ye', "pwd":'123456'}
# 发送 请求需要（url 参数）
res = requests.post(url, data=data)
# print(res.text)
print(res.status_code)  # 状态码
print(res.content.decode())

# cookie  获取
cookies = res.cookies


url1 = "http://127.0.0.1:5000/"
res1 = requests.post(url1, cookies=cookies)
print(res1.text)
