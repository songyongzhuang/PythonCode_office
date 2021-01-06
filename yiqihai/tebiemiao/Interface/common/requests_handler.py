# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : requests_handler.py
# Author       : 大壮
# Create time  : 2020-01-19 15:55
# IDE          : PyCharm
import requests
import logging
from Interface.common import logger


class RequestsHandler:
    """ 不需要记住cookie信息的请求类 """

    def get(self, url, params=None, **kwargs):
        """ 发送get请求
        params 传递参数就是放到URL里面传递
        data 在form表单中传递参数 """
        try:
            res = requests.get(url, params=params, **kwargs)
        except Exception:
            # 记录异常到日志
            logging.info('访问get请求不成功')
            # raise  # 手动抛出异常
        else:
            # 操作成功运行 else
            return res

    def post(self, url, data=None, json=None, **kwargs):
        """ 发送post请求 """
        try:
            res = requests.post(url, data=data, json=json, **kwargs)
        except Exception:
            # 记录异常到日志
            logging.info(url, data, json, **kwargs)
            logging.info('访问post请求不成功')
        else:
            # 操作成功运行 else
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        访问 get 和 post 接口
        :param method：请求方法
        :param url：URL地址
        :param params：参数放到URL里面传递，
        :param data：在form表单中传递参数
        :param json：json 格式
        """
        #  lower 转换成小写
        if method.lower() == 'get':
            return self.get(url, params=params, **kwargs)
        elif method.lower() == 'post':
            return self.post(url, params=params, data=data, json=json, **kwargs)
        else:
            # 其他请求
            # requests 通用的访问方式  其他的也是使用的 request 进行的具体封装
            return requests.request(method, url, params=params, data=data, json=json, **kwargs)

    def json(self, method, url, params=None, data=None, json=None, **kwargs):
        """ 访问接口， 获取json数据 """
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        logging.info(res)  # TODO
        # 获取json 数据
        try:
            return res.json()
        except:
            logging.info('获取json 数据失败，不是json格式的数据')


class RequestsCookieHandler:
    """ 记住coolie信息的请求类 """

    def __init__(self):
        # Session 管理 cookie  作用是动态管理cookie
        self.session = requests.Session()

    def get(self, url, params=None, **kwargs):
        """ 发送get请求
        params 传递参数就是放到URL里面传递
        data 在form表单中传递参数 """
        try:
            res = self.session.get(url, params=params, **kwargs)
        except Exception:
            # 记录异常到日志
            logging.info('coolie请求类，访问get请求不成功')
            # raise  # 手动抛出异常
        else:
            # 操作成功运行 else
            return res

    def post(self, url, data=None, json=None, **kwargs):
        """ 发送post请求 """
        try:
            res = self.session.post(url, data=data, json=json, **kwargs)
        except Exception:
            # 记录异常到日志
            logging.info('coolie请求类，访问post请求不成功')
        else:
            # 操作成功运行 else
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kwargs):
        """
        访问 get 和 post 接口
        :param method：请求方法
        :param url：URL地址
        :param params：参数放到URL里面传递，
        :param data：在form表单中传递参数
        :param json：json 格式
        """
        #         lower 转换成小写
        if method.lower() == 'get':
            return self.get(url, params=params, **kwargs)
        elif method.lower() == 'post':
            return self.post(url, params=params, data=data, json=json, **kwargs)
        else:
            # 其他请求
            # requests 通用的访问方式
            return self.session.request(method, url, params=None, data=None, json=None, **kwargs)

    def json(self, method, url, params=None, data=None, json=None, **kwargs):
        """ 访问接口， 获取json数据 """
        res = self.visit(method, url, params=params, data=data, json=json, **kwargs)
        # 获取json 数据
        try:
            return res.json()
        except:
            logging.info('coolie请求类，获取json 数据失败，不是json格式的数据')
