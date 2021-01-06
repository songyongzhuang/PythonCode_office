from fake_useragent import UserAgent
import json, requests


# 获取皮肤数据
def read_heroskin():
    skin_file = open('./completehero/completeheroskin.json', 'r', encoding='utf-8')
    skin_file_data = json.load(skin_file)
    # print(skin_file_data)
    return skin_file_data


def downskin():
    # 1.读取保存的json皮肤数据
    heroskindata = read_heroskin()
    # print(heroskindata)
    i = 0
    while i < len(heroskindata):
        hero = heroskindata[i]
        # print("第%d个英雄："%i,hero)

        # 2. 遍历获取单个英雄数据，英雄名称，皮肤列表
        # 英雄名称
        hero_name = hero.get("hero_name")
        skin_path = './completehero/pictures/' + hero_name
        # print("存放路径:",skin_path)
        # 皮肤列表
        skin_list = hero.get("skin_hero_list")
        # print("皮肤列表:",skin_list)

        # 3. 遍历皮肤列表，获得单个皮肤，名称，图片下载地址
        for skin_element in skin_list:
            # print(skin_element)
            # 皮肤名称
            skin_name = skin_element['skin_name']
            # 图片下载地址
            skin_url = skin_element['skin_url']
            # print("皮肤名称:%s,地址:%s"%(skin_name,skin_url))

            # 4.通过图片地址下载皮肤图片
            # 图片内容
            headers = {
                "User-Agent": UserAgent().chrome  # chrome浏览器随机代理
            }
            response = requests.get(skin_url, headers=headers)
            image_content = response.content
            # 下载图片
            with open(skin_path + '/' + skin_name + '.jpg', 'wb') as f:
                f.write(image_content)
            print("正在下载英雄%s的皮肤图片，皮肤名称%s" % (hero_name, skin_name))
        print("已成功下载英雄%s得皮肤图片" % hero_name)
        i += 1
    print("所有英雄的皮肤图片均已下载完毕，谢谢")


if __name__ == '__main__':
    downskin()
