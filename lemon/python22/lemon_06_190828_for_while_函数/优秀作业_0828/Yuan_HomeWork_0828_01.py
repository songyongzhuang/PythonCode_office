# -*-coding=utf-8-*-

# 1.求三个整数中的最大值
print("*" * 30 + "方法一"+"*" * 30)

# 提示用户输入第一个整数
number_one = input("请输入第一个整数： ")

# 提示用户输入第二个整数个整数
number_two = input("请输入第二个整数： ")

# 提示用户输入第三个整数
number_three = input("请输入第三个整数： ")

# 判定输入的字符串全为数字或带负荷的数字
while (number_one.isdigit() and number_two.isdigit() and number_three.isdigit()) \
        or '-' in number_one or '-' in number_two or '-' in number_three:
    # 判定number_one最大
    if number_one > number_two and number_one > number_three:
        print("最大数是：{}".format(number_one))
    # 判定number_two最大
    elif number_two > number_one and number_two > number_three:
        print("最大数是：{}".format(number_two))
    # 否则number_three最大
    else:
        print("最大数是：{}".format(number_three))
    break

print("*" * 30 + "方法二"+"*" * 30)

# 提示用户输入要比较整数的个数
numbers = input("请输入要比较多少个整数： ")

# 判定输入要比较的整数个数是否全为数字
if numbers.isdigit():
    # 提示用户输入第一个整数
    number_max = input("请输入第1个整数： ")
    nums = int(numbers)
    # 循环提示输入数据
    for i in range(nums-1):
        number_x = input("请输入第{}整数: ".format(i + 2))
        # 将输入的number_x数据与number_max比较
        if number_x > number_max:
            # 将大的数据赋值给number_max
            number_max = number_x
    print("最大数是：{}".format(number_max))
else:
    print("输入数据错误")
