# 引入模块
from urllib import request

url = "http://www.baidu.com"

# 第一种下载网页的方法
# print("第一种方法:")
# # request = urllib.urlopen(url)  2.x
# response1 = request.urlopen(url)
# print("状态码:", response1.getcode())
# # 获取网页内容
# html = response1.read()
# # 设置编码格式
# print(html.decode("utf8"))
# # 关闭response1
# response1.close()


# 第二种下载网页的方法
# print("第二种：")
# request2 = request.Request(url)
# request2.add_header('user-agent','Mozilla/5.0')
# response2 = request.urlopen(request2)
# print("状态码:",response2.getcode())
# #获取网页内容
# htm2 = response2.read()
# #调整格式
# print(htm2.decode("utf8"))
# #关闭response1
# response2.close()


import http.cookiejar
cookie = http.cookiejar.LWPCookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(opener)
response3 = request.urlopen(url)
print(cookie)
html3 = response3.read()
#将内容格式排列
print(html3.decode("utf8"))
response3.close()