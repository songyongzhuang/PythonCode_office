# --*-- coding : utf-8 --*--
# Project      : python_test
# Current file : back_server.py.py
# Author       : 大壮
# Create time  : 2019-10-13 11:05
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
from flask import Flask, redirect

app = Flask(__name__)


# 两个结合起来才是一个接口
# 接口地址
@app.route('/', methods=['GET', 'POST'])
# 函数
def index():
    # return '嘻嘻嘻嘻'
    return redirect('/login')


# 接口是一个类、函数
# 不是所欲函数都是接口 调用函数


@app.route('/login')
def login():
    return 'login hello world'


app.run(debug=True)
