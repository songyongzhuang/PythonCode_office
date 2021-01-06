#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# datetime:2019/9/23 21:07
# email: wagyu2016@163.com
# author: 雨泽
# copyright: 湖南省零檬信息技术有限公司

# 引入解析配置文件库
from configparser import ConfigParser

# 配置文件他的格式。 .ini .conf
config = ConfigParser()

# 读取配置文件
# os.path
config.read('./setting.ini', encoding='utf-8') # 文件名

print(config)
# print(config.getboolean('teachers', 'name'))
# 自己实现， 封装一个类，Config: def get_list() # eval

# print(config.get('demo', 'file_name'))
#
# # 字典获取
# print(config['demo']['file_name'])
# 解析出来的每一个的 option 都是字符串
#
# 添加 section
# name = yuze
# age = yuze
config.add_section('cases')

# 变更
config['cases']['msg'] = 'hello'
print(config['cases']['msg'])

# 写普通的文件, 'w',
with open('./setting.ini', 'w', encoding='utf-8') as f:
    # f.write(data)
    config.write(f)
    # f.write(config)

# config 封装好的





