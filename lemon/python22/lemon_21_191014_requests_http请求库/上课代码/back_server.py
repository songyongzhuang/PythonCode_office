#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/26 20:19
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

from flask import Flask, redirect, jsonify, make_response, Response, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if not request.cookies.get('user'):
        # 验证，session
        return "login"

    return jsonify({"msg":" hello word"})
# 接口是一个函数，类。
# 不是所有函数都是接口，

@app.route('/login', methods=['GET', 'POST'])
def login():
    resp = Response('login success')
    resp.set_cookie('user', 'yuz')
    # 保存到服务端。
    return resp

app.run(debug=True)