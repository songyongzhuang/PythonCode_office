#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/25 20:49
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

class Movie:

    def __new__(cls, *args, **kwargs):
        print("正在 new")
        return super().__new__(*args, **kwargs)

    def __init__(self):
        print("正在初始化")
        self.a = 'a'

movie = Movie()
print(movie.a)