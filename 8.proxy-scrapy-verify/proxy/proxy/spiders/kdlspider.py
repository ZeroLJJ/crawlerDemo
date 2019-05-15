# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.comm']
    start_urls = []

    # 通过简单的循环，来生成爬取页面的列表
    # 这里我们爬1~5页
    for i in range(1, 6):
        start_urls.append('https://www.kuaidaili.com/free/inha/' + str(i) + '/')

    def parse(self, response):
        # 我们先实例化一个item
        item = ProxyItem()

        # 通过Xpath找到每条代理的内容
        addr_list = response.xpath(
            '//table[@class="table table-bordered table-striped"]/tbody/tr')

        for addr in addr_list:
            # 找到ip地址
            ip = addr.xpath('td/text()').extract()[0]
            # 找到端口：
            port = addr.xpath('td/text()').extract()[1]
            # 将两者连接，并返回给item处理
            item['addr'] = ip + ':' + port
            yield item
