# 这也许就是大佬吧
# datetime:2019/08/19 11:43


import keyword

# user_email = 'simagousheng@itcast.cn'
# print(user_email.count('s'))  # 返回字符串出现的次数
# print(user_email.find('s', 2))  # 位置
# print(user_email.split('@'))  # 根据@ 切片
# print(user_email.split('@')[0], user_email.split('@')[1])


# and:与     只要两个都是真才是真，只要一个为假，那么就是假
# or:或     只要有一个为真，就是真，只有两个为假，才是假
# print(False and True)  # False
# print(False and False)  # False
# print(True and True)  # True
# print(True and False)  # False
#
# print(False or True)  # True
# print(False or False)  # False
# print(True or True)  # True
# print(True or False)  # True

# 列表添加元素：.append
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# bicycles.append('123456')
# print(bicycles)


# 使用方法insert()可在列表的任何位置添加新元素.
# bicycles.insert(1, '123456')
# print(bicycles)

# 从列表中删除元素使用del语句
# del bicycles[1]
# print(bicycles)

# 方法pop()可删除列表末尾的元素
# print(bicycles.pop())  # 打印弹出的值，以证明我们依然能够访问被删除的值
# print(bicycles)
# 使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
# print(bicycles.pop(1))  # 打印弹出的值，以证明我们依然能够访问被删除的值
# print(bicycles)


# 根据"值"删除元素，使用方法remove()。
# motorcycles = ['a', 'hoinda', 'yamaha', 'suzuki', 'ducati', 'd', 'z']
# print(motorcycles)

# motorcycles.remove('hoinda')
# print(motorcycles)


# 使用sort()对列表进行永久性排序是按字母顺序排列
# motorcycles.sort()
# print(motorcycles)

# 也可以与字母排序相反的顺序排列元素,在方法中传递参数：reverse=True
# motorcycles.sort(reverse=True)
# print(motorcycles)


# 倒着打印列表 reverse() 反转列表元素
# motorcycles.reverse()
# print(motorcycles)

# 确定列表的长度
# print(len(motorcycles))

# motorcycles = ['a', 'hoinda', 'yamaha', 'suzuki', 'ducati', 'd', 'z']
# # for a in motorcycles:
# #     print(a.title())  # title() 首字母大写
# print(type(motorcycles))
# print(len(motorcycles))

# average = input('请输入一个整数：')
#
# print(int(average) % 2 is 0 and True or False)
# print(id(int(average) % 2))
# print(id(0))


# 方法一:remove
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.remove("矮穷丑")
print("删除后的结果为：%s" % info)

# 方法二:pop
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.pop(3)
print("删除后的结果为：%s" % info)

# 方法三:del
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
del info[3]
print("删除后的结果为：%s" % info)


# 方法四:for循环遍历列表

info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info_new = []
for target in info:
    if target is not "矮穷丑":
        info_new.append(target)
print("删除后的结果为：{0}".format(info_new))


# 方法五：根据索引进行遍历
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info_new = []
target_index = info.index("矮穷丑")
for i in range(len(info)):
    if i != target_index:
        info_new.append(info[i])
print("删除后的结果为：{new_info}".format(new_info=info_new))


# 方法六：函数写法，返回删除后的结果并打印输出
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]


def info_result(n):
    info_new = []
    for target in n:
        if target != "矮穷丑":
            info_new.append(target)
    return info_new
print("删除后的结果为：{}".format(info_result(info)))


# 方法七：采用filter函数进行过滤
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]


def filter_result(x):
    return x != "矮穷丑"
# 对info列表进行过滤，把非"矮穷丑"，即True的值筛选出来
info_new = list(filter(filter_result, info))
print("删除后的结果为：{0}".format(info_new))


# 方法八:lambda结合map的使用

info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 对info列表的每个元素进行判断，判断结果为bool值
# 以列表的形式保存在li中，非"矮穷丑"的bool值即False，找到对应位置，根据索引删除
li = list(map(lambda x: x != "矮穷丑", info))
index = 0
for i in li:
    index += 1
    if i == False:
        break
    else:
        continue
del info[index-1]
print("删除后的结果为：{0}".format(info))


