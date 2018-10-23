# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     job_name = scrapy.Field()
     job_price = scrapy.Field()
     job_addr  = scrapy.Field()
     company_name = scrapy.Field()
     job_url   = scrapy.Field()

