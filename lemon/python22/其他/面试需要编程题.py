# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : 面试需要编程题.py
# Author       : Administrator
# Create time  : 2019-09-26 18:17
# IDE          : PyCharm
# TODO 成长很苦, 进步很甜, 加油！

#  整数数组里两个数之和为183的所有整数对（列如，输入数据为{10, 183, 0, 2, 182, 100, 83, 1, 181, 173}，得到结果为（183,0）（-184,367））
result_list = []
datas = [10, 183, 0, 2, 182, 100, 83, 1, 181, 173]
for key, value in enumerate(datas):
    for i in range(key, len(datas)):
        if value + datas[i] == 183:
            result_list.append((value, datas[i]))

print(result_list)


#  处理这种问题
a = 'test jobs test work test jobs'


def fenge(tata):
    data = tata.split(' ')  # 根据空格分隔
    new_data = [[i, data.count(i)] for i in set(data)]
    # sort对列表进行排序
    new_data.sort(key=lambda x: x[1], reverse=True)
    for i in new_data:
        print(i[0], i[1])

fenge(a)

"""
作为标准的 996 程序员，小胖长期伏案写代码体重剧增，下定决心开始跑步减肥。在
连续跑了4个月（这里当做120天）后，小胖查看自己的跑步APP的打卡记录，发现有N
天偷懒没打卡。 
于是小胖购买了M张 "补打卡"。每张 "补打卡" 都可以补回一天的打卡记录，将原本
没打卡的一天变成打卡成功，获得一点满足感。 
问题来了，小胖要如何利用这 M 张"补打卡"，使自己过去 120 天跑步记录中的 "最
长连续打卡天数" 最大？
约束：0<=N<=120, 0<=M<=120，N和M都是正整数。
 
l 样例1： 
input： 5 2  10 30 55 56 90  output： 65   
 
l 样例2： input： 7 3  10 30 55 56 90 99 110  output： 79


第二届1024程序员节——极客大作战，等你来闯关 
 
l 说明：（以例1为例） 输入： 
第一行中，数字 5 代表一共的 N 次偷懒， 2 代表购买的补打卡张数 M, 以空格分隔；
 
第二行中，连续的 5个数字代表偷懒的实际日期, 从小到大排列，比如数字 10 代表过
去120天中的第 10天偷懒没有运动, 以空格分隔； 
输出： 
65代表使用2次补卡机会后，获得的最大连续运动天数。（针对样例1，补上第56和
90天性价比最高，最长的连续打卡记录即为从第56天到第120天，合计65天）

"""
