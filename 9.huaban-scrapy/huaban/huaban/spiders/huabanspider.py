# -*- coding: utf-8 -*-
import scrapy
from huaban.items import HuabanItem


class HuabanspiderSpider(scrapy.Spider):
    name = 'huabanspider'
    allowed_domains = ['huaban.com']
    start_urls = ['https://huaban.com/explore/rixirenx/']

    item = HuabanItem()

    def parse(self, response):
        img_list = response.xpath('//*[@id="waterfall"]/div[contains(@class, "pin")]/@data-id')
        for img_item in img_list:
            url = 'https://huaban.com/pin/' + img_item
            yield scrapy.Request(url, callback=self.post_page)

    def post_page(self, response):
        # images_url = response.xpath("//div[@id='entry-content']//img/@src").extract()
        # self.item['image_urls'] = images_url
        return self.item
