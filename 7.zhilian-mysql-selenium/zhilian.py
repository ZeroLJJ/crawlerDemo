#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/6 10:33
# @Author  : Zero
# @File    : zhilian.py
# @Descr   : 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import random
import traceback

from selenium.webdriver.support import ui


def get_html(url):
    try:
        # 建立浏览器对象 ，通过Chrome   headless表示无界面
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

        # 访问url
        driver.get(url)

        # 等待一定时间，让js脚本加载完毕
        driver.implicitly_wait(10)
        # 获取页面源码
        # content = driver.page_source.encode('utf-8')
        # 执行js得到整个HTML
        # content = driver.execute_script("return document.documentElement.outerHTML")
        # 等待页面某个元素的加载，等待时长不超过60s
        waiter = ui.WebDriverWait(driver, 60)
        waiter.until(lambda d: driver.find_element_by_class_name("contentpile__content__wrapper"))
        # 获得整个文档的HTML(通过以下方式才能获取智联页面的完整代码)
        content = driver.find_element_by_xpath("//*").get_attribute("outerHTML")

        # 通过selenium在获取包含多个class名称的tag对象时，建议使用：
        # find_element_by_css_selector(".xx.xxx.xxxxx")
        # 或者
        # find_element_by_css_selector("[class='xx xxx xxxxx']")
        # div_list = driver.find_element_by_css_selector("[class='contentpile__content__wrapper clearfix']")
        driver.close()
        return content
    except Exception as e:
        return 'error'


def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    return agents[random.randint(0, len(agents))]


def get_content(url):
    html = get_html(url)
    if html == 'error':
        print('页面获取失败')
        return ''

    list = [] # 招聘信息列表

    soup = BeautifulSoup(html, 'lxml')
    div_list = soup.select('div.contentpile__content__wrapper__item.clearfix')
    for item in div_list:
        obj = {} # 招聘信息
        obj['url'] = item.select_one('a')['href']
        obj['company_name'] = item.select_one('.contentpile__content__wrapper__item__info__box__cname__title.company_title').get_text()
        obj['job_name'] = item.select_one('span.contentpile__content__wrapper__item__info__box__jobname__title')['title']
        obj['salary'] = item.select_one('p.contentpile__content__wrapper__item__info__box__job__saray').get_text()
        demand_list = item.select('ul.contentpile__content__wrapper__item__info__box__job__demand li')
        obj['address'] = demand_list[0].get_text()
        obj['experience'] = demand_list[1].get_text()
        obj['education'] = demand_list[2].get_text()
        company_descr = item.select('div.contentpile__content__wrapper__item__info__box__job__comdec span')
        obj['company_type'] = company_descr[0].get_text()
        obj['company_num'] = company_descr[1].get_text()
        i = 0 # 福利的循环起点
        if len(item.select('.contentpile__content__wrapper__eager-talents')) > 0:
            i = 1  # 第一项为求贤的内容，非福利，需要跳过
            obj['if_eager'] = True
        else:
            obj['if_eager'] = False
        welfare_list = item.select('.contentpile__content__wrapper__item__info__box__welfare__item')
        welfare = ''
        for welfare_item in welfare_list[i:]:
            welfare = welfare + welfare_item.get_text() + " "
        obj['welfare'] = welfare
        obj['status'] = item.select_one('span.contentpile__content__wrapper__item__info__box__status__recruit').get_text()
        list.append(obj)
    print(list)
    return list

# 获取数据库连接
def get_connection():
    connection = pymysql.connect(host='localhost',      #ip
                                 user='root',           #用户名
                                 password='lingshi',    #密码
                                 db='zhilian',          #库名
                                 charset='utf8',        #编码
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# 连接到数据库
def db_save(list):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # 使用executemany批量增加记录
            # sql = "INSERT INTO `recruitment` (`url`, `company_name`, `company_type`, " \
            #       "`company_num`, `job_name`, `salary`, `address`, " \
            #       "`experience`, `education`, `welfare`, `if_eager`, " \
            #       "`status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # 使用executemany添加的数据的格式必须为list[tuple(),tuple()]或者tuple(tuple(),tuple())，且顺序对应
            # cursor.executemany(sql, list)
            if len(list) == 0:
                print('数据长度为0，保存失败')
                return
            sql = "INSERT INTO `recruitment` (`url`, `company_name`, `company_type`, " \
                  "`company_num`, `job_name`, `salary`, `address`, " \
                  "`experience`, `education`, `welfare`, `if_eager`, " \
                  "`status`) VALUES "
            for item in list:
                sql += "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}'),".format(
                    item['url'], item['company_name'], item['company_type'], item['company_num'],
                    item['job_name'], item['salary'], item['address'], item['experience'],
                    item['education'], item['welfare'], item['if_eager'], item['status'])
            # 截取掉最后一个逗号，切片包上不包下
            sql = sql[:-1]
            cursor.execute(sql)
            print('数据保存成功')
        # 手动保存刚才的添加操作
        connection.commit()
    except Exception as e:
        traceback.print_exc()
        print('数据保存失败')
    finally:
        connection.close()


def main():
    # 设置访问的url
    url = 'https://sou.zhaopin.com/?jl=682&kw=Java%E5%BC%80%E5%8F%91&kt=3&sf=0&st=0'

    list = get_content(url)

    db_save(list)


if __name__=='__main__':
    main()