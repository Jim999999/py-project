# -*- coding: utf-8 -*-
import scrapy
from qiancheng.items import QianchengItem
import re

class QianspiderSpider(scrapy.Spider):
    name = 'qianSpider'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']

    def start_requests(self):
        bash_url = 'https://search.51job.com/list/030200,000000,0000,00,0,99,PHP%2B%25E5%25BC%2580%25E5%258F%2591,2,'
        ext_url = '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        job_lists = range(1,2)
        for i in job_lists :
            url = bash_url + str(i) + ext_url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        job_items = QianchengItem()
        job_names = response.css('div.el>p.t1 span>a::text')
        job_urls = response.css('div.el>p.t1 span>a[href]')
        job_companys = response.css('div.el>span.t2>a::text')
        job_addrs = response.css('div.el>span.t3::text')
        job_prices = response.css('div.el>span.t4::text')

        i = 0
        for name in job_names :

            job_items['job_name'] = name.extract().strip()
            job_items['job_price']= job_prices[i].extract()
            job_items['job_addr'] = job_addrs[i].extract()
            job_items['company_name'] = job_companys[i].extract()

            # 提取url
            job_url = job_urls[i].extract()
            pattern = '<a.*?href="(.+?)".*>'
            res = re.findall(pattern, job_url)
            job_items['job_url'] = res[0]
            yield  job_items
            i = i+1






