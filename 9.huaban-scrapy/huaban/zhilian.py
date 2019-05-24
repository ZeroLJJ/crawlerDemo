#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/6 10:33
# @Author  : Zero
# @File    : zhilian.py
# @Descr   :
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import random
import traceback



def get_html(url):
    try:
        # 建立浏览器对象 ，通过Chrome   headless表示无界面
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

        # 访问url
        driver.get(url)

        # 等待一定时间，让js脚本加载完毕
        driver.implicitly_wait(4)
        # 获取页面源码
        # content = driver.page_source.encode('utf-8')
        # 执行js得到整个HTML
        # content = driver.execute_script("return document.documentElement.outerHTML")
        # 等待页面某个元素的加载，等待时长不超过60s
        # waiter = ui.WebDriverWait(driver, 60)
        # waiter.until(lambda d: driver.find_element_by_class_name("contentpile__content__wrapper"))
        # 获得整个文档的HTML(通过以下方式才能获取智联页面的完整代码)
        for i in range(1, 3):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(4)
        content = driver.find_element_by_xpath("//*").get_attribute("outerHTML")

        # 通过selenium在获取包含多个class名称的tag对象时，建议使用：
        # find_element_by_css_selector(".xx.xxx.xxxxx")
        # 或者
        # find_element_by_css_selector("[class='xx xxx xxxxx']")
        # div_list = driver.find_element_by_css_selector("[class='contentpile__content__wrapper clearfix']")
        driver.close()
        return content
    except Exception as e:
        return 'error'

# </div></div><a href="/pins/
if __name__=='__main__':
    print(get_html('https://huaban.com/explore/rixirenx/'))