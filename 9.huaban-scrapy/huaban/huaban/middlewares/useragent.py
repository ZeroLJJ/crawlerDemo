#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/14 16:46
# @Author  : Zero
# @File    : useragent
# @Descr   : 

from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    # 随机跟换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')  # 从setting文件中读取RANDOM_UA_TYPE值

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):  ###系统电泳函数
        def get_ua():
            # getattr(object, name[, default]) 获取对象属性
            # object - - 对象。
            # name - - 字符串，对象属性。
            # default - - 默认返回值，如果不提供该参数，在没有对应属性时，将触发AttributeError。
            return getattr(self.ua, self.ua_type)

        # user_agent_random=get_ua()
        request.headers.setdefault('User_Agent', get_ua())
        pass
