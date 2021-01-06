# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 练习_自动管理cookie.py
# Author       : Administrator
# Create time  : 2019-09-30 10:35
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# import logging
#
# # 快速创建一个logger收集器，RootLonger
# # RootLogger(WARNING) --> 继承自 Logger
# # RootLogger 的等级是：warning 30
# logging.info('hello world')


def dafd(deposit, expect):
    A = 1  # 年
    B = deposit  # 10000存的钱
    while B < expect:
        b = B * 0.0352
        B += b
        A += 1

    return f'{A}年'


print(dafd(deposit=1000, expect=2000))


# save_money = float(input("请输入你要存入银行的钱："))
# print("你存了{}元到银行!".format(save_money))
# TOTAL_MONEY = save_money * 2  # 定义变量用于保存总钱数
#
# year = 1  # 定义变量用于记录年份
#
# while save_money < TOTAL_MONEY:
#
#     save_money *= (1 + 0.0352)
#
#     year += 1
#
# print("定期利率为3.52%，需要{}年本金和才能翻一番。".format(year))




































