#!/usr/bin/env python3
# -*- coding: utf-8 -*-  文件编码设为utf-8
# __author__ = 'Zero'

import requests

# #这个方法可以接收三个参数，其中第二个默认为None 第三个可选
# def get(url, params=None, **kwargs)
# #作用是模拟发起GET请求
# Sends a GET request.
# #模拟获取页面的url链接
# :param url: URL for the new :class:Request object.
# #额外参数 字典或字节流格式，可选
# :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:Request.
# # 十二个控制访问参数，比如可以自定义header
# :param **kwargs: Optional arguments that request takes.
# # 返回一个Response对象
# :return: :class:Response <Response> object
# :type: requests.Response

hd = {'User-agent': '123'}
r = requests.get("http://www.baidu.com", headers=hd)

# kwargs: 控制访问的参数，均为可选项，以下为kwargs可用的key
# params : 字典或字节序列，作为参数增加到url中
# data : 字典、字节序列或文件对象，作为Request的内容 json : JSON格式的数据，作为Request的内容
# headers : 字典，HTTP定制头
# cookies : 字典或CookieJar，Request中的cookie
# auth : 元组，支持HTTP认证功能
# files : 字典类型，传输文件
# timeout : 设定超时时间，秒为单位
# proxies : 字典类型，设定访问代理服务器，可以增加登录认证
# allow_redirects : True/False，默认为True，重定向开关
# stream : True/False，默认为True，获取内容立即下载开关
# verify : True/False，默认为True，认证SSL证书开关
# cert : 本地SSL证书路径
# url: 拟更新页面的url链接
# data: 字典、字节序列或文件，Request的内容
# json: JSON格式的数据，Request的内容

# print(r.text)

# HTTP请求的返回状态，比如，200表示成功，404表示c失败
print("请求返回状态：%s" % r.status_code)
# HTTP请求中的headers
print("网页头：%s" % r.headers)
# 从header中猜测的响应的内容编码方式
print("从header获得编码：%s" % r.encoding)
# 从内容中分析的编码方式（慢）
print("从内容获得编码：%s" % r.apparent_encoding)
# 响应内容的二进制形式
#print ("二进制内容：%s" % r.content)