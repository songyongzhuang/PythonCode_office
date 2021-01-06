# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : 作业_修改版01.py
# Author       : 大壮
# Create time  : 2019-09-10 21:44
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


# 0906-文件异常作业
# 截至：09月09日  16:00 展示词云
# 1.编写如下程序
# 创建一个txt文本文件，来添加数据
# a.第一行添加如下内容：
# name,age,gender,hobby,motto


# b.从第二行开始，每行添加具体用户信息，例如：
# yuze,17,男,假正经, I am yours
# cainiao,18,女,看书,Lemon is best!


# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
# person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "", "motto": "hehe"}
#
#
#
# d.将所有用户信息写入到txt文件中之后，然后再读出
#
#
#
#
#
# 2.编写如下程序
# 有两行数据，存放在txt文件里面：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
# [{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
# {'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
#
#
#
#
#
#
# 3.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
#
#
#
# 3.编写如下程序
# 优化剪刀石头布游戏程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
