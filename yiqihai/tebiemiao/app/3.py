from selenium import webdriver
import lxml.html
import os
import json
import time


def parse_hero_url(http_url):
    # 获得浏览器对象
    pjs_path = r'D:/package/phantomjs-2.1.1-windows/bin/phantomjs.exe'
    browser = webdriver.PhantomJS(pjs_path)  # PhantomJS是无界面化浏览器
    # 发送请求
    browser.get(http_url)
    time.sleep(2)  # 延迟2秒
    # 详细提取数据  --获得网页源代码  page_source
    hero_html_content = browser.page_source
    # print(hero_html_content)
    # 关闭浏览器
    browser.quit()
    return hero_html_content


def get_data(data):
    # 获取etree对象
    metree = lxml.html.etree
    # 获取解析器对象
    parse = metree.HTML(data)
    # 开始解析
    hero_list = parse.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    print(len(hero_list))  # 查看我们爬取到几个英雄的信息
    # print(hero_list)
    list = []
    for li in hero_list:
        item = {}
        hero_name = li.xpath("./a/text()")[0]
        # print(hero_name)
        item['hero_name'] = hero_name
        hero_href_url = "https://pvp.qq.com/web201605/" + li_element.xpath("./a/@href")[0]
        # print(hero_href_url )
        item['hero_href_url '] = hero_href_url
        hero_image_url = "https:" + li_element.xpath(".//img/@src")[0]
        # print(hero_image_url )
        item['hero_image_url '] = hero_image_url
        # print(item)
        list.append(item)
    #         print(list)
    return list


# 保存文件
def save_file_json(datas):
    # 如果路径不存在，则创建
    path_name = './completehero'
    if not os.path.exists(path_name):
        os.makedirs(path_name)
        print('目录[%s]保存英雄信息创建成功！' % path_name)
    # 保存数据
    with open(path_name + '/completeherohero.json', 'w', encoding='utf-8') as f:
        json.dump(datas, f, ensure_ascii=False, indent=2)
    print('英雄数据保存成功，谢谢！')


def main():
    # 获得网页数据
    hero_url = "https://pvp.qq.com/web201605/herolist.shtml"
    # parse_hero_url(hero_url)
    hero_html_datas = parse_hero_url(hero_url)
    # print(hero_html_datas)
    # 提取数据
    hero_info_datas = get_data(hero_html_datas)
    # print(hero_info_datas)
    # 保存到文件中
    save_file_json(hero_info_datas)


if __name__ == '__main__':
    main()
