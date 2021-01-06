# --*-- coding : utf-8 --*--
# Project      : Python_practice
# Current file : 九九乘法口诀.py
# Author       : 大壮
# Create time  : 2019-11-14 19:53
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
"""
# 使用for循环
for i in range(1, 10):
    for j in range(1, i+1):  # 一定要加一记住了
        print(f'{i}*{j}={i*j}', end=' ')
    print()


# 使用while循环
a = 1
while a < 10:
    b = 1
    while b <= a:
        print(f'{a}*{b}={a*b}', end=' ')
        b += 1
    a += 1
    print()
"""

# 只处理Windows的上传
import win32gui
import win32con

'''
# 导出文件 Windows 窗口
def export(filePath, browser_type="chrome"):
    """
    :param filePath: 传入文件路径 绝对路径 例如："E:\WebWebpageTest\酒店商品销售明细表.xls"
    :param browser_type: 浏览器默认 chrome(谷歌)

    # Edit - ComboBox - ComboBoxEx32 - #32770
    # 找到输入框和打开按钮 元素；2、输入地址，点击打开。
    # 前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。
    """
    # 这个是判断的浏览器，不同的浏览器上传的 title(标题头) 是不一样的
    if browser_type == "chrome":
        title = "另存为"
    else:
        title = ""

    # 找元素
    # 一级窗口 顶级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", title)  # 一级
    # FindWindowEx 在爸爸的基础上找后代，1、爸爸是谁. 2、0. 3、找什么类型的后代. 4、有文本写文本，没有文体写 None
    DUIViewWndClassName = win32gui.FindWindowEx(dialog, 0, "DUIViewWndClassName", None)  # 三级
    DirectUIHWND = win32gui.FindWindowEx(DUIViewWndClassName, 0, "DirectUIHWND", None)  # 四级
    FloatNotifySink = win32gui.FindWindowEx(DirectUIHWND, 0, "FloatNotifySink", None)  # 五级
    ComboBox = win32gui.FindWindowEx(FloatNotifySink, 0, "ComboBox", None)  # 六级
    # 编辑存储路径
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 七级
    # 保存按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "保存(&S)")  # 二级
    # 往编辑当中，输入文件路径 。
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击保存按钮

# 另存为
export(r"E:\WebWebpageTest\酒店商品销售明细表(2020-03-25 10_45_22).xls")
'''
