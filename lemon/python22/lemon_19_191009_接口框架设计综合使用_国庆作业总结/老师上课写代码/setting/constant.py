#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# datetime:2019/10/9 21:20
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司
import os


class BasePath:
    pass


class ProjectPath(BasePath):
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    CONFIG_PATH = os.path.join(ROOT_PATH, 'setting')

class SubPath(ProjectPath):
    pass


p_path = ProjectPath()
