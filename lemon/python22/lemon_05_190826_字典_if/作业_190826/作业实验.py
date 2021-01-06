# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 作业实验.py
# Author       : Administrator
# Create time  : 2019-08-27 09:14
# IDE          : PyCharm
# isdigit() 判断所有字符是否都是正整数
# isalnum() 判断所有字符都是数字或者字母

# player_int = int(input('123456'))
#
# if 4 > player_int != 0:
#     print(f'您出拳为：{player_int}')
#     if player_int < 4 and player_int != 0:
#         print('哈哈')
#
# elif player_int == 4:
#     print('游戏结束')
#
# else:
#     print('您的输入有误, 请重新输入.\n')


# int(money) >= 50 and int(money)<= 100:

# num = input("input:")
# if num.replace(".", '').isdigit():
#     print(num.replace(".", ''))
#     if num.count(".") == 0:
#         print('int')
#     elif num.count(".") == 1:
#         print('float')
#     else:
#         print("即不是int类型,也不是float类型")
# else:
#     print("即不是int类型,也不是float类型")


# while True:
#     money = input('请您输入购买金额(回复“退出”退出本系统)：')
#     if len(money) <= 13:  # 判断字符串长度
#         if money.replace('.', '').isdigit():  # replace方法不会改变原字符串, 把所有的"."替换成"", 再判断是不是纯数字.
#             if money.count('.') < 2:  # 用count来查找字符串中的".", 判断"."要小于2个(一个点, 或者没有点)
#                 float_money = float(money)  # 字符串转为浮点类型
#                 if len(float_money.split('.')[1]) <= 2:  # 根据"."切割, 判断"."位数只能小于等于2
#                     if float_money == 0:
#                         print('您的输入数据有误, 金额不能为零.\n')
#                     elif 50 <= float_money <= 100:  # 包含50元和100元
#                         print('您购买的商品价格为：{}元, 给予10%折扣, 最终价格为：{:.2f}元.\n'
#                               .format(float_money, (float_money - float_money * (10 / 100))))  # 折扣百分比除100就是
#                     elif float_money > 100:
#                         print('您购买的商品价格为：{}元, 给予20%折扣, 最终价格为：{:.2f}元.\n'
#                               .format(float_money, (float_money - float_money * (20 / 100))))
#                     else:
#                         print(f'您购买的商品价格为：{float_money}元, 没有折扣, 只有购买五十及以上金额才有折扣. \n')
#                 else:
#                     print('您输入的数据有误, 最大为两位小数')
#             else:
#                 print('您的输入数据有误请重试\n')
#         elif money == '退出':
#             print('退出系统成功, 期待您的下次使用, 祝您生活愉快.')
#             break
#         else:
#             print('您的输入数据有误请重试\n')
#     else:
#         print('您的输入数据有误请重试, 最大长度为13\n')


# money = '4561'
# float_money = money
# a = float_money.split('.')[1:]
#
# b = int(len(a[0:][0]))
# print(b)
# print(b > 2)
#
# while True:
#     money = input('请您输入购买金额(回复“退出”退出本系统)：')
#     if money.replace('.', '', 1).isdigit():  # replace方法不会改变原字符串, 把所有的"."替换成"", 再判断是不是纯数字.
#         float_money = float(money)  # 字符串转为浮点类型
#         if float_money == 0:
#             print('您的输入数据有误, 金额不能为零.\n')
#         elif 50 <= float_money <= 100:  # 包含50元和100元
#             print('您购买的商品价格为：{}元, 给予10%折扣, 最终价格为：{:.2f}元.\n'
#                   .format(float_money, (float_money - float_money * (10 / 100))))  # 折扣百分比除100就是
#         elif float_money > 100:
#             print('您购买的商品价格为：{}元, 给予20%折扣, 最终价格为：{:.2f}元.\n'
#                   .format(float_money, (float_money - float_money * (20 / 100))))
#         else:
#             print(f'您购买的商品价格为：{float_money}元, 没有折扣, 只有购买五十及以上金额才有折扣. \n')
#     elif money == '退出':
#         print('退出系统成功, 期待您的下次使用, 祝您生活愉快.')
#         break
#     else:
#         print('您的输入数据有误请重试\n')

# a = 1
# if isinstance(a, (int, tuple)):
#     print('a 是一个整数或者元组')
# else:
#     print('a 不是一个整数或者元组')

# bool(), 空,,{}, [], (), 0, ""  这些都是空值，
name = 1
if name:
    print('看这里')
