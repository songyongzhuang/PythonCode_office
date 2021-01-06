# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 作业修改版_上课版本.py
# Author       : Administrator
# Create time  : 2019-10-16 11:13
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import requests
import logging


class RequestsHandler:

    def get(self, url, params=None, **kw):
        """ 发送get情求 """
        # url 不符合就会报错，或者超时
        try:
            res = requests.get(url, params=params, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功会运行else下面的代码
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """ 发送post请求"""
        # url 不符合就会报错，或者超时
        try:
            res = requests.post(url, data=data, json=json, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功会运行else下面的代码
        else:
            return res

    def vist(self, url, method, params=None, data=None, json=None, **kw):
        """" 访问接口 """
        # 判断大小写  lower全部替换成大写
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            res = self.post(url, data=data, json=json, **kw)
            return res
        else:
            # request 通用的访问方式
            return requests.request(url, method, **kw)

    def json(self, url, method, params=None, data=None, json=None, **kw):
        """ 获取json数据 """
        res = self.vist(url, method, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error('不是json格式的数据')


class HttpSession:
    """ 封装一个能记住cookie信息的请求类：HttpSession """

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kw):
        """ 发送get情求 """
        # url 不符合就会报错，或者超时
        try:
            res = self.session.get(url, params=params, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功会运行else下面的代码
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """ 发送post请求"""
        # url 不符合就会报错，或者超时
        try:
            res = self.session.post(url, data=data, json=json, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功会运行else下面的代码
        else:
            return res

    def vist(self, url, method, params=None, data=None, json=None, **kw):
        """" 访问接口 """
        # 判断大小写  lower全部替换成大写
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            res = self.post(url, data=data, json=json, **kw)
            return res
        else:
            # request 通用的访问方式
            return self.session.request(url, method, **kw)

    def json(self, url, method, params=None, data=None, json=None, **kw):
        """ 获取json数据 """
        res = self.vist(url, method, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error('不是json格式的数据')
