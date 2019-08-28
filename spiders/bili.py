# -*- coding: utf-8 -*-

'''
json 文件地址
https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E9%9B%86%E7%BE%8E%E5%A4%A7%E5%AD%A6&from_source=banner_search&page=3&jsonp=jsonp

视频播放的地址
arcurl":"http:\/\/www.bilibili.com\/video\/av45237546
'''
import scrapy
import json
import os

class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E9%97%BD%E6%B1%9F%E5%AD%A6%E9%99%A2&page=1&jsonp=jsonp']

    def parse(self, response):
        url="https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E9%97%BD%E6%B1%9F%E5%AD%A6%E9%99%A2&page={}&jsonp=jsonp"

        decodejson= response.body.decode()
        # print(decodejson)
        decodejson=json.loads(decodejson).get('data')
        numPages = decodejson['numPages']
        items = decodejson['result']
        print(numPages)
        n=2
        n+=1
        if n > int(numPages):
            return 0

        for i in items:
            item={}
            item['title']=i['title']
            item['arcurl']=i['arcurl']
            yield item
            yield scrapy.Request(url=url.format(n),callback=self.parse)

