# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class ProxyPipeline(object):
    def process_item(self, item, spider):
        parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        open(os.path.join(parent_dir, 'proxy.txt'), 'a').write(item['addr'] + '\n')
        return item
