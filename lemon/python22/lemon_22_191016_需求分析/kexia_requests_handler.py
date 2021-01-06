# --*-- coding ：utf-8 --*--
# Project      ：python22
# Current file ：kexia_requests_handler.py
# Author       ：Administrator
# Create time  ：2019/10/22 14:58
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import logging

import requests


class RequestsHandler:

    def get(self, url, params=None, **kw):
        """ 发送get情求 """
        try:  # 判断是否是正确的
            res = requests.get(url, params=params, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功运行else的代码
        else:
            return res

    def post(self, url, json=None, **kw):
        """ 发送get情求 """
        try:  # 判断是否是正确的
            res = requests.post(url, json=json, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功运行else的代码
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """ 访问接口，两种格式 """
        if method.lower() == 'get':
            return self.get(url, params=params, **kw)
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return requests.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """ 访问接口，获取json数据 """
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            logging.error("不是json格式的数据")
            return


class RequestsCookieHandler:
    """ cllkie 获取 """

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kw):
        """ 发送get情求 """
        try:  # 判断是否是正确
            res = self.session.get(url, params=params, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功运行else的代码
        else:
            return res

    def post(self, url, json=None, **kw):
        """ 发送get情求 """
        try:  # 判断是否是正确的
            res = self.session.post(url, json=json, **kw)
        except:
            # 记录日志信息
            logging.error('访问不成功')
        # 操作成功运行else的代码
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """ 访问接口，两种格式 """
        if method.lower() == 'get':
            return self.get(url, params=params, **kw)
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return self.session.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """ 访问接口，获取json数据 """
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            logging.error("不是json格式的数据")
            return
