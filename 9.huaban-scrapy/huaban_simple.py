#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/6 10:33
# @Author  : Zero
# @File    : huaban_simple.py
# @Descr   :
import os
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 建立浏览器对象 ，通过Chrome   headless表示无界面
from selenium.webdriver.support import ui

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=chrome_options)


def get_ids(url):
    try:
        # 访问url
        driver.get(url)

        # 等待一定时间，让js脚本加载完毕
        driver.implicitly_wait(4)
        # 屏幕翻滚次数
        scroll_num = 4
        # 总抓取到的id列表
        total_ids = []
        for i in range(1, scroll_num):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight/2);")
            time.sleep(4)
            content = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
            html = etree.HTML(content)
            ids = html.xpath('//*[@id="waterfall"]/div/@data-id')
            for id in ids:
                if id not in total_ids:
                    total_ids.append(id)

        # driver.close()
        return total_ids
    except Exception as e:
        return 'error'


def get_img(ids=None):
    imgs = []
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())   #获取当前时间
    dir_path = os.path.join(os.path.dirname(__file__), 'img('+now+')')  #图片目录路径
    os.mkdir(dir_path)  #创建图片目录
    if ids is None:
        ids = []
    for id in ids:
        url = 'https://huaban.com/pins/' + str(id)
        print("爬取url：%s页面中..." % url)
        driver.get(url)
        # 等待页面某个元素的加载，等待时长不超过60s
        waiter = ui.WebDriverWait(driver, 60)
        waiter.until(lambda d: driver.find_element_by_id("baidu_image_holder"))
        content = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        html = etree.HTML(content)
        # 获取出来的是数组(//从当前节点查找所有节点，/从当前节点查找子节点（只包含子节点）)
        img_url = html.xpath('//*[@id="baidu_image_holder"]//img/@src')
        # 用extend拼接数组
        imgs.extend(img_url)

        img_path = os.path.join(dir_path, id+'.jpg')
        with open(img_path, 'wb+') as f:
            src = 'https:' + img_url[0]
            f.write(requests.get(src).content)
        print("爬取url：%s页面完成:" % img_url)
    return imgs


if __name__ == '__main__':
    all_ids = get_ids('https://huaban.com/explore/rixirenx')
    print(get_img(all_ids))
