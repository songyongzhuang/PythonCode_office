# --*-- coding : utf-8 --*--
# Project      : python22
# Current file : module2.py
# Author       : Administrator
# Create time  : 2019-09-05 08:42
# IDE          : PyCharm
# from pack.module1 import zhuanqian

# 1、import 包名.模块名
import pack.module1

pack.module1.func_name('小花')

# 2、import 包名.模块名 as 别名
import pack.module1 as one

one.func_name('小花')

# 3、from 包名.模块名 import 函数(类)

from pack.module1 import func_name

func_name('小花456')

# 4、from 包名 import 模块名
from pack import module1

module1.func_name('小花')

# 5、from 包名 import 模块名 as 别名
from pack import module1 as two

two.func_name('小花')

# 6、第六种现阶段最好不要用，避免重名的现象
from pack.module1 import *

func_name('小花')

print(a)

# __main__ ,主程序 入口，你运行那一个文件，那个文件就叫:__main__
print(__name__)  # 打印模块的名称
