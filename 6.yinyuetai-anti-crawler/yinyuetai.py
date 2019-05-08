#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   yinyuetai.py
@Time    :   2019/04/29 15:39:41
@Author  :   Zero
@Desc    :   
'''

# here put the import lib
import requests
import bs4
import random
import traceback


def get_html(url):
    try:
        r = requests.get(url, timeout=30, headers=get_agent(), proxies=get_proxy())
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        traceback.print_exc()
        return "error"


def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    # random.randint包上且包下，即random.randint(0, 10)，可以随机0-10的数字，包括0和10
    fakeheader['User-agent'] = agents[random.randint(0, len(agents)-1)]
    return fakeheader


def get_proxy():
    '''
    简单模拟代理池(以下皆是免费的ip代理，质量较差，容易失效，如遇ip失效或已被封请自行寻找)
    http://www.gatherproxy.com/zh/ 从这个找国际的ip比较容易成功，国内的大部分都被封了
    ip代理只是为了防止自己ip爬虫被网址封禁，所以用自己ip不用代理去爬，质量肯定会更好
    返回一个字典类型的键值对，
    '''
    proxy = ["181.176.209.86:8080",
             "190.102.154.131:8080",
             "103.240.206.152:55740"]
    random_ip = proxy[random.randint(0, len(proxy)-1)]
    fakepxs = {}
    fakepxs['http'] = 'http://' + random_ip
    fakepxs['https'] = 'https://' + random_ip
    return fakepxs


def get_content(url):
    #我们来打印一下表头
    if url[-2:]=="ML":
        print("内地排行榜")
    elif url[-2:]=="HT":
        print("香港排行榜")
    elif url[-2:]=="US":
        print("欧美排行榜")
    elif url[-2:]=="KR":
        print("韩国排行榜")
    else:
        print("日本排行榜")

    # 找到我们需要的每个li标签
    html = get_html(url)
    if html == 'error':
        print('网页获取失败')
    soup = bs4.BeautifulSoup(html, 'lxml')
    li_list = soup.find_all('li', attrs={'name': 'dmvLi'})
     
    for li in li_list:
        match = {}
        try:
            #判断分数的升降！
            if li.find('h3', class_='desc_score'):
                match['分数'] = li.find('h3', class_='desc_score').text
            else:
                match['分数'] = li.find('h3', class_='asc_score').text
            
            match['排名'] = li.find('div', class_='top_num').text
            match['名字'] = li.find('a', class_='mvname').text
            match['发布时间'] = li.find('p', class_='c9').text
            match['歌手'] = li.find('a', class_='special').text
        except:
            return ""
        print(match)



def main():
    base_url = "http://vchart.yinyuetai.com/vchart/trends?area="
    suffix = ['ML','HT','US','JP','KR']
    for suff in suffix:
        url = base_url+suff
        get_content(url)

if __name__ == '__main__':
    main()