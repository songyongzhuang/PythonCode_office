# -*- coding:utf-8 -*-

# 5. .编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best

print("*" * 20 + "方法一" + "*" * 20)
def login_info():
    """
     接受用户输入的用户名和密码
    """
    userName = input("请输入用户名： ")
    passWord = input("请输入密码: ")
    return userName, passWord
# 调用函数与正确的用户名和密码进行判断
if login_info() == ("lemon", "best"):
    print("登录系统成功")
else:
    print("用户名或密码错误")


print("*" * 20 + "方法二" + "*" * 20)
def login_judge():
    """
     接受用户输入的用户名和密码，并与正确的信息进行判断
    """
    # 提示用户输入用户名
    userName = input("请输入用户名： ")
    # 提示用户输入密码
    passWord = input("请输入密码: ")
    true_name = "lemon"
    true_password = "best"
    # 输入的用户名信息和密码与正确的信息进行判断
    if userName == true_name and passWord == true_password:
        print("登录系统成功！")
    elif userName == true_name and passWord != true_password:
        print("您输入的密码错误！")
    elif userName != true_name and passWord ==true_password:
        print("您输入的用户名错误！")
    else:
        print("您输入的用户名和密码都错误！")
# 调用登录判断函数
login_judge()