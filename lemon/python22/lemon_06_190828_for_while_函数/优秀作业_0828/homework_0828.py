print('****************** task1 *****************')
user_input = input('请输入3个整数，以空格分隔：')


def max_value(numbers):
    '''
        根据用户输入，求最大值
    '''
    numbers = user_input.split(' ')
    num_list = []   # 空列表
    for i in range(len(numbers)):
        num_list.append(int(numbers[i]))
    num_list.sort(reverse=True)  # 排序
    max_num = num_list[0]       # 取最大值
    return max_num


max_num = max_value(user_input)
print('您输入的3个数中，最大数是：{}'.format(max_num))

# print('****************** task2 *****************')
# print('九九乘法表 - for实现')
# for row in range(1, 10):
#     for column in range(1, row + 1):
#         result = column * row
#         print('{} * {} = {}\t'.format(column, row, result), end=' ')
#     print()   # 换行
#
# print('九九乘法表 - while实现')
# row = 1
# while(row <= 9):
#     column = 1      # 每次都初始化列变量
#     while(column <= row):
#         result = column * row
#         print('{} * {} = {}\t'.format(column, row, result), end=' ')
#         column += 1
#     row += 1
#     print()     # 换行

# print('****************** task3 *****************')
# black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# black_list.clear()
# print(black_list)

# print('****************** task4 *****************')
# a = [1, 7, 4, 89, 34, 2]
# len_a = len(a)
# new_a = []  # 排序后存放的列表
# for times in range(len_a):
#     min_a = a[0]
#     for index in range(1, len(a)):  # a的第一个成员和其他的比较
#         if min_a >= a[index]:
#             min_a = a[index]
#     new_a.append(min_a)             # 最小的数放到new_a中
#     a.pop(a.index(min_a))           # 比完一轮，把最小的数删掉
# print('从小到大比较结果：{}'.format(new_a))

# print('****************** task5 *****************')
# def login(user_name, pwd):
#     if user_name == 'lemon' and pwd == 'best':
#         print('登录成功')
#     else:
#         print('用户名或密码错误')
#
#
# user_name = input('请输入用户名：')
# password = input('请输入密码：')
# login(user_name, password)
