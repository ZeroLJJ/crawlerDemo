#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/24 11:21
# @Author  : Zero
# @File    : SeleniumMiddleware
# @Descr   : 

from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumMiddleware(object):
    def __init__(self):
        # 建立浏览器对象 ，通过Chrome   headless表示无界面
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        self.browser.set_page_load_timeout(30)

    def __del__(self):
        self.browser.close()


    def process_request(self, request, spider):
        if spider.name == 'huabanspider':
            try:
                spider.browser.get(request.url)
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            except TimeoutException as e:
                print('超时')
                spider.browser.execute_script('window.stop()')
            time.sleep(2)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",
                                request=request)
