# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : mo_ni_jie_ko_cheng_xu.py
# Author       : Administrator
# Create time  : 2019-10-15 15:33
# IDE          : PyCharm


from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if not request.cookies.get('user'):  # 没有cookies就返回not login
        return 'not login'
    return jsonify({'msg': 'hello world'})


@app.route('/login')
def login():
    resp = Response('login success')
    resp.set_cookie('user', 'python')
    return resp


app.run(debug=True)
