# -*- coding: utf-8 -*-
import scrapy
from ..items import Scrapy58Item
from pyquery import PyQuery

class Spider58Spider(scrapy.Spider):
    name = 'spider_58'
    allowed_domains = ['58.com']
    start_urls = ['http://bj.58.com/chuzu/']   #开始爬取的链接

    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li').items()  # 记得带上.items()
        for it in li_list:
            a_tag = it(' div.des > h2 > a')
            item = Scrapy58Item()
            item['name'] = a_tag.text()  # a_tag取出文本
            item['url'] = a_tag.attr('href')  # 取出href参数
            item['price'] = it('div.listliright > div.money > b').text()
            yield item  #把Item返回给引擎,可以不结束这个函数
