# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyuSpiderSpider(scrapy.Spider):

    #定义爬虫名称
    name = 'douyu_spider'
    #允许的域名，可省
    allowed_domains = ['douyucdn.cn']
    #组装url
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    #开始爬取的urls
    start_urls = [base_url+str(offset)]

    #解析函数
    def parse(self, response):
        # response.body 为二进制编码，需转为utf-8
        results = json.loads(response.body.decode('utf-8'))['data']
        if len(results) == 0:
            print('crawing over ! spider stop!')
            exit()

        for li in results:
            item = DouyuItem()
            # print(li['nickname'])
            # print(li['room_src'])
            # print('#'*30)
            item['nickname'] = li['nickname']
            item['link'] = li['room_src']
            #yield 給pipelines
            yield  item

        #跟进 下载 另一页面
        self.offset += 20
        href = self.base_url + str(self.offset)
        #注意，此处是 关键词 yield 一个scrapy.Request()
        yield  scrapy.Request(href,callback=self.parse)


