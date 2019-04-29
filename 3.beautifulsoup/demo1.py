# 导入bs4模块
from bs4 import BeautifulSoup
import os

htmlf=open(os.path.join(os.path.dirname(__file__), 'test.html'),'r',encoding="utf-8")
html=htmlf.read()
# 做一个美味汤
soup = BeautifulSoup(html, 'html.parser')
# 输出结果
print(soup.prettify())

# 找到文档的title
soup.title
# <title>The Dormouse's story</title>

# title的name值
soup.title.name
# u'title'

# title中的字符串String
soup.title.string
# u'The Dormouse's story'

# title的父亲节点的name属性
soup.title.parent.name
# u'head'

# 文档的第一个找到的段落
soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# 找到的p的class属性值
soup.p['class']
# u'title'

# 找到a标签
soup.a
# http://example.com/elsie" id="link1">Elsie

# 找到所有的a标签
soup.find_all('a')
# [http://example.com/elsie" id="link1">Elsie,
#  http://example.com/lacie" id="link2">Lacie,
#  http://example.com/tillie" id="link3">Tillie]

# 找到id值等于3的a标签
soup.find(id="link3")
# http://example.com/tillie" id="link3">Tillie

# 遍历所有a标签
for link in soup.find_all('a'):
    print(link.get('href'))