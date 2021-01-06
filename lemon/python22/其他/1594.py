

"""
pyCharm = 'aAb bCd vEf A A '
print(pyCharm.replace('A', '哪吒', 2))  # 替换, 后面可以设置修改的次数，注意, 不会修改原字符串. 会返回一个替换后的新字符串.
print(pyCharm.find('a', 1))  # 存在则返回出现的索引值, 否则返回-1.
print(pyCharm.count('A'))  # 返回字符串出现的次数
print(pyCharm.split('A'))  # split 方法根据指定的分割字符串, 将原字符串分割成多个部分, 以列表形式返回.
print(pyCharm.lower())  # 全部小写
print(pyCharm.upper())  # 全部大写
print(pyCharm.title())  # 首字母大写, 不是首字母的转换成小写
print(pyCharm.swapcase())  # 大写转小写，小写转大写
print(pyCharm.capitalize())  # 只有最开始的字母大写，其余都小写

# 字符串拼接, 根据来字符串拼接   456字符串968字符串654
print('/'.join(['2019', '08', '21']))

# Str_01为字符串
# Str_01.isalnum() 判断所有字符都是数字或者字母
print(pyCharm.isalnum())
# Str_01.isalpha() 判断所有字符都是字母
print(pyCharm.isalpha())
# Str_01.isdigit() 判断所有字符都是正整数
print(pyCharm.isdigit())
# Str_01.islower() 判断所有字符都是小写
# Str_01.isupper() 判断所有字符都是大写
# Str_01.istitle() 判断所有单词都是首字母大写，像标题
print(pyCharm.istitle())
# Str_01.isspace() 判断所有字符都是空白字符，如：\t、\n、\r
print(pyCharm.isspace())

a = "  sod635  "

print(a.strip())  # 移除字符串两端的空格

"""


# poetry = '远看泰山黑乎乎,上头细来下头粗.茹把泰山倒过来,下头细来上头粗.'
# print(poetry[9:])
# print(poetry[-6:-2:2])

import random
# lst = [random.randint(6, 100) for i in range(23)]
# a = len(lst)
#
# print(lst)
# print(a)



