# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : mo_ni_jie_ko_cheng_xu.py
# Author       : Administrator
# Create time  : 2019-10-15 15:33
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app. route('/', methods=['GET', 'POST'])
def index():
    if not request.cookies.get('user'):  # 没有cookies就返回not login
        # 验证, session
        return jsonify({'msg': 'hello world'})
    return jsonify({'msg': 'hello world'})


@app. route('/login', methods=['GET', 'POST'])
def login():
    resp = Response('login success')
    resp.set_cookie('user', 'py')
    # return resp
    return resp


app.run(debug=True)
