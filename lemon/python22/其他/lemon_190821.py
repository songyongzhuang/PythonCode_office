"""
Project      : python22
Current file : lemon_190821.py
Creator      : Administrator
Create time  : 2019-08-22 08:40
IDE          : PyCharm
"""

# 1、现在有字符串：'hello python18 !'（注意点:转换之后单词之间有空格），转化成列表 li = [‘hello’,‘python18’,‘!’]
print('-' * 30)
data = 'hello python18 !'
print(data.split(' '))  # split() 根据指定分割字符串, 将字符串分割成多个部分, 以列表形式返回.
li = (data.split(' '))
print('li = {}'.format(li))  # 控制台打印列表


# 2、把 username = 'There is sweet man named yuze, 18 sui' 中的 'man' 字符串取出来
print('-' * 30)
username = 'There is sweet man named yuze, 18 sui'
location = username.find('man')  # find() 返回索引, 没有返回-1.
print(username[location:location+3])  # 字符串长度3，后面索引需要加3


# 3、将给定字符串前后的空格除去，把PHP替换为Python，
#  best_language = "     PHP is the best programming language in the world!      "。左右各有一个空格。
print('-' * 30)
best_language = "     PHP is the best programming language in the world!      "
print((best_language.strip()).replace('PHP', 'python'))  # strip() 去除两侧空格、replace() 替换字符
print('-' * 30)


# 4.演练字符串操作
my_hobby = "Never stop learning!"

# 截取从 位置2 ~ 位置6 的字符串
print(my_hobby[1:6])  # ever

# 截取从 位置2 ~ 末尾 的字符串
print(my_hobby[1:])  # ever stop learning!

# 截取从 开始位置~ 位置6 的字符串
print(my_hobby[:6])  # Never

# 截取完整的字符串
print(my_hobby[:])  # Never stop learning!

# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])  # e tplann!

# 从右边开始截取，倒数第 2位置 到 倒数 5位置，步长为2
print(my_hobby[-2:-5:-2])  # gi

# 截取字符串末尾两个字符
print(my_hobby[-2:])  # g!

# 字符串的逆序
print(my_hobby[::-1])  # !gninrael pots reveN

# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），
# “索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）

