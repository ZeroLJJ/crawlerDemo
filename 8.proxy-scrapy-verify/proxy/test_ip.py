#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/15 10:34
# @Author  : Zero
# @File    : test_ip
# @Descr   :
import os
import random
import requests
# 引入这个库来获得map函数的并发版本
from multiprocessing.dummy import Pool as ThreadPool

# 定义全局变量
dir_path = os.path.abspath(os.path.dirname(__file__))
alive_ip = []

# 使得map并发！实例化pool对象 并 设置并发数量
pool = ThreadPool(20)


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


def test_alive(proxy):
    '''
    一个简单的函数，
    来判断通过代理访问百度
    筛选通过的代理保存到alive_ip中
    '''
    global alive_ip
    # 设置代理头
    proxies = {'http': proxy}
    print('正在测试：{}'.format(proxies))
    try:
        r = requests.get('http://www.baidu.com', headers=get_agent(), proxies=proxies, timeout=3)
        if r.status_code == 200:
            print('该代理：{}成功存活'.format(proxy))
            alive_ip.append(proxy)
    except:
        print('该代理{}失效！'.format(proxies))


def out_file(ip_list=[]):
    # 将符合要求的代理写入文件
    global dir_path
    with open(os.path.join(dir_path, 'alive_ip.txt'), 'a+') as f:
        for ip in ip_list:
            f.write(ip + '\n')
        print('所有存活ip都已经写入文件！')


def test(filename='blank.txt'):
    # 循环处理每行文件
    with open(os.path.join(dir_path, filename), 'r') as f:
        lines = f.readlines()
        # 我们去掉lines每一项后面的\n\r之类的空格
        # 生成一个新的列表！
        proxys = list(map(lambda x: x.strip(), [y for y in lines]))

        # 一行代码解决多线程！
        pool.map(test_alive, proxys)

    # 将存活的ip写入文件
    out_file(alive_ip)


# 调用函数！
if __name__ == '__main__':
    test('proxy.txt')
