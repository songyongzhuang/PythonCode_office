# --*-- coding : utf-8 --*--
# IDE          : PyCharm


# 1、将用户输入的所有数字相乘之后对20取余数
# 用户输入的数字个数不确定
"""
def multiplyList(remainder) :
    a = 1
    for x in remainder:
        a = a * x
    print(a)
    return a % 20


list_c = []  # 创建空列表
while True:
    str_a = input('请输入数字，回复0停止输入：')
    if str_a.replace('.','').isdigit():  # 判断小数
        float_b = float(str_a)   # 转成浮点类型
        if float_b == 0:
            print('退出')
            print('把所有数字相乘之后对20取余, 结果为：', multiplyList(list_c))  #
            break
        else:
            list_c.append(float_b)  # 循环一次，把数据插入到列表
    else:
        print('您输入的数据有误')
"""

# 2、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
'''
def list_length(list_02):
    """外面创建一个列表，传进函数判断是否大于两位，要是大的话进行切片[:2], 索引0"""
    if len(list_02) <= 2:
        return list_02
    else:
        return list_02[:2]


list_01 = []  # 创建一个空列表
while True:
    str_01 = input('请输入数据,(只获取前两位)回复0结束输入：')
    if str_01 is '0':
        print('您输入的数据前两位是：', list_length(list_01))
        break
    else:
        list_01.append(str_01)
'''

# 3、定义一个函数，传入一个字典和字符串，
# 判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典


def pan(list_a, a):
    for i in list_a.values():
        if i is a:
            print('有重复')
        else:
            print('没有重复')
            list_c = {a: a}

    list_a.update(list_c)
    return list_a


list_b = {'b': '小梅花', 'a': 200}
b = '100'
print(pan(list_b, b))

# 4、通过定义一个计算器函数，调用函数传递两个参数，
# 然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
"""
def calculator(symbol, data_01, data_02):
    if symbol == 1:
        data_03 = data_01 + data_02
        return data_03
    elif symbol == 2:
        data_03 = data_01 - data_02
        return data_03
    elif symbol == 3:
        data_03 = data_01 * data_02
        return data_03
    elif symbol == 4:
        data_03 = data_01 / data_02
        return data_03


# print(calculator('4', 5, 3))
list_04 = []  # 创建个空列表，存计算的两个值
a = 1
while True:
    if a <= 2:
        str_04 = input(f'请输入第个{a}数据：')
        if str_04.replace('.', '').isdigit():
            list_04.append(str_04)
            a += 1
        else:
            print('您输入数据有误，请从新输入\n')
    elif a != 2:
        str_4 = input('选择运算\n【1】加 【2】减【3】乘 【4】除：')
        if str_4.isdigit():
            str_4 = int(str_4)
            if 0 < str_4 <= 4:
                print(calculator(symbol=str_4, data_01=float(list_04[0]), data_02=float(list_04[1])))
                break
            else:
                print('您输入的数据有误')
        else:
            print('您输入的数据有误')
"""

# 5、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，
# 询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
aaa = 1
a_5 = 0
while aaa <= 10:
    aaa += 1
    aa = input('请输入您的性别：')
    if aa == '女':
        bb = input('请输入您的年龄：')
        if bb.isdigit():
            bb = int(bb)
            if 15 <= bb <= 22:
                print('您可以加入啦啦队')
                a_5 += 1
            else:
                print('您的年龄不符, 只要15岁到22岁的')
        else:
            print('您输入的年龄有误')
    elif aa == '男':
        print('您的性别不符，只要女生')
    else:
        print('您输入性别有误')
print(f'满足条件的总人数{a_5}')
'''
