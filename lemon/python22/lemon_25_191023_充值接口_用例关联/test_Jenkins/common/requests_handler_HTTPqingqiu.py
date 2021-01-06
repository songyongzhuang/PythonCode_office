
# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : logger_handler_rizhicaozuo.py
# Author       : 大壮
# Create time  : 2019-10-10 21:01
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import logging
import requests


class RequestsHandler:

    def get(self, url, params=None, **kw):
        """发送get请求"""
        # http://:baidu
        try:
            res = requests.get(url, params=params, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送 post 请求"""
        try:
            res = requests.post(url, data=data, json=json, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def request(self, url, data=None, json=None, **kw):
        """发送 post 请求"""
        try:
            res = requests.request(url, data=data, json=json, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return requests.request(method, url, params=params, data=data, json=json, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口，获取 json 数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json 数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是 json 格式的数据")


class RequestsCookieHandler:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kw):
        """发送get请求"""
        # http://:baidu
        try:
            res = self.session.get(url, params=params, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送 post 请求"""
        try:
            res = self.session.post(url, data=data, json=json, **kw)
        except Exception as e:
            # 记录日志信息
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            res = self.get(url, params=params, **kw)
            return res
        elif method.lower() == 'post':
            return self.post(url, data=data, json=json, params=params, **kw)
        else:
            # requests 通用的访问方式
            return self.session.request(method, url, data=data, json=json, params=params, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口，获取 json 数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json 数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是 json 格式的数据")
