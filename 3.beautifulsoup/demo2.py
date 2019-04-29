# 导入bs4模块
from bs4 import BeautifulSoup
import os

htmlf = open(os.path.join(os.path.dirname(__file__), 'test.html'), 'r', encoding="utf-8")
html=htmlf.read()
# 推荐使用lxml解析
soup=BeautifulSoup(html, 'lxml')

# 对象的种类：
# bs4 库将复杂的html文档转化为一个复杂的树形结构，每个节点都是Python对象 ，所有对象可以分为以下四个类型：
# Tag , NavigableString , BeautifulSoup , Comment
# 我们来逐一解释：

# Tag： 和html中的Tag基本没有区别，可以简单上手使用
# NavigableString： 被包裹在tag内的字符串
# BeautifulSoup： 表示一个文档的全部内容，大部分的时候可以吧他看做一个tag对象，支持遍历文档树和搜索文档树方法。
# Comment：这是一个特殊的NavigableSting对象，在出现在html文档中时，会以特殊的格式输出，比如注释类型。

# 获取所有的标签
tag=soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 假设我们要找到a标签中的第二个元素：
need=tag[1]
print(need)


# tag的.contents属性可以将tag的子节点以列表的方式输出：
head_tag=soup.head
print(head_tag)
# <head><title>The Dormouse's story</title></head>
head_contents=head_tag.contents
print(head_contents)
title_tag=head_tag.contents[0]
print(title_tag)

# 通过tag的 .children生成器，可以对tag的子节点进行循环：
for child in head_tag.title.children:
    print(child)
# 这种方式只能遍历出子节点。如何遍历出子孙节点呢？

# 子孙节点：比如 head.contents 的子节点是<title>The Dormouse's story</title>,
# 这里 title本身也有子节点：‘The Dormouse‘s story’ 。
# 这里的‘The Dormouse‘s story’也叫作head的子孙节点

for child in head_tag.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story

# 如何找到tag下的所有的文本内容呢？
# 如果该tag只有一个子节点（NavigableString类型）：直接使用tag.string就能找到。
# 如果tag有很多个子、孙节点，并且每个节点里都string：
# 我们可以用迭代的方式将其全部找出：

for string in soup.strings:
    print(repr(string))
