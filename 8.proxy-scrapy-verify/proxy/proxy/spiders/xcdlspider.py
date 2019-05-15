# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class XcdlspiderSpider(scrapy.Spider):
    name = 'xcdlspider'
    allowed_domains = ['xicidaili.com']
    start_urls = []

    # 通过简单的循环，来生成爬取页面的列表
    # 这里我们爬1~5页
    for i in range(1, 6):
        start_urls.append('https://www.xicidaili.com/wt/' + str(i) + '/')

    def parse(self, response):
        # 我们先实例化一个item
        item = ProxyItem()

        # 通过Xpath找到每条代理的内容(忽略表头那行)
        addr_list = response.xpath('//*[@id="ip_list"]/tbody/tr[position()>1]')
        if len(addr_list) == 0:
            addr_list = response.xpath('//*[@id="ip_list"]/tr[position()>1]')

        for addr in addr_list:
            # 找到ip地址(因为第一个td不含文本，所以不包含第一个td)
            ip = addr.xpath('td/text()').extract()[0]
            # 找到端口：
            port = addr.xpath('td/text()').extract()[1]
            # 将两者连接，并返回给item处理
            item['addr'] = ip + ':' + port
            yield item
