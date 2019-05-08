#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/8 10:51
# @Author  : Zero
# @File    : iptest
# @Descr   : 

# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlwt

s = requests.session()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

rs = s.get(url="http://www.xicidaili.com/nn/", headers=header, verify=False)
# 还有一个网址获取国外代理Ip
#　http://www.gatherproxy.com/zh/，该例子爬取不了，被拒绝相应了，大概有什么反爬机制

soup = BeautifulSoup(rs.text, "lxml")
ip_list_all = []
ip_list = soup.select_one("#ip_list").select("tr")
ip_info_list_key = ["ip", "port", "address", "hidden", "type", "speed", "conn_time", "survival_time", "verify_time"]

for item in ip_list[1:]:
    ip_info_list_value = []
    ip_info = item.select("td")
    for info in ip_info[1:]:
        if info.select_one(".bar"):
            ip_info_list_value.append(info.select_one(".bar")["title"])
        else:
            ip_info_list_value.append(info.get_text().strip())
    # x=[1, 2, 3, 4, 5 ]
    # y=[6, 7, 8, 9, 10]
    # zip(x, y)就得到了
    # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
    # 再通过dict就得到{1:6, 2:7, 3:8, 4:9, 5:10}的字典了
    ip_list_all.append(dict(zip(ip_info_list_key, ip_info_list_value)))

print(len(ip_list_all))
# 写excel文件
w = xlwt.Workbook()  # 创建一个工作簿
ws = w.add_sheet(u"西刺免费代理IP")  # 创建一个工作表
ws.write(0, 0, u"序号")  # 在1行1列写入，u表示用unicode编码，python3默认是unicode编码，但python2默认是ascii码
ws.write(0, 1, u"IP地址")
ws.write(0, 2, u"端口")
ws.write(0, 3, u"服务器地址")
ws.write(0, 4, u"是否匿名")
ws.write(0, 5, u"类型")
ws.write(0, 6, u"速度")
ws.write(0, 7, u"连接时间")
ws.write(0, 8, u"存活时间")
ws.write(0, 9, u"验证时间")
i = 0
for item in ip_list_all:
    i += 1
    ws.write(i, 0, i)  # 在i+1行1列写入
    ws.write(i, 1, item["ip"])
    ws.write(i, 2, item["port"])
    ws.write(i, 3, item["address"])
    ws.write(i, 4, item["hidden"])
    ws.write(i, 5, item["type"])
    ws.write(i, 6, item["speed"])
    ws.write(i, 7, item["conn_time"])
    ws.write(i, 8, item["survival_time"])
    ws.write(i, 9, item["verify_time"])
w.save(u"免费代理IP.xls")  # 保存
print("写excel完成")