# -*-coding=utf-8-*-

# 3、你的微信好友当中有 5 个推销的，他们存在一个列表当中, 请把这 5 个人从 black_list 当中删除，最后 black_list 为空

print("*" * 20 + "方法一：切片" + "*" * 20)
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
a = len(black_list)
del black_list[0:a]
print("black_list = {}".format(black_list))

print("*" * 20 + "方法二：pop" + "*" * 20)
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
a = len(black_list)
for i in range(a):
    black_list.pop()
print("black_list = {}".format(black_list))

print("*" * 20 + "方法三：del" + "*" * 20)
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
a = len(black_list)
for i in range(a):
    del black_list[0]
print("black_list = {}".format(black_list))

print("*" * 20 + "方法四：remove" + "*" * 20)
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
a = len(black_list)
i = 0
while i < a:
    black_list.remove(black_list[0])
    i += 1
print("black_list = {}".format(black_list))
