# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 练习配置文件setting.py
# Author       : 大壮
# Create time  : 2019-09-24 23:07
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


""" 
配置项，相当于默认值
默认数据相当于常量，就是不变化的量
以配置项的方式存储常量

全局，常量可以用大写
# 配置文件的格式：.ini  .conf
""" ''
# 引入解析配置文件库 ConfigParser
import configparser

# 1、初始化ConfigParser
config = configparser.ConfigParser()

# 2、读取配置文件，填写文件名称，编码格式
# ./ 当前文件
config.read('setting.ini', encoding='utf-8')
"""
print(config.get('teachers', 'name'))  # 获取某一个
print(eval(config.get('demo', 'file_name')))

# get 字典获取
print(config['demo']['file_name'])

# 自带的转换
print('asdfasdf',config.getint('teachers', 'age'))
# 自己实现eval
# 还要封装

# 查询是否包含某个属性
# print(config.has_option("demo", "age"))  # 当section或者option不存在时。结果都为False

"""
# 修改属性的值。属性不存在时功能为添加。若组不存在会报错。
# 第一个参数为组名，第二个参数为属性名，第三个参数为属性的值
# try:
#     config.set("demo", "age", "18")
#     with open('./setting.ini', "w", encoding='utf-8') as f:
#         config.write(f)
#         print('修改成功')
# except configparser.NoSectionError:
#     print('请输入正确的片名')

# # # 增加属性
# config.set("demo", "age2", "11") # 第一个参数为组名，第二个参数为属性名，第三个参数为属性的值
# with open('./setting.ini', "w", encoding='utf-8') as f:
#     config.write(f)
# #
# # # 删除属性
try:
    config.remove_option("demo", "age1")
    with open('./setting.ini', "w", encoding='utf-8') as f:
        config.write(f)
        print('123456')
except configparser.NoSectionError:
    print('请输入正确的片名')

# 添加section
# 他不是写入普通的文件，是config封装好的
# config.add_section('cases')
# config['cases']['msg'] = 'hello'
# with open('./setting.ini', 'w', encoding='utf-8') as f:
#     config.write(f)  # 写入，write格式

