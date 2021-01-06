# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : lemon_191014_requests作业.py
# Author       : Administrator
# Create time  : 2019-10-15 14:54
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
# 1、 封装一个能记住cookie信息的请求类：HttpSession
# 2、 封装一个不需要记住cookie信息的请求类：HttpRequest
# 封装 4 个方法：
# - get
# - post
# - visit (可以同时处理 get 和 post 请求)
# - get_json (可以同时处理 get, post, 且返回 json 格式数据)

# 导入 requests 第三方库
import requests


class HttpRequest(object):
    """ 封装一个不需要记住cookie信息的请求类：HttpRequest """

    def request_get(self, url, headers):
        """ get """
        res = requests.get(url=url, headers=headers)
        return res

    def request_post(self, url, json, headers_register):
        """ post """
        res = requests.post(url, json=json, headers=headers_register)
        return res

    def visit(self, request , url , json, headers):
        """ 可以同时处理 get 和 post 请求 """
        if request == 'GET':
            res = requests.get(url=url, headers=headers)
            return res
        elif request == 'POST':
            res = requests.post(url=url, json=json, headers=headers)
            return res
        else:
            return '仅支持 GET 和 POST 请求'

    def get_json(self, request , url , headers, json=None):
        """ 可以同时处理 get, post, 且返回 json 格式数据 """
        if request == 'GET':
            res = requests.get(url=url, headers=headers)
            return res.json()
        elif request == 'POST':
            res = requests.post(url=url, json=json, headers=headers)
            return res.json()
        else:
            return '仅支持 GET 和 POST 请求'


class HttpSession:

    def cookie(self, url_login, url):
        # 创建会话对象 Session会话机制
        session = requests.Session()
        # 会话访问
        res = session.post(url=url_login)
        res1 = session.post(url)
        return res1.json()


# ======================  不需要记住cookie信息的  ======================
request = HttpRequest()
# -----------  注册 -----------
url_register = 'http://120.78.128.25:8766/futureloan/member/register'
headers_register = {'X-Lemonban-Media-Type': 'lemonban.v1', 'Content-Type': 'application/json'}
json = {"mobile_phone": '13333333333', 'pwd': "123456789", 'type': 0}
print('注册post', request.request_post(url=url_register, json=json, headers_register=headers_register).json())

# -----------  登录 -----------
url_enter = 'http://120.78.128.25:8766/futureloan/member/login'
print('登录post', request.request_post(url=url_enter, json=json, headers_register=headers_register).json())

# -----------  查看用户信息  -----------
url_information = 'http://120.78.128.25:8766/futureloan/member/167/info'
print('查看用户信息get', request.request_get(url=url_information, headers=headers_register).json())

# -----------  get_json  -----------

print(request.get_json('GET', url=url_information, headers=headers_register))
print(request.get_json('POST', url=url_enter, json=json, headers=headers_register))


# ======================  Session会话机制 存储cookie  ======================
httpsession = HttpSession()
url = 'http://127.0.0.1:5000/'
url_login = 'http://127.0.0.1:5000/login'
print(httpsession.cookie(url=url, url_login=url_login))