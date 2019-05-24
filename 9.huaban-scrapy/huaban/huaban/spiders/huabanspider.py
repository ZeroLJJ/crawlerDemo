# -*- coding: utf-8 -*-
import scrapy


class HuabanspiderSpider(scrapy.Spider):
    name = 'huabanspider'
    allowed_domains = ['huaban.com']
    start_urls = ['https://huaban.com/explore/rixirenx/']



    def parse(self, response):
        pass
