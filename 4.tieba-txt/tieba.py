#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/04/28 11:09:15
@Author  :   Zero
@Desc    :   
'''

# here put the import lib
import os
import requests
from bs4 import BeautifulSoup

print(os.getcwd())

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码非200时，抛出异常
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。
        # 爬其他的页面时建议使用：apparent_encoding会从内容中分析出的响应内容编码方式
        # r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "
        
def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''

    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    # 我们来做一锅汤
    soup = BeautifulSoup(html, 'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中(strip移除头尾指定字符，默认为空格或换行)
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit '}).text.strip()
            # 采用css选择器进行筛选, class名称要正确, 多个空格也不行, 如class_=' j_th_tit'
            comment['link'] = "http://tieba.baidu.com/" + \
                li.find('a', class_="j_th_tit")['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')

    return comments


def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。
    open要加utf-8编码，不然window7默认为gbk编码，而页面爬取的为utf-8编码，将会出现编码异常
    '''
    with open(os.path.join(os.path.dirname(__file__), 'TTBT.txt'), 'r+', encoding='utf-8') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for i, url in enumerate(url_list):
        print("第 %d 次循环 begin" % (i+1))
        content = get_content(url)
        Out2File(content)
        print("第 %d 次循环 end" % (i+1))
    print('所有的信息都已经保存完毕！')


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3


# 当前模块文件作为主程序时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果当其他主程序的模块导入时，__name__置为文件名（不包括.py），if判断将失败，因此。
# 这种if测试可以让一个模块进行运行测试。
if __name__ == '__main__':
    main(base_url, deep)