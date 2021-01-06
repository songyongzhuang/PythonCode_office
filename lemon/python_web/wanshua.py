# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：wanshua.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/13 18:16
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！

# TODO 王者荣耀英雄图片
import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号

print("只支持Windows操作系统，其他系统请绕行.")
drive = input("输入你想存放的盘符：(想存放到C盘就填写:C)")
a = input("输入你想存放的文件夹名称(只能写一个).")

# 创建文件夹
if os.path.exists(r"{}:\{}\\".format(drive, a)) is True:
    print('文件夹已存在, 开始下载英雄图片.')
else:
    os.mkdir(r"{}:\{}\\".format(drive, a))
    print('创建了文件夹'.format())


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir(r"{}:\{}\\".format(drive, a) + hero_name[i])
        print("创建了新文件夹：{}".format(hero_name[i]))
        # 进入创建好的文件夹
        os.chdir(r"{}:\{}\\".format(drive, a) + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()
print("下载完毕，请去{}盘{}文件夹查看结果".format(drive, a))
