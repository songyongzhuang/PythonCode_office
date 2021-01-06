# --*-- coding ：utf-8 --*--
# Project      ：python22_web
# Current file ：wanshua.py
# Author       ：Administrator猜猜猜
# Create time  ：2019/12/13 18:16
# IDE          ：PyCharm
# TODO 成长很苦, 进步很甜, 加油！
import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir(r"D:\wzry\\" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir(r"D:\wzry\\" + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


downloadPic()
