"""
--*-- coding : utf-8 --*--
Project      : python_lemon
Current file : lemon_190819_作业.py
Author       : 大壮
Create time  : 2019-08-23 19:25
IDE          : PyCharm
"""

# 一、现在有字符串：str1 = 'python cainiao 666'
#     1、请找出第 5 个字符。
str1 = 'python cainiao 666'
print(str1[4])  # 字符串的索引从零开始，第五个其实就是 5-1

#     2、请复制一份字符串，保存为 str_two
str_two = str1[:]  # 切片，起始位置和结束位置都不填，就是复制一份字符串
print(str_two)

#     3、请找出最中间的字符。
str_length = len(str1)  # 1.先求出字符串的总长度.
str_average = str_length / 2  # 2.再用总长度除以二，计算平均值
print(str1[int(str_average)])  # 3.除法的返回结果是浮点数类型，所以要进行数据转换.
# 简化版，一步到位...
print('啊哈哈', str1[int(len(str1) / 2):int(len(str1) / 2)+1])
print(int(len(str1) / 2))
print(int(len(str1) / 2)+1)
# 1.找中间字符，没考虑有字符串个数是奇数还是偶数


# 二、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False  # 偶数就是双数,奇数就是单数
# （提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）
average = input('请输入一个整数：')
print(int(average) % 2 == 0 and True or False)


# 三、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！
tangerine_price = input('请输入橘子的价格：')
tangerine_weight = input('请输入橘子的重量：')
# 转换为浮点类型的原因就是：价格和重量不可能都是整数，都是几斤几两，必然会用到浮点类型(小数)
print('应付金额为：', (float(tangerine_price) * float(tangerine_weight)))

# print('应付金额为：', round((float(tangerine_price) * float(tangerine_weight)), 3))  # 解决 7.8500000000000005
# print('应付金额为：%.2f' % (float(tangerine_price) * float(tangerine_weight)))  # 解决 7.8500000000000005


# 四、a = True , b = (99 // 2 == 1), c = 0 判断真假：
# ont:非     取反，真亦假，假亦真。
# and:与    只有两个都是真才是真，只要一个为假，那么就是假
# or:或     只要有一个为真，就是真，只有两个为假，才是假
# 1是真，0是假

# print('', 99 // 2 == 1)
# 结果是：False  99//2取整数是45，显而易见45不可能等于 1

# 1， not b
print('判断 not b 的结果为：', not (99 // 2 == 1))
# TODO 结果是：True (not取反，本来是假，取反就是真)

# 2， a and b
print('判断 a and b 的结果为：', True and False)
# TODO 结果是：False (只有两个都是真才是真。a是真，b是假)
# print("a and b：", True and (99 // 2 == 1))

# 3， a and b and c
print('判断 a and b and c 的结果为：', True and False and False)
# TODO 结果是：False (没有括号就从左往右看，两两比较，只要有一个是假结果必定是假)
# print('a and b and c：', True and (99 // 2 == 1) and 0)

# 4， (a or c) and b
print('判断 (a or c) and b 的结果为：', (True or False) and False)
# TODO 结果是：False
# (先比较括号里的,or只要有一个为真,就是真, 括号里面的结果是：真(True)。
# 再计算外面，(True and False),and只有两个都是真才是真 , 结果为：False)
# print('(a or c) and b：', (True or 0) and (99 // 2 == 1))
