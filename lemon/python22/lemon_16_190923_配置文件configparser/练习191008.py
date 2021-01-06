# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习191008.py
# Author       : 大壮
# Create time  : 2019-10-08 20:01
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
# 引入配置文件库
from configparser import ConfigParser

# 配置文件的格式 .ini .conf
# 1.初始化 configparser
config = ConfigParser()  # 根据片名和键名设置value值

# 读取配置文件, 解析 ./ 表示当前文件的文件名
config.read(r'./setting.ini', encoding='utf-8')  # 返回的是一个文件名

print(config)
print(config.get('teachers', 'name'))  # 根据片段名和键名取值
print(config['teachers']['age'])

# 添加，修改
config.set('teachers', 'age1', '17')
with open(r'./setting.ini', 'w', encoding='utf-8') as f:
    config.write(f)

# 删除
config.remove_option('teachers', 'age1')
with open(r'./setting.ini', 'w', encoding='utf-8') as f:
    config.write(f)
