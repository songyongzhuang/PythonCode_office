# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : helper.py
# Author       : 大壮
# Create time  : 2019-10-24 20:13
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
import random  # 随机数


def mk_phone():
    """ 随机生成手机号码 """
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        # 取值九次
        num = str(random.randint(0, 9))
        phone += num

    return phone


if __name__ == '__main__':
    print(mk_phone())
