#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/10/18 21:44
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司


# getattr

class Context:
    a = 1
    b = 2

# print(Context.c)


print(getattr(Context, 'c', 'hello'))
