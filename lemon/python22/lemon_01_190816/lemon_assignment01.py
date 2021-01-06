# 一、下面那些不能作为标识符？
# 1、find     2、 _num   3、7val   4、add.    5、def
# 6、pan     7、-print   8、open_file 9、FileName   10、print
# 11、INPUT   12、ls     13、user^name  14、list1   15、str_

# 标识符的命名规则
# 1、标识符由字母、下划线、和数字组成，且数字不能开头
# 2、python中的标识符是区分大小写的
# 3、变量名一般用小写和下划线组成
# 4、不能和关键字和已有的名字冲突

# 不符合第一条的有：
# 3(数字开头)、4(点结尾)、7(中划线)
# 不符合第三条的有：
# 13(^)
# 不符合第四条的有：
# 5(def)、10(print)

# 不能作为标识符：3/4/5/7/9/10/13
# 9(驼峰可以用，不推荐)


# 关键字
# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

a = True
print(type(a))
print(3**3)
