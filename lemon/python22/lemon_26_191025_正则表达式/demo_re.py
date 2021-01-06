# --*-- coding ：utf-8 --*--
# Project      ：Python22
# Current file ：demo_re.py
# Author       ：Administrator
# Create time  ：2019/10/28 10:58
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

import re
"""
# 匹配到了返回一个对象，没有匹配到
a = re.match(r'yangjiao', 'yangjiao123')
# 分组，得到匹配的内存
print(a.group(0))
"""

# 非贪婪模式
# 这里的\* 这是表示字符串* . 非换行符零次或者一次 +表示至少一个
# ？非泛滥模式 \* 表示字符串*

pattern = r'\*(.+?)\*'
my_string = '{"username": "*phone*", "pwd": "*pwd*"}'
# sub 先把目标字符串能匹配到的先查找出来，根据后面的进行替换次数
b = re.sub(pattern, '13333333333', my_string, 1)
print(b)
