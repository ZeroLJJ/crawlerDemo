# -*- coding: utf-8 -*-

# Scrapy settings for huaban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huaban'

SPIDER_MODULES = ['huaban.spiders']
NEWSPIDER_MODULE = 'huaban.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'huaban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 设置下载延迟，避免被封锁
DOWNLOAD_DELAY = 2

RANDOM_UA_TYPE = 'chrome'  ##random    chrome,以供中间件配置读取

DOWNLOADER_MIDDLEWARES = {
    'proxy.middlewares.useragent.RandomUserAgentMiddleware': 543,
    'proxy.middlewares.useragent.SeleniumMiddleware': 544,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

ITEM_PIPELINES = {
    # 引入Scrapy提供的ImagesPipeline组件
    'scrapy.pipelines.images.ImagesPipeline': 1
}

# ImagesPipeline辅助配置项
# 图片存储路径(绝对路径 or 相对路径)
IMAGES_STORE = 'img/'
# 该字段的值为XxxItem中定义的存储图片链接的image_urls字段.(默认为image_urls)
IMAGES_URLS_FIELD = 'image_urls'
# 该字段的值为XxxItem中定义的存储图片信息的images字段.(默认为images)
IMAGES_RESULT_FIELD = 'images'
# 生成缩略图(可选)
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
# 过期时间,单位:天(可选)
IMAGES_EXPIRES = 120
# 过滤小图片(可选)
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
# 是否允许重定向(可选)
# MEDIA_ALLOW_REDIRECTS = True
