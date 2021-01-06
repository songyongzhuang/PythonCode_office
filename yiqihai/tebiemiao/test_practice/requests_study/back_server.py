# --*-- coding : utf-8 --*--
# Project      : Interface
# Current file : back_server.py
# Author       : 大壮
# Create time  : 2020-01-13 10:55
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from flask import Flask, redirect, jsonify, make_response, Response, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if not request.cookies.get('user'):
        # 验证，session
        return jsonify({"mag": "login"})
    return jsonify({"msg": " hello word"})


# 接口是一个函数，类。
# 不是所有函数都是接口，

@app.route('/login', methods=['GET', 'POST'])
def login():
    resp = Response('login success')
    resp.set_cookie('user', 'python')
    # 保存到服务端。
    return resp


app.run(debug=True)
