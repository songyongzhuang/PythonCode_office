# --*-- coding : utf-8 --*--
# Project      : python_lemon_作业
# Current file : lemon_190823_作业.py
# Author       : 大壮
# Create time  : 2019-08-24 09:04
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！


# 一、.删除如下列表中的"矮穷丑"，写出能想到的所有方法
info = ["yule", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 1、根据值删除, 使用remove方法.
info.remove("矮穷丑")  # 直接输入删除的"矮穷丑".
print(info)

# 2、根据索引删除, 使用pop方法, 根据索引删除元素.
print('删除的是：', info.pop(info.index("矮穷丑")))  # 1.使用index()求出索引, 2.根据索引删除并打印元素.
print(info)

# 3、del 通过索引删除
del info[info.index("矮穷丑")]  # 根据索引删除
print(info)


# 二、有5道小题：
# a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄.
print('欢迎来到相亲节目, 请输入您的个人信息, 谢谢合作.')
personal_data = {}  # 创建一个空字典
name = input('请输入您的姓名：')  # 通过input获取数据
sex = input('请输入您的性别：')
age = input('请输入您的年龄：')
# update()批量添加, 如果key(键)不存在则为添加新元素, 存在则修改
personal_data.update({'姓名': name, '性别': sex, '年龄': age})
print('录入数据成功, 你的信息为：{}'.format(personal_data))  # 打印字典，展示输入的个人信息
print()


# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
print('有一个人对您很感兴趣，平台需要您补足您的身高和联系方式')
stature = input('请输入您的身高：')
phone = input('请输入您的联系方式：')
personal_data.update({'身高': stature, '联系方式': phone})  # 保存补充的数据
print('数据添加成功, 您的信息修改为：{}'.format(personal_data))
print()


# c, 平台为了保护你的隐私，需要你删除你的联系方式；
input('为了保护您的隐私, 我们需要删除您的联系方式, 请按任意键继续：')  # 这样删除是不有点过分[滑稽]
print('您的联系方式:{}, 删除成功.'.format(personal_data.pop('联系方式')))  # 根据key值删除元素
print('数据删除成功, 您的信息修改为：', personal_data)
print()


# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
print('您为了取得更好的成绩，需要取一个花名, 并修改自己的身高和其他您觉得需要改的信息')
new_name = input('请输入您的花名：')
stature = input('请修改您的身高：')
personal_data.update({'花名': new_name, '身高': stature})  # 保存

print('\n请输入其他需要修改的信息：\nps:如需要修改年龄为18,先填入：年龄，再填写：18 ')

while True:  # 不确定循环次数, 用True, 一定要防止死循环
    key = input('请输入其他需要修改的信息：回复“1”放弃修改：')
    if key in personal_data.keys():  # 获取字典的key (键)
        value = input('请输入修改的数据：')
        personal_data.update({key: value})  # 保存到字典里面
        break
    elif key == '1':
        print("您已放弃其他修改")
        break
    else:
        print("\n您没有录入这个信息，请重新输入")
        print("您的信息为", personal_data)

print('修改后的数据为：', personal_data)


# e, 你进一步添加自己的兴趣，至少需要 3 项。一经确定，不可单独修改各个兴趣点。
print('您需要进一步添加自己的兴趣，至少需要 3 项')

new_like = []  # 先新建一个空列表
while True:  # 不确定循环次数, 用True, 一定要防止死循环
    number = (input("请输入需要填写兴趣的项数："))
    if number.isdigit() is True:  # 字符串操作，判断是不是都是正整数
        if int(number) >= 3:  # 判断项目次数至少 3 项
            for i in range(int(number)):  # range() 根据传值循环多少次
                temp = input('请输入要添加的兴趣:')
                new_like.append(temp)  # 列表操作：append末尾追加
            break  # 退出循环.
        print("至少需要 3 项, 请重新输入：")
        continue  # 终止当前次循环, 继续下次循环.
    else:
        print('输入错误，请输入正整数\n')

personal_data.update({'兴趣': tuple(new_like)})  # 把列表转换为元组
print('您现在的信息为：', personal_data)


# 三、现在有一个列表 li2=[1，2，3，4，5]
# 第一步：请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]
li2 = [1, 2, 3, 4, 5]

# 1、向列表中添加元素
li2.insert(0, 0)  # 通过索引添加插入的值
li2.insert(4, 66)
li2.append(11)  # 末尾追加, 只能加一个
li2.extend([22, 33])  # 通过extend添加多个
print(li2)

# 2、第二种方法
li2[0:50] = [0, 1, 2, 3, 66, 4, 5, 11, 22, 33]  # 切片从新赋值
print(li2)


# 第二步：对li2进行排序处理
# 对列表中的元素排序, 默认升序
li2.sort()
print('li2:', li2)
# 对列表中的元素排序, 降序排列
li2.sort(reverse=True)
print('li2:', li2)


# 第三步：请写出删除列表中元素的方法，并说明每个方法的作用
# 1.根据值删除
li2.remove(1)  # 只能删除一个, 根据值删除, 删除找到的第一个

# 2.根据索引删除
li2.pop(1)  # 只能删除一个, 可以写负数, 有返回值

# 3.del
del li2[1]  # 根据索引删除
del li2[0:4]  # 删除多个, 切片删
del li2  # 删除列表, 列表都没了

# 4.clear
li2.clear()  # 删除整个列表里面的元素
