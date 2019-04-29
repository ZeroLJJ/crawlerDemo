#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/04/29 10:21:01
@Author  :   Zero
@Desc    :   
'''

# here put the import lib
from bs4 import BeautifulSoup
import requests
import os
import time


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 该网站采用gbk编码！
        r.encoding = 'gbk'
        return r.text
    except:
        return "error"


def get_movies(url):
    print('开始爬取》》》》》》》')
    html = get_html(url)
    if "error" == html:
        print('页面爬取失败')
        return
    soup = BeautifulSoup(html, 'lxml')

    # 找到电影排行榜的ul列表
    movies_list = soup.find('ul', class_='picList clearfix')
    # 去重小方法：url_list = list(set(url_list))
    movies = movies_list.find_all('li')

    now = time.strftime("%Y%m%d%H%M%S", time.localtime())   #获取当前时间
    dir_path = os.path.join(os.path.dirname(__file__), 'img('+now+')')  #图片目录路径
    os.mkdir(dir_path)  #创建图片目录

    for i, top in enumerate(movies):
        print('爬取第%d条中......' % (i+1))
        # 找到图片连接，
        img_url = 'http:' + top.find('img')['src']

        name = top.find('span', class_='sTit').a.text
        # 这里做一个异常捕获，防止没有上映时间的出现
        try:
            movie_time = top.find('span', class_='sIntro').text
        except:
            movie_time = "暂无上映时间"

        # 这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
        actors = top.find('p', class_='pActor')
        actor = ''
        for act in actors.contents:
            actor = actor + act.string + '  '
        # 找到影片简介
        intro = top.find('p', class_='pTxt pIntroShow').text

        print("片名：{}\t{}\n{}\n{} \n ".format(name, movie_time, actor, intro))

        # 我们来吧图片下载下来：
        name = name.replace(':' , '-')  #替换电影名中windows不允许的特殊字符
        img_path = os.path.join(dir_path, name+'.jpg')
        with open(img_path, 'wb+') as f:
            f.write(requests.get(img_url).content)
        print('第%d条爬取完成\n' % (i+1))


def main():
    url = 'http://dianying.2345.com/top/'
    get_movies(url)


if __name__ == "__main__":
    main()
