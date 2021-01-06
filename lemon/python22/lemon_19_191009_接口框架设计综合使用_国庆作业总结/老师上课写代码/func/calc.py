#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/10/9 20:27
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# 1 + 2 = 3
# 1 + 'a' ==> 预期结果 报错， None

def add(a, b):
    """当a, b 都不是数字的时候，返回 None"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # logger
    # 相加出现问题
    # logger.warning()


def minus(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b


def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b


def division(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b !=0 :
        return a / b
